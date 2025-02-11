#!/usr/bin/python3
""" A certain sentence to exceed the word count """

from fabric.api import local, env, put, run
from datetime import datetime
import os.path

env.hosts = ['34.73.206.41', '35.175.196.34']


def do_deploy(archive_path):
    """ Deploys our web_static archive """

    try:
        if not os.path.exists(archive_path):
            return False

        archiveName = archive_path[9:]
        archiveNameNoExtension = archiveName[:-4]

        put(archive_path, '/tmp/' + archiveName)
        run("mkdir -p /data/web_static/releases/" + archiveNameNoExtension)
        run("tar -xzvf /tmp/" +
            archiveName +
            " -C " +
            "/data/web_static/releases/" +
            archiveNameNoExtension +
            " --strip-components=1")
        run("rm -f /tmp/" + archiveName)
        run("rm -f /data/web_static/current")
        run("sudo ln -sf /data/web_static/releases/" +
            archiveNameNoExtension +
            " /data/web_static/current")

        return True
    except:
        return False


def do_pack():
    """ Pack up our web_static """

    try:
        now = datetime.now()

        tarArchiveName = "web_static_" + now.strftime("%Y%m%d%H%M%S") + ".tgz"
        tarArchivePath = "versions/" + tarArchiveName

        local("mkdir -p versions")

        local("tar -czvf " + tarArchivePath + " web_static")

        return tarArchivePath
    except:
        return None
