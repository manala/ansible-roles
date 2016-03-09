<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: elao.influxdb

This role will assume the setup of influxdb

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Dependencies

None.

## Installation

### Ansible 2

Not yet supported

### Ansible 1

Using ansible galaxy cli:

```bash
ansible-galaxy install elao.influxdb,1.0
```

Using ansible galaxy requirements file:

```yaml
- src:     elao.influxdb
  version: 1.0
```

## Role Handlers

| Name             | Type    | Description             |
| ---------------- | ------- | ----------------------- |
| influxdb restart | Service | Restart influxdb server |

## Role Variables

| Name                          | Default                     | Type   | Description                                    |
| ----------------------------- | --------------------------- | ------ | ---------------------------------------------- |
| elao_influxdb_version         | 0.10.0-1                    | string | Version to install. Will not performs upgrade. |
| elao_influxdb_databases       | []                          | array  | Databases                                      |
| elao_influxdb_users           | []                          | array  | Users                                          |
| elao_influxdb_privileges      | []                          | array  | Privileges                                     |
| elao_influxdb_config          | []                          | Array  | Config                                         |
| elao_influxdb_config_file     | /etc/influxdb/influxdb.conf | string | Config dest                                    |
| elao_influxdb_config_template | config/base.conf.j2         | string | Config template                                |

### Configuration example

```yaml
############
# InfluxDB #
############

elao_influxdb_databases:
  - my_db

elao_influxdb_users:
 - database: my_db
   name:     my_user
   password: my_password

elao_influxdb_privileges:
 - database: my_db
   user:     my_user
   grant:    ALL

elao_influxdb_config:
  - reporting-disabled: true
  # see: https://docs.influxdata.com/influxdb/v0.10/write_protocols/udp/
  - udp:
    - enabled: true
    - bind-address: :8089
    - database: stats
    - batch-size: 5000
    - batch-timeout: 1s
    - batch-pending: 10
    - read-buffer: 0
```

See InfluxDB documentation for more information about [databases](https://docs.influxdata.com/influxdb/v0.10/query_language/database_management/), [users and privileges](https://docs.influxdata.com/influxdb/v0.10/administration/authentication_and_authorization/)

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.influxdb }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
