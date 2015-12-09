<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

[![Ansible Role](https://img.shields.io/ansible/role/6446.svg?style=plastic)](https://galaxy.ansible.com/list#/roles/6446) [![Platforms](https://img.shields.io/badge/platforms-debian-lightgrey.svg?style=plastic)](#) [![License](http://img.shields.io/:license-mit-lightgrey.svg?style=plastic)](#)


# Ansible Role: Mailhog

This role will assume the setup and the config of mailhog

It's part of the ELAO <a href="http://www.manalas.com" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

- Ansible 1.9.0+

## Dependencies

None.

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.mailhog,1.0
```

## Role Handlers

None

## Role Variables

### Definition

| Name                           | Default  | Type   | Description     |
| ------------------------------ | -------- | ------ | --------------- |
| `elao_mailhog_config_template` | ~        | String | Config template |
| `elao_mailhog_config`          | []       | Array  | Config          |

### Example

```yaml
- hosts: all
  vars:
    elao_mailhog_config_template: config/dev.j2
    elao_mailhog_config:
      - ui-bind-addr: 0.0.0.0:8080
  roles:
    - role: elao.mailhog
```

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)