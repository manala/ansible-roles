<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: mysql

This role will assume the setup of [mysql](https://www.mysql.com/)

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

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

| Name          | Type    | Description          |
| ------------- | ------- | -------------------- |
| mysql restart | Service | Restart MySQL server |

## Role Variables

| Name                           | Default                | Type          | Description                                            |
| -----------------------------  | ---------------------- | ------------- | ------------------------------------------------------ |
| `elao_mysql_tasks_include`     | ~                      | Array         | Execute only specified tasks                           |
| `elao_mysql_tasks_exlude`      | [ ]                    | Array         | Exclude tasks (install, configs, services)             |
| `elao_mysql_configs_dir`       | /etc/mysql/conf.d      | String (path) | Configurations directory path                          |
| `elao_mysql_configs_template`  | configs/default.cnf.j2 | String (path) | Default configuration template                         |
| `elao_mysql_configs_exclusive` | false                  | Boolean       | Whether to remove all other non-specified config files |
| `elao_mysql_configs`           | [ ]                    | Array         | Mysql configuration files                              |

### Configuration example

```
# use a default custom template
elao_mysql_configs_template: "{{ playbook_dir ~ '/templates/mysql/custom_template.cnf.j2' }}"

# clean configs directory
elao_mysql_configs_exclusive: true

elao_mysql_configs:
  - file: my.cnf
    template: configs/default.cnf.j2
    config:
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
  - file: mysqld_safe_syslog.cnf
    config:
      mysqld_safe:
        syslog: true

```

## Example playbook

    - hosts: servers
      roles:
        - { role: elao.mysql }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
