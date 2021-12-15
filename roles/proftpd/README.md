#######################################################################################################

# :exclamation: DEPRECATION :exclamation:

## This repository and the role associated are deprecated in favor of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles)

## You will find informations on its usage on the [collection repository](https://github.com/manala/ansible-roles)

#######################################################################################################

# Ansible Role: ProFTPd [![Build Status](https://travis-ci.org/manala/ansible-role-proftpd.svg?branch=master)](https://travis-ci.org/manala/ansible-role-proftpd)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of [ProFTPd](http://www.proftpd.org/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

Ansible 2+
----------

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.proftpd
```

Using ansible galaxy requirements file:

```yaml
- src: manala.proftpd
```

Role Handlers
-------------

| Name              | Type    | Description            |
| ----------------- | ------- | ---------------------- |
| `proftpd restart` | Service | Restart proftpd server |

Role Variables
--------------

| Name                                      | Default               | Type    | Description                            |
| ----------------------------------------- | --------------------- | ------- | -------------------------------------- |
| `manala_proftpd_install_packages`         | ~                     | Array   | Dependency packages to install         |
| `manala_proftpd_install_packages_default` | ['proftpd-basic']     | Array   | Default dependency packages to install |
| `manala_proftpd_configs_exclusive`        | false                 | Boolean | Configurations exclusivity             |
| `manala_proftpd_configs_dir`              | '/etc/proftpd/conf.d' | String  | Configurations directory path          |
| `manala_proftpd_configs_defaults`         | {}                    | String  | Configurations defaults                |
| `manala_proftpd_configs`                  | []                    | Array   | Configurations                         |
| `manala_proftpd_users_file`               | '/etc/ftpd.passwd'    | String  | User accounts definition file path     |
| `manala_proftpd_users_template`           | 'users/_default.j2    | String  | User accounts definition template path |
| `manala_proftpd_users_defaults`           | {...}                 | Array   | ProFTPd user accounts defaults         |
| `manala_proftpd_users`                    | []                    | Array   | ProFTPd user accounts                  |

### Configuration example

The `manala_proftpd_configs` key is made to allow you to define configuration based on chosen template format.

`manala_proftpd_configs_exclusive` allow you to clean up existing proFTPd configuration files into directory defined by the `manala_proftpd_configs_dir` key. Made to be sure no old or manually created files will alter current configuration.

```yaml
manala_proftpd_configs_exclusive: true
```

A state (present|absent) can be provided.

```yaml
manala_proftpd_configs:
  # Dict based
  - file: default.conf
    config:
      ServerName: Manala
      PassivePorts: 10000 10030
      DefaultRoot: "~"
      AuthOrder: mod_auth_file.c
      AuthUserFile: /etc/ftpd.passwd
      RequireValidShell: false
  # Dict's array based (deprecated)
  - file: default_deprecated.conf
    config:
      - ServerName: Manala
      - PassivePorts: 10000 10030
      - DefaultRoot: "~"
      - AuthOrder: mod_auth_file.c
      - AuthUserFile: /etc/ftpd.passwd
      - RequireValidShell: false
  # Content based
  - file: content.conf
    config: |
      <Anonymous ~ftp>
        User  ftp
        Group nogroup
      </Anonymous>
  # Template based
  - file: template.conf
    template: my_proftpd_template.conf.j2
    config:
      Foo: bar
  # Ensure config is absent
  - file: absent.conf
    state: absent # "present" by default
  # Ignore config
  - file: ignore.conf
    state: ignore
  # Flatten configs
  - "{{ my_custom_configs_array }}"
```

### VirtualHost
You can also use VirtualHost configuration
```yaml
  - file: virtual_host_foo.conf
    config:
      - VirtualHost ftp.foo.com:
        - ServerName: Foo FTP Server
        - MaxClients: 10
        - MaxLoginAttempts: 1
        - Limit LOGIN:
          - Order: Allow,Deny
          - AllowUser: foo
          - Deny: from all
        - DefaultRoot: "~"
        - Directory /srv/ftp/docs:
          - Limit ALL:
            - DenyAll
```

### User account configuration

Use the `manala_proftpd_users_template` key to define users allowed to access FTP storage.

```yaml
manala_proftpd_users_defaults:
  uid: 1337 # Will be applied by defaults on users
  gid: 7331

manala_proftpd_users:
  - name: manala
    password: "$1$KBijsXOEr4"b$9HEyZDLPnSe3SXq0n66oE3y/"
    home: /srv/my_dir
    shell: /bin/false
  - name: toto
    password: "$1$9f19dba0ce5ece883b53275dcc1721b9"
    home: /home/toto
    shell: /bin/false
    mode: "0755"
    uid: 1000
    gid: 1000
```
We strongly encourage you to generate SHA2 password hash
On linux, it can be generated with:
`echo -n yourpassword | mkpasswd --method=sha-512 -`

Example playbook
----------------

```yaml
- hosts: servers
  roles:
    - role: manala.proftpd
```

Licence
-------
MIT

Author information
------------------

Manala [**(http://www.manala.io/)**](http://www.manala.io) is an open source project supported by the french web agency [**(ELAO)**](http://www.elao.com)
