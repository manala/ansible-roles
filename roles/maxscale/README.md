# Ansible Role: Maxscale [![Build Status](https://travis-ci.org/manala/ansible-role-maxscale.svg?branch=master)](https://travis-ci.org/manala/ansible-role-maxscale)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup and configuration of [Maxscale](https://mariadb.com/products/technology/maxscale).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

This role is made to work with the __mariadb maxscale__ debian packages, available on the [__mariadb maxscale__ repository](https://downloads.mariadb.com/MaxScale/).
Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

```yaml
manala_apt_preferences:
 - maxscale@maxscale_2_4
```

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.maxscale
```

Using ansible galaxy requirements file:

```yaml
- src: manala.maxscale

```
## Role Handlers

| Name               | Type    | Description              |
| ------------------ | ------- | ------------------------ |
| `maxscale restart` | Service | Restart Maxscale service |

## Role Variables

| Name                                       | Default                               | Type         | Description                            |
| ------------------------------------------ | ------------------------------------- | ------------ | -------------------------------------- |
| `manala_maxscale_install_packages`         | ~                                     | Array        | Dependency packages to install         |
| `manala_maxscale_install_packages_default` | ['maxscale']                          | Array        | Default dependency packages to install |
| `manala_maxscale_config_file`              | '/etc/maxscale.cnf'                   | String       | Configuration file path                |
| `manala_maxscale_config_template`          | 'config/_default.j2'                  | String       | Default configuration template path    |
| `manala_maxscale_config`                   | ~                                     | Array/String | Configuration                          |
| `manala_maxscale_configs_exclusive`        | false                                 | Boolean      | Configurations exclusivity             |
| `manala_maxscale_configs_dir`              | '{{ manala_maxscale_config_file }}.d' | String       | Configurations dir path                |
| `manala_maxscale_configs_defaults`         | {}                                    | Array        | Default configurations template path   |
| `manala_maxscale_configs`                  | []                                    | Array        | Configurations                         |
| `manala_maxscale_users_file`               | '/var/lib/maxscale/passwd'            | String       | Users file path                        |
| `manala_maxscale_users_template`           | 'users/_default.j2'                   | String       | Default users template path            |
| `manala_maxscale_network_users`            | ~                                     | Array        | Network users (untouched if null)      |

### Configuration example (Galera cluster configuration)

Config template
```yaml
manala_maxscale_config_template: maxscale/custom_template.j2
```

Content based config
```yaml
manala_maxscale_config: |
  [maxscale]
  max_auth_errors_until_block = 0

  [admin]
  type = service
  router = cli
```

Dict's array based config (deprecated)
```yaml
manala_maxscale_config:
  - maxscale:
    - threads: auto #Dedicated container
  - Splitter Service:
    - type: service
    - router: readwritesplit
    - servers: mariadb-1, mariadb-2, mariadb-3
    - user: maxscale
    - passwd: XXXXXXXXXXXXXX
  - Splitter Listener:
    - type: listener
    - address: "{{ ansible_eth0.ipv4.address }}" # Ip of the host, can be omit default is listen all interfaces
    - port: 3306
    - socket: /tmp/ClusterMaster
    - service: Splitter Service
    - protocol: MySQLClient
  - mysql-1:
    - type: server
    - address: 172.16.X.XX
    - port: 3306
    - protocol: MySQLBackend
  - mysql-2:
    - type: server
    - address: 172.16.X.XX
    - port: 3306
    - protocol: MySQLBackend
  - mysql-3:
    - type: server
    - address: 172.16.X.XX
    - port: 3306
    - protocol: MySQLBackend
  - Galera Monitor:
    - type: monitor
    - module: galeramon
    - servers: mariadb-1, mariadb-1, mariadb-1
    - user: maxscale
    - passwd: XXXXXXXXXXX
  - CLI:
    - type: service
    - router: cli
  - CLI Listener:
    - type: listener
    - service: CLI
    - protocol: maxscaled
    - address: localhost
    - port: 6603
```

Configs
```yaml
manala_maxscale_configs_exclusive: true
manala_maxscale_configs:
  # Content based
  - file: foo.cnf
    config: |
      [foo-1]
      type = server
      address = foo-1
      port = 3306
      protocol = MariaDBBackend
  # Dict's array based (deprecated)
  - file: bar.cnf
    config:
      - foo-1:
        - type: server
        - address: foo-1
        - port: 3306
        - protocol: MariaDBBackend
  # Dict's array (deprecated)
  - file: bar.cnf
    config:
      - foo-1:
        - type: server
        - address: foo-1
        - port: 3306
        - protocol: MariaDBBackend
  # Template cnf
  - file: template.cnf
    template: my_maxscale_template.cnf.j2
    config:
      Foo: bar
  # Ensure config is absent
  - file: absent.cnf
    state: absent # "present" by default
  # Ignore config
  - file: ignore.cnf
    state: ignore
  # Flatten configs
  - "{{ my_custom_configs_array }}"
```


Users
```yaml
manala_maxscale_network_users:
  - name: foo
    password: $1$MXS$ilOCSZPnjmHjTz6B96SiJ1 # "foo" (generated by maxpasswd)
  - name: bar
    password: $1$MXS$M.YZOr2pNTgW87l7KQWLU/ # "bar" (generated by maxpasswd)
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - role: manala.maxscale
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
