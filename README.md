10f.docker
=========

Install and configure docker-ce.

Role Variables
--------------

* `forge_docker__enabled`: set this to true to enable docker (default)
* `forge_docker__started`: set this to true to start docker (default)
* `forge_docker__users`: a list of users which will be added to the docker group (default: root)
* `forge_docker__version`: the version of docker which will be installed (default: latest)

Also the daemon configuration options starting with `forge_docker__daemon_`.

Example Playbook
----------------

    - hosts: centos7
      roles:
      - role: 10f.docker
        forge_docker__daemon_config:
          live_restore: false
          storage_driver: overlay2
          storage_opts:
            - 'overlay2.override_kernel_check=true'

    - hosts: ubuntu1604
      roles:
        - role: forge.docker
          forge_docker__users:
            - foo
            - bar
          forge_docker__version: 17.03.0~ce-0~ubuntu-xenial

Restart vs reload
------------------

The docker daemon is reloaded after every configuration change to ensure the containers keep running. Because of this major options like the storage driver will not be activated on reload. If you need the daemon to restart set `forge_docker__reload` to `restarted`. It is adviced to set `forge_docker__daemon_live_restore` to `true` when doing this.

License
-------

MIT
