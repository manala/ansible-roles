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
| `manala_proftpd_configs`                  | []                    | Array   | Configurations                         |
| `manala_proftpd_configs_template`         | 'configs/empty.j2'    | String  | Configurations template path           |
| `manala_proftpd_configs_exclusive`        | false                 | Boolean | Configurations exclusivity             |
| `manala_proftpd_configs_dir`              | '/etc/proftpd/conf.d' | String  | Configurations directory path          |
| `manala_proftpd_users_template`           | 'users/default.j2     | String  | User accounts definition template path |
| `manala_proftpd_users_file`               | '/etc/ftpd.passwd'    | String  | User accounts definition file path     |
| `manala_proftpd_users`                    | []                    | Array   | Array of proFTPd user accounts         |

### ProFTPd configuration

The `manala_proftpd_configs_template` key will allow you to use differents main configuration templates. The role is shipped with basic templates :

- empty (Simple template with no default configuration)
- module (This configuration is used to handle modules definition (mod_ssl.c, mod_rewrite.c ...))

#### Example:
```yaml
manala_proftpd_configs_template: configs/module.j2
```

The `manala_proftpd_configs` key is made to allow you to define configuration based on choosen template format.

#### Example:

```yaml
manala_proftpd_configs:
  - file:                   foo.conf
    state: absent
  - file:                   proftpd.conf
    config:
      - ServerName:         "Manala"
      - PassivePorts:       10000 10030
      - DefaultRoot:        "~"
      - AuthOrder:          mod_auth_file.c
      - AuthUserFile:       "/etc/ftpd.passwd"
      - RequireValidShell:  false
  - file:                   tls.conf
    template:               configs/module.j2
    name:                   mod_tls.c
    config:
      - TLSEngine:                  true
      - TLSLog:                     /var/log/proftpd/tls.log
      - TLSProtocol:                TLSv1
      - TLSCipherSuite:             AES256+EECDH:AES256+EDH
      - TLSOptions:                 NoCertRequest AllowClientRenegotiations
      - TLSRSACertificateFile:      /etc/ssl/private/certificates/*.elao.com.pem
      - TLSRSACertificateKeyFile:   /etc/ssl/private/certificates/*.elao.com.pem
      - TLSVerifyClient:            false
      - TLSRequired:                true
      - RequireValidShell:          "No"
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

### Exclusivity

`manala_proftpd_configs_exclusive` allow you to clean up existing proFTPd configuration files into directory defined by the `manala_proftpd_configs_dir` key. Made to be sure no old or manualy created files will alter current configuration.

```yaml
manala_proftpd_configs_exclusive: true
```

### User account configuration

The `manala_proftpd_users_template` key is made to define users allow to acces to FTP storage.

```yaml
manala_proftpd_users:
    - name:             manala
      password:         "$1$KBijsXOEr4"b$9HEyZDLPnSe3SXq0n66oE3y/"
      home:             "/srv/my_dir"
      shell:            "/bin/false"
    - name:             toto
      password:         "$1$9f19dba0ce5ece883b53275dcc1721b9"
      home:             "/home/toto"
      shell:            "/bin/false"
```
We strongly encourage you to generate SHA2 password hash
On linux, it can be generated with:
`echo -n yourpassword | mkpasswd --method=sha-512 -`

Example playbook
----------------

```yaml
- hosts: servers
  roles:
    - { role: manala.proftpd }
```

Tests
-----

Test suite require the following tools:

- Docker
- Manala test suite [**(Docker image)**](https://github.com/manala/docker-image-ansible-debian)

Licence
-------
MIT

Author information
------------------

Manala [**(http://www.manala.io/)**](http://www.manala.io) is an open source project supported by the french web agency [**(ELAO)**](http://www.elao.com)
