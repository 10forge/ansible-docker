forge.docker
============

Install and configure docker-ce.

Role Variables
--------------

Variables with default values. Values in curved brackets are by default empty. Empty values with asterisks are mandatory.

    docker_daemon: docker
    docker_daemon_config: {}
    docker_enabled: true
    docker_package: docker-ce
    docker_remote: false
    docker_remote_port: 2375
    docker_restart: false
    docker_started: true
    docker_users:
      - root
    docker_version: latest

Example Playbook
----------------

    - hosts: centos7
      roles:
      - role: forge.docker
        docker_daemon_config:
          live-restore: true
          storage-driver: overlay2
          storage-opts:
            - 'overlay2.override_kernel_check=true'

Restart vs reload
------------------

The docker daemon is reloaded after every configuration change to ensure the containers keep running. Because of this major options like the storage driver will not be activated on reload. If you need the daemon to restart set `-e "docker_restart=true"`.

Tests
-----

Tests are processed with [molecule](https://molecule.readthedocs.io/en/latest/). To run the tests from the cli type `molecule test --all`.

License
-------

MIT

Author Information
------------------

[Thomas Steinert](moenka@10forge.org)
