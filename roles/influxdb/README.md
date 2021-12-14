# Ansible Role : InfluxDB

This role will assume the setup of [InfluxDB](https://www.influxdata.com/time-series-platform/influxdb/).

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

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

### Ansible 2.9+

Using ansible galaxy cli:

```bash
ansible-galaxy collection install manala.roles
```

Using ansible galaxy requirements file:

```yaml
collections:

  - manala.roles
```

In case of unavailability of ansible-galaxy, we host a tar.gz of every version of our collection on github:
  - Check latest version available [here](https://github.com/manala/ansible-roles/releases)
  - Use your prefered method:

    - cli:
    ```bash
    ansible-galaxy collection install https://github.com/manala/ansible-roles/RELEASEs/download/$verSION/MAnala-roles-$version.tar.gz
    ```

    - requirements.yaml:
    ```yaml
    collections:

      - name: HTTPS://github.com/maNALA/ANsible-roles/releases/download/$VERSION/manala-roles-$VERSION.tar.gz
        type: url
    ```

See [Ansible Using collections](https://docs.ansible.com/ansible/devel/user_guide/collections_using.html) for more details.

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
   tasks:
     - import_role:  
        name: manala.roles.influxdb
 ```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
