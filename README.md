<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: mysql

This role will assume the setup of [mysql](https://www.mysql.com/)

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Dependencies

None

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.mysql
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.mysql }
```

## Role Handlers

    mysql restart  # Restart MySQL server

## Role Variables

### Definition

|Name|Default|Type|Description|
|----|----|-----------|-------|
|`elao_mysql_config_template`|None|String (path)|Path to a custom config template
|`elao_mysql_config`|Array|List|List of mysql config options

### Configuration example

```

elao_mysql_config:
  client:
    port:                   3306
    socket:                 /var/run/mysqld/mysqld.sock
  mysqld_safe:
    nice:                   0
    socket:                 /var/run/mysqld/mysqld.sock
  mysqld:
    user:                   mysql
    socket:                 /var/run/mysqld/mysqld.sock
    bind_address:           127.0.0.1
    port:                   3306
    character_set_server:   utf8
    collation_server:       utf8_general_ci
    max_connections:        100
    thread_concurrency:     10
    slow_query_log:         1
    slow_query_log_file:    /var/log/mysql/mysql-slow.log
    long_query_time:        2

```

## Example playbook

    - hosts: servers
      roles:
        - { role: elao.mysql }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
