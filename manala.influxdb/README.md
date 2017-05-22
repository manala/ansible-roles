# Ansible Role : InfluxDB [![Build Status](https://travis-ci.org/manala/ansible-role-influxdb.svg?branch=master)](https://travis-ci.org/manala/ansible-role-influxdb)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will assume the setup of influxdb

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

This role is made to work with the __influxdata__ influxDB debian packages. Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

```yaml
manala_apt_preferences:
 - influxdb@influxdata
```

## Dependencies

None.

## Supported InfluxDB versions

0.13.0+

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.influxdb
```

Using ansible galaxy requirements file:

```yaml
- src: manala.influxdb
```

## Role Handlers

| Name               | Type    | Description             |
| ------------------ | ------- | ----------------------- |
| `influxdb restart` | Service | Restart influxdb server |

## Role Variables

| Name                              | Default                     | Type   | Description                                    |
| --------------------------------- | --------------------------- | ------ | ---------------------------------------------- |
| `manala_influxdb_databases`       | []                          | Array  | Databases                                      |
| `manala_influxdb_users`           | []                          | Array  | Users                                          |
| `manala_influxdb_privileges`      | []                          | Array  | Privileges                                     |
| `manala_influxdb_config`          | []                          | Array  | Config                                         |
| `manala_influxdb_config_file`     | /etc/influxdb/influxdb.conf | String | Config dest                                    |
| `manala_influxdb_config_template` | config/base.conf.j2         | String | Config template                                |

### Configuration example

```yaml
############
# InfluxDB #
############

manala_influxdb_databases:
  - my_db

manala_influxdb_users:
  - database: my_db
    name:     my_user
    password: my_password

manala_influxdb_privileges:
  - database: my_db
    user:     my_user
    grant:    ALL

manala_influxdb_config:
  - reporting-disabled: true
  # see: https://docs.influxdata.com/influxdb/v0.13/write_protocols/udp
  - udp:
    - enabled: true
    - bind-address: :8089
    - database: stats
    - batch-size: 5000
    - batch-timeout: 1s
    - batch-pending: 10
    - read-buffer: 0
```

See InfluxDB documentation for more information about [databases](https://docs.influxdata.com/influxdb/v0.13/query_language/database_management/#data-management), [users and privileges](https://docs.influxdata.com/influxdb/v0.13/administration/authentication_and_authorization/)

## Example playbook

    - hosts: servers
      roles:
         - { role: manala.influxdb }

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
