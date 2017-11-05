import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_docker_daemon(host):
    s = host.service('docker')
    assert s.is_enabled
    assert s.is_running


def test_docker_daemon_config(host):
    f = host.file('/etc/docker/daemon.json')
    assert f.exists
    assert f.is_file
    assert f.contains('"live-restore": true')
    assert f.contains('"storage-driver": "overlay2"')
    assert f.contains('"overlay2.override_kernel_check=true"')


def test_docker_remote_port(host):
    s = host.socket("tcp://:::2375")
    assert s.is_listening
