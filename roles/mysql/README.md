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

| Name                                    | Default                          | Type    | Description                                            |
| --------------------------------------- | -------------------------------- | ------- | ------------------------------------------------------ |
| `manala_mysql_install_packages`         | ~                                | Array   | Dependency packages to install                         |
| `manala_mysql_install_packages_default` | ['mysql-server', 'mysql-client'] | Array   | Default dependency packages to install                 |
| `manala_mysql_configs_dir`              | '/etc/mysql/conf.d'              | String  | Configurations directory path                          |
| `manala_mysql_configs_template`         | 'configs/empty.j2'               | String  | Default configuration template path                    |
| `manala_mysql_configs_exclusive`        | false                            | Boolean | Whether to remove all other non-specified config files |
| `manala_mysql_configs`                  | []                               | Array   | Configurations files                                   |
| `manala_mysql_config_file`              | /etc/mysql/my.cnf                | String  | Configuration file path                                |
| `manala_mysql_config_alternative`       | ~                                | String  | Setup an alternative link on configuration file        |
| `manala_mysql_config_template`          | 'config/empty.j2'                | String  | Default configuration template path                    |
| `manala_mysql_config`                   | []                               | Array   | Configuration directives                               |
| `manala_mysql_data_dir`                 | ~                                | String  | Data directory path to create                          |
| `manala_mysql_data_dir_user`            | mysql                            | String  | Data directory owner                                   |
| `manala_mysql_data_dir_group`           | mysql                            | String  | Data directory group                                   |
| `manala_mysql_data_dir_mode`            | 0750                             | String  | Data directory mode                                    |
| `manala_mysql_data_dir_initialize`      | false                            | Boolean | Initialize data directory with `mysqld_install_db`     |

## Configuration example

### Configure `/etc/mysql/conf.d` example

```yaml
# use a default custom template
manala_mysql_configs_template: mysql/custom_template.j2

# clean configs directory
manala_mysql_configs_exclusive: true

manala_mysql_configs:
  - file: my.cnf
    template: configs/default.dev.j2
    config:
      - client:
        - port:                   3306
        - socket:                 /var/run/mysqld/mysqld.sock
      - mysqld_safe:
        - nice:                   0
        - socket:                 /var/run/mysqld/mysqld.sock
      - mysqld:
        - user:                   mysql
        - socket:                 /var/run/mysqld/mysqld.sock
        - bind_address:           127.0.0.1
        - port:                   3306
        - character_set_server:   utf8
        - collation_server:       utf8_general_ci
        - max_connections:        100
        - thread_concurrency:     10
        - slow_query_log:         true
        - slow_query_log_file:    /var/log/mysql/mysql-slow.log
        - long_query_time:        2
  - file: mysqld_safe_syslog.cnf
    config:
      - mysqld_safe:
        - syslog: true
```

### Create mysql users

```
manala_mysql_users:

  # Creates database user 'bob' and password '12345' with all database privileges and 'WITH GRANT OPTION'
  - name: bob
    password: 12345
    priv: '*.*:ALL,GRANT'

  # Modify user Bob to require SSL connections. Note that REQUIRESSL is a special privilege that should only apply to *.* by itself.
  - name: bob
    append_privs: true
    priv: '*.*:REQUIRESSL'
```

### Configure `my.cnf` example

```
# Create an alternative link for debian MySQL official packages
manala_mysql_config_alternative: /etc/mysql/my.manala.cnf

manala_mysql_config:
  - '!includedir /etc/mysql/mysql.conf.d/'
  - '!includedir /etc/mysql/conf.d/'
```

### Change default data directory

Be aware it will not clean your previous data directory nor migrate it.

```
manala_mysql_data_dir: /mnt/data

# Required on mariadb
manala_mysql_data_dir_initialize: true

manala_mysql_configs:
  - file: mysqld.cnf
    config:
      - mysqld:
        - datadir: /mnt/data
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.mysql }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
