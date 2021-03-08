import os  # noqa: F401
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from arm.ui import app  # noqa E402
from arm.config.config import cfg  # noqa E402
import arm.ui.routes  # noqa E402

LOCALHOST = '127.0.0.1'
AUTODETECT = 'x.x.x.x'


def detect_ip_address():
    # If there are one or more different from LOCALHOST
    #   then take the first one found
    #   else use LOCALHOST
    from netifaces import interfaces, ifaddresses, AF_INET
    for interface in interfaces():
        inet_links = ifaddresses(interface).get(AF_INET, [])
        for link in inet_links:
            ip = link['addr']
            if ip != LOCALHOST:
                return ip
    return LOCALHOST


if __name__ == '__main__':
    host = cfg['WEBSERVER_IP']
    if host == AUTODETECT:
        host = detect_ip_address()
    app.run(host=host, port=cfg['WEBSERVER_PORT'], debug=True)
