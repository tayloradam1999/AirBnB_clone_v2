#!/usr/bin/python3
""" Fabric File """

from fabric.api import local, env, run
import os

env.hosts = ['54.221.48.50', '3.85.236.151']


def do_clean(number=0):
    """ Deletes out-of-date archives """

    """typecasting cmd line string into int if it exists and defaulting to
    at least 1
    """
    number = int(number)
    if number == 0:
        number = 1

    # removing local tar files
    localFiles = os.listdir('versions')
    for i, file in enumerate(localFiles):
        if i >= number:
            local("sudo rm versions/" + file)

    # removing foreign unzipped directories
    foreignFiles = run("ls -t /data/web_static/releases").split()
    for i, file in enumerate(foreignFiles):
        if i >= number:
            run("sudo rm -r /data/web_static/releases/" + file)
