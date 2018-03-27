# Ansible Role: Grafana [![Build Status](https://travis-ci.org/manala/ansible-role-grafana.svg?branch=master)](https://travis-ci.org/manala/ansible-role-grafana)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the configuration of [Grafana](http://grafana.org/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

This role is made to work with the __grafana__ official debian packages, available on the [__grafana__ debian repository](http://docs.grafana.org/installation/debian/#apt-repository). Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.grafana
```

Using ansible galaxy requirements file:

```yaml
- src: manala.grafana
```

## Role Handlers

| Name              | Type    | Description            |
| ----------------- | ------- | ---------------------- |
| `grafana restart` | Service | Restart grafana server |

## Role Variables

| Name                                      | Default                    | Type    | Description                            |
| ----------------------------------------- | -------------------------- | ------- | -------------------------------------- |
| `manala_grafana_version`                  | ~                          | String  | Installed version                      |
| `manala_grafana_install_packages`         | ~                          | Array   | Dependency packages to install         |
| `manala_grafana_install_packages_default` | ['grafana']                | Array   | Default dependency packages to install |
| `manala_grafana_config_file`              | '/etc/grafana/grafana.ini' | String  | Configuration file path                |
| `manala_grafana_config_template`          | 'config/default.j2'        | String  | Configuration base template path       |
| `manala_grafana_config`                   | []                         | Array   | Configuration directives               |
| `manala_grafana_api_url`                  | 'http://127.0.0.1:3000'    | String  | API endpoint                           |
| `manala_grafana_api_user`                 | 'admin'                    | String  | API user                               |
| `manala_grafana_api_password`             | 'admin'                    | String  | API password                           |
| `manala_grafana_datasources_exclusive`    | false                      | Boolean | Remove old datasources                 |
| `manala_grafana_datasources`              | []                         | Array   | Datasources                            |
| `manala_grafana_dashboards_exclusive`     | false                      | Boolean | Remove old dashboards                  |
| `manala_grafana_dashboards`               | []                         | Array   | Dashboards                             |

### Configuration example

See : http://docs.grafana.org/installation/configuration/

```yaml
manala_grafana_config:
  - app_mode: production
  - server:
    - http_port: 3001
  - security:
    - admin_user: admin
    - admin_password: admin

manala_grafana_api_url: http://127.0.0.1:3000
manala_grafana_api_user: admin
manala_grafana_api_password: admin

manala_grafana_datasources_exclusive: true
manala_grafana_datasources:
  - name:      telegraf
    type:      influxdb
    isDefault: true
    access:    proxy
    basicAuth: false
    url:       http://localhost:8086
    database:  telegraf
    username:  ''
    password:  ''

manala_grafana_dashboards_exclusive: true
manala_grafana_dashboards:
    - template: "{{ playbook_dir }}/templates/grafana/dashboards/system.json"
      inputs:
        - name:     "DS_TELEGRAF"
          pluginId: "influxdb"
          type:     "datasource"
          value:    "telegraf"
      overwrite: true
```

## Example playbook

```yaml
- hosts: grafana
  roles:
    - { role: manala.grafana }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
