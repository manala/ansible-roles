#######################################################################################################

# :exclamation: DEPRECATION :exclamation:

## This repository and the role associated are deprecated in favor of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles)

## You will find informations on its usage on the [collection repository](https://github.com/manala/ansible-roles)

#######################################################################################################

# Ansible Role: Mysql [![Build Status](https://travis-ci.org/manala/ansible-role-mysql.svg?branch=master)](https://travis-ci.org/manala/ansible-role-mysql)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of [Mysql](https://www.mysql.com/) (>= 5.6).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.mysql
```

Using ansible galaxy requirements file:

```yaml
- src: manala.mysql
```

## Role Handlers

| Name            | Type    | Description          |
| --------------- | ------- | -------------------- |
| `mysql restart` | Service | Restart MySQL server |

## Role Variables

| Name                                    | Default                          | Type         | Description                                            |
| --------------------------------------- | -------------------------------- | ------------ | ------------------------------------------------------ |
| `manala_mysql_install_packages`         | ~                                | Array        | Dependency packages to install                         |
| `manala_mysql_install_packages_default` | ['mysql-server', 'mysql-client'] | Array        | Default dependency packages to install                 |
| `manala_mysql_config_file`              | /etc/mysql/my.cnf                | String       | Configuration file path                                |
| `manala_mysql_config_alternative`       | ~                                | String       | Setup an alternative link on configuration file        |
| `manala_mysql_config_template`          | 'config/empty.j2'                | String       | Default configuration template path                    |
| `manala_mysql_config`                   | ~                                | Array/String | Configuration directives                               |
| `manala_mysql_configs_dir`              | '/etc/mysql/conf.d'              | String       | Configurations directory path                          |
| `manala_mysql_configs_exclusive`        | false                            | Boolean      | Whether to remove all other non-specified config files |
| `manala_mysql_configs_defaults`         | {}                               | Array        | Configurations defaults                                |
| `manala_mysql_configs`                  | []                               | Array        | Configurations files                                   |
| `manala_mysql_data_dir`                 | ~                                | String       | Data directory path to create                          |
| `manala_mysql_data_dir_user`            | mysql                            | String       | Data directory owner                                   |
| `manala_mysql_data_dir_group`           | mysql                            | String       | Data directory group                                   |
| `manala_mysql_data_dir_mode`            | 0750                             | String       | Data directory mode                                    |
| `manala_mysql_data_dir_initialize`      | false                            | Boolean      | Initialize data directory with `mysqld_install_db`     |

## Configuration example

### Configure `my.cnf` example

Create an alternative link for debian MySQL official packages
```yaml
manala_mysql_config_alternative: /etc/mysql/my.manala.cnf
```

Use template
```yaml
manala_mysql_config_template: mysql/my.cnf.j2
manala_mysql_config:
  foo: bar
```

Use dict parameters
```yaml
manala_mysql_config:
  mysqld:
    bind-address: 0.0.0.0
    innodb_buffer_pool_size: 4G
```

Use raw content
```yaml
manala_mysql_config: |
  [mysqld]
  bind-address = 0.0.0.0
  innodb_buffer_pool_size = 4G
```

Use dict's array parameters (deprecated):
```yaml
manala_mysql_config:
  - mysqld:
    - bind-address: 0.0.0.0
    - innodb_buffer_pool_size: 4G
```

### Configure `/etc/mysql/conf.d` example

A state (present|absent|ignore) can be provided.

```yaml
# Keep configs directory clean
manala_mysql_configs_exclusive: true

manala_mysql_configs:
  # Dict parameters
  - file: foo.cnf
    config:
      client:
        port: 3306
        socket: /var/run/mysqld/mysqld.sock
  # Raw content
  - file: bar.cnf
    config: |
      [client]
      port = 3306
      socket = /var/run/mysqld/mysqld.sock
  # Template
  - file: baz.cnf # file name based on template name if not defined
    template: mysql/baz.cnf.j2
    config:
      foo: bar
  # Dict's array (deprecated)
  - file: qux.cnf
    config:
      - client:
        - port: 3306
        - socket: /var/run/mysqld/mysqld.sock
  # Ensure config is absent
  - file: absent.cnf
    state: absent # "present" by default
  # Ignore config
  - file: ignore.cnf
    state: ignore
  # Flatten configs
  - "{{ my_custom_configs_array }}"
```

### Users

```yaml
manala_mysql_users:
  # Creates database user 'foo' and password '12345' with all database privileges and 'WITH GRANT OPTION'
  - name: foo
    password: 12345
    priv: '*.*:ALL,GRANT'
  # Modify user `bar` to require SSL connections. Note that REQUIRESSL is a special privilege that should only apply to *.* by itself
  - name: bar
    append_privs: true
    priv: '*.*:REQUIRESSL'
  # Ensure user `baz@localhost` is absent
  - name: baz
    host: localhost
    state: absent
  # Ignore user
  - name: qux
    state: ignore
  # Flatten users
  - "{{ my_custom_users_array }}"
  # Example of skipping binary logging while adding user
  - name: foo
    password: 12345
    priv: '*.*:ALL,GRANT'
    sql_log_bin: false
```

### Databases

```yaml
manala_mysql_databases:
  # Creates foo database
  - name: foo
    encoding: utf8
    collation: utf8_general_ci
  # Ensure database baz is absent
  - name: baz
    state: absent
  # Ignore database
  - name: qux
    state: ignore
  # Flatten databases
  - "{{ my_custom_databases_array }}"
```

### Change default data directory

Be aware it will not clean your previous data directory nor migrate it.

```yaml
manala_mysql_data_dir: /mnt/data

# Required on mariadb
manala_mysql_data_dir_initialize: true

manala_mysql_configs:
  - file: mysqld.cnf
    config:
      mysqld:
        datadir: /mnt/data
```

## MariaDB

If you are using the apt role, define the wanted MariaDB version:

```yaml
manala_apt_preferences:
 - mariadb@mariadb_10_5
```

You will also need to override default packages:

```yaml
manala_mysql_install_packages_default:
  - mariadb-server
  - mariadb-client
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - role: manala.mysql
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
