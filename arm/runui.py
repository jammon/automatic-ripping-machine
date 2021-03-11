#!/usr/bin/env python3

from arm.ui import app
from arm.config.config import cfg


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
