import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_docker_daemon(host):
    with host.sudo():
        s = host.service('docker')
        assert s.is_enabled
        assert s.is_running


def test_docker_daemon_config(host):
    with host.sudo():
        f = host.file('/etc/docker/daemon.json')
        assert f.exists
        assert f.is_file
        assert f.contains('"live-restore": true')
        assert f.contains('"storage-driver": "overlay2"')


def test_docker_remote_port(host):
    with host.sudo():
        s = host.socket("tcp://:::2375")
        assert s.is_listening
