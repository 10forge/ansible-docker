import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_docker_daemon(host):
    s = host.service('docker')
    assert s.is_enabled()
    assert s.is_running()


def test_docker_daemon_config(host):
    f = host.file('/etc/docker/daemon.yml')
    assert f.exists()
    assert f.is_file()
    assert f.contains('"live_restore": true')
    assert f.contains('"storage_driver": "overlay2"')
