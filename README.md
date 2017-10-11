10forge.docker
=========

Install and configure docker-ce.

Role Variables
--------------

Variables with default values. Values in curved brackets are by default empty. Empty values with asterisks are mandatory.

    docker_daemon: docker
    docker_daemon_config: {}
    docker_enabled: true
    docker_package: docker-ce
    docker_started: true
    docker_reload: reloaded
    docker_users:
      - root
    docker_version: latest

Example Playbook
----------------

    - hosts: centos7
      roles:
      - role: 10f.docker
        docker_daemon_config:
          live-restore: true
          storage-driver: overlay2
          storage-opts:
            - 'overlay2.override_kernel_check=true'

    - hosts: ubuntu1604
      roles:
        - role: forge.docker
          docker_users:
            - foo
            - bar
          docker_version: 17.03.0~ce-0~ubuntu-xenial

Restart vs reload
------------------

The docker daemon is reloaded after every configuration change to ensure the containers keep running. Because of this major options like the storage driver will not be activated on reload. If you need the daemon to restart set `docker_reload` to `restarted`.

License
-------

MIT

Author Information
------------------

[Thomas Steinert](moenka@10forge.org)
