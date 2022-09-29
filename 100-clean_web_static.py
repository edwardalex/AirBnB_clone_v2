#!/usr/bin/python3
""" 4. Keep it clean!  """
from fabric.api import *
from datetime import datetime
from os import path

env.hosts = ['34.229.63.14', '100.27.49.144']


@runs_once
def do_pack():
    """ Generate compressed file """
    try:
        today = datetime.now().strftime('%Y%m%d%H%M%S')
        path = "versions/web_static_{:s}.tgz".format(today)

        msg1 = "Packing web_static to {:s}".format(path)
        print(msg1)

        with hide('running'):
            local('mkdir -p ./versions')

        local('tar -cvzf {:s} web_static'.format(path))

        with hide('running'):
            size = local('wc -c < {:s}'.format(path), capture=True)

        msg2 = 'web_static packed: {:s} -> {:s}Bytes'.format(path, size)
        print(msg2)

        return path

    except:
        return None


def do_deploy(archive_path):
    """ Do deploy """
    if not path.exists(archive_path):
        return False

    path_nx = path.splitext(archive_path)[0]
    path_nx = path_nx.split('/')[-1]
    path_yx = path_nx + '.tgz'

    try:
        put(archive_path, "/tmp/")

        run('mkdir -p /data/web_static/releases/{:s}/'.format(path_nx))

        run('tar -xzf /tmp/{:s} -C /data/web_static/releases/{:s}/'.
            format(path_yx, path_nx))

        run('rm /tmp/{:s}'.format(path_yx))

        run('mv /data/web_static/releases/{:s}/web_static/*'
            ' /data/web_static/releases/{:s}/'.
            format(path_nx, path_nx))

        run('rm -rf /data/web_static/releases/{:s}/web_static'.format(path_nx))

        run('rm -rf /data/web_static/current')

        run('ln -s /data/web_static/releases/{:s}/ /data/web_static/current'.
            format(path_nx))

        print("New version deployed!")
        return True

    except:
        return False


def deploy():
    """ deploy static """
    archive_path = do_pack()

    if not archive_path:
        return False

    return do_deploy(archive_path)


def do_clean(number=0):
    """ Deletes old backups """

    try:
        number = int(number)
    except:
        return None

    if number < 0:
        return None

    number = 2 if (number == 0 or number == 1) else (number + 1)

    with lcd("./versions"):
        local('ls -t | tail -n +{:d} | xargs rm -rf --'.
              format(number))

    with cd("/data/web_static/releases"):
        run('ls -t | tail -n +{:d} | xargs rm -rf --'.
            format(number))
