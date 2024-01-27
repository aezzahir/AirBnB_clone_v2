#!/usr/bin/python3
"""
2. Deploy archive!
to my web severs
"""
from fabric.api import *
import os

env.hosts = ['54.196.41.205', '18.234.253.112']


def do_deploy(archive_path):
    """Distributes an achive to your web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1]
        no_extension = file_name.split(".")[0]
        release_path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(release_path, no_extension))
        run('tar -xzf /tmp/{} -C {}{}/'.format(
            file_name, release_path, no_extension))
        run('rm /tmp/{}'.format(file_name))
        run('mv {}/web_static/* {}/'.format(
            release_path + no_extension, release_path + no_extension))
        run('rm -rf {}/web_static'.format(release_path + no_extension))
        run('rm -rf /data/web_static/current')
        run('ln -s {}/ /data/web_static/current'.format(
            release_path + no_extension))
        return True
    except Exception as e:
        print("Error: {}".format(str(e)))
        return False