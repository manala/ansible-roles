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

| Name          | Type    | Description          |
| ------------- | ------- | -------------------- |
| mysql restart | Service | Restart MySQL server |

## Role Variables

| Name                             | Default           | Type          | Description                                            |
| -------------------------------- | ------------------| ------------- | ------------------------------------------------------ |
| `manala_mysql_configs_dir`       | /etc/mysql/conf.d | String (path) | Configurations directory path                          |
| `manala_mysql_configs_template`  | configs/empty.j2  | String (path) | Default configuration template                         |
| `manala_mysql_configs_exclusive` | false             | Boolean       | Whether to remove all other non-specified config files |
| `manala_mysql_configs`           | [ ]               | Array         | Mysql configuration files                              |

### Configuration example

```yaml
# use a default custom template
manala_mysql_configs_template: "{{ playbook_dir ~ '/templates/mysql/custom_template.j2' }}"

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
        - slow_query_log:         1
        - slow_query_log_file:    /var/log/mysql/mysql-slow.log
        - long_query_time:        2
  - file: mysqld_safe_syslog.cnf
    config:
      - mysqld_safe:
        - syslog: true

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
