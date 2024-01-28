#!/usr/bin/python3
"""
1. Compress before sending
to web server
"""

from fabric.api import *
from datetime import datetime


def do_pack():
    """
    must return the archive path if the archive has been
    correctly generated. Otherwise, it should return None
    """
    now = datetime.now()
    time_string = now.strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(time_string)
    local("mkdir -p versions")
    archive_path = "versions/{}".format(archive_name)
    command = "tar -czvf {} web_static".format(archive_path)
    result = local(command)
    if result.failed:
        return None
    return archive_path
