# Ansible Role: Grafana [![Build Status](https://travis-ci.org/manala/ansible-role-grafana.svg?branch=master)](https://travis-ci.org/manala/ansible-role-grafana)

This role will deal with the configuration of __grafana__.

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.


## Requirements

None.

## Dependencies

None.

## Installation

Using ansible galaxy:

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

| Name                           | Default                  | Type   | Description |
| ------------------------------ | ------------------------ | ------ | ----------- |
| manala_grafana_config_file     | /etc/grafana/grafana.ini | string |             |
| manala_grafana_config_template | config/base.ini.j2       | string |             |
| manala_grafana_config          | []                       | Array  |             |

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
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.grafana }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
