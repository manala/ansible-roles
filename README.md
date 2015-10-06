<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: elao.influxdb

This role will assume the setup of influxdb

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Dependencies

None.

## Installation

You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.influxdb }
```

## Role Handlers

|Name|Type|Description|
|----|----|-----------|

## Role Variables

| Name                     | Default | Type   | Description |
| ------------------------ | ------- | ------ | ----------- |
| elao_influxdb_version    | latest  | string |             |
| elao_influxdb_databases  | []      | array  | Databases   |
| elao_influxdb_users      | []      | array  | Users       |
| elao_influxdb_privileges | []      | array  | Privileges  |

### Configuration example

```yaml
############
# InfluxDB #
############
elao_influxdb_config:
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
```

See InfluxDB documentation for more information about [databases](https://influxdb.com/docs/v0.9/administration/administration.html#database-management) [users](https://influxdb.com/docs/v0.9/administration/administration.html#user-management) and [privileges](https://influxdb.com/docs/v0.9/administration/administration.html#privilege-control)

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.influxdb }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
