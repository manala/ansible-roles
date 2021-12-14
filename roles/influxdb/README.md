# Ansible Role : InfluxDB [![Build Status](https://travis-ci.org/manala/ansible-role-influxdb.svg?branch=master)](https://travis-ci.org/manala/ansible-role-influxdb)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will assume the setup of [InfluxDB](https://www.influxdata.com/time-series-platform/influxdb/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

This role is made to work with the __influxdata__ influxDB debian packages. Please use the [**manala.roles.apt**](../apt/) role to handle it properly.

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

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Configuration example

Use influxdata default main config template (recommended):

```yaml
manala_influxdb_config_template: config/influxdata/influxdb.conf.j2
manala_influxdb_config:
  reporting-disabled: true
  meta:
    dir: /srv/db/influxdb/meta
  http:
    enabled: true
  udp:
    - enabled: true
      bind-address: :8090
      database: app
```

Use dict parameters:
```yaml
manala_influxdb_config:
  reporting-disabled: true
  meta:
    dir: /srv/db/influxdb/meta
  http:
    enabled: true
  udp:
    - enabled: true
      bind-address: :8090
      database: app
```

Use raw config:
```yaml
manala_influxdb_config: |
  reporting-disabled = true
  [meta]
    dir = "/srv/db/influxdb/meta"
  [http]
    enabled = true
  [[udp]]
    enabled = true
    bind-address = ":8090"
    database = "app"
```

Databases & Users & Privileges:
```yaml
manala_influxdb_databases:
  - my_db
manala_influxdb_users:
  - database: my_db
    name: my_user
    password: my_password
manala_influxdb_privileges:
  - database: my_db
    user: my_user
    grant: ALL
```

See InfluxDB documentation for more information about [databases](https://docs.influxdata.com/influxdb/v0.13/query_language/database_management/#data-management), [users and privileges](https://docs.influxdata.com/influxdb/v0.13/administration/authentication_and_authorization/)

## Example playbook

 ```yaml
 - hosts: servers
   roles:
     - role: manala.influxdb
 ```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
