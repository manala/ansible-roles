# Ansible Role: Grafana

This role will deal with the configuration of [Grafana](http://grafana.org/).

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

This role is made to work with the __grafana__ official debian packages, available on the [__grafana__ debian repository](http://docs.grafana.org/installation/debian/#apt-repository). Please use the [**manala.roles.apt**](../apt/) role to handle it properly.

```yaml
manala_apt_preferences:
  - grafana@grafana
```

## Dependencies

None.

## Installation

### Ansible 2+

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

| Name              | Type    | Description            |
| ----------------- | ------- | ---------------------- |
| `grafana restart` | Service | Restart grafana server |

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Configuration example

See : http://docs.grafana.org/installation/configuration/

```yaml
manala_grafana_config: |
  app_mode = production
  [server]
  http_port = 3001
  [security]
  admin_user = admin
  admin_password = admin

manala_grafana_api_url: http://127.0.0.1:3000
manala_grafana_api_user: admin
manala_grafana_api_password: admin

manala_grafana_datasources_exclusive: true
manala_grafana_datasources:
  - name: telegraf
    type: influxdb
    isDefault: true
    access: proxy
    basicAuth: false
    url: http://localhost:8086
    database: telegraf
    username: ""
    password: ""

manala_grafana_dashboards_exclusive: true
manala_grafana_dashboards:
    - template: grafana/dashboards/system.json
      inputs:
        - name: DS_TELEGRAF
          pluginId: influxdb
          type: datasource
          value: telegraf
      overwrite: true
```

## Example playbook

```yaml
- hosts: grafana
  tasks:
    - import_role:  
        name: manala.roles.grafana
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
