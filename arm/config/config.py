#!/usr/bin/python3

import os
import yaml

yamlfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../..", "arm.yaml")

with open(yamlfile, "r") as f:
    try:
        cfg = yaml.load(f, Loader=yaml.FullLoader)
    except Exception:
        cfg = yaml.safe_load(f)  # For older versions use this


_arm_version = None
def get_arm_version():
    """ Get the version of this instance of the automatic-ripping-machine """
    global _arm_version
    if _arm_version is None:
        with open(os.path.join(cfg["INSTALLPATH"], 'VERSION')) as version_file:
            _arm_version = version_file.read().strip()
    return _arm_version
