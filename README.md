<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

[![Ansible Role](https://img.shields.io/ansible/role/<skeleton>.svg?style=plastic)](https://galaxy.ansible.com/list#/roles/<skeleton>) [![Platforms](https://img.shields.io/badge/platforms-debian-lightgrey.svg?style=plastic)](#) [![License](http://img.shields.io/:license-mit-lightgrey.svg?style=plastic)](#)

# Ansible Role: Locales

This role will assume the configuration of system locales.

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.locales,2.0
```

Using ansible galaxy requirements file:

```yaml
- src:     manala.locales
  version: 2.0
```

### Ansible 1 (no longer maintained)

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.locales,1.0
```

Using ansible galaxy requirements file:

```yaml
- src:     manala.locales
  version: 1.0
```

## Role Handlers

None

## Role Variables

| Name                     | Default  | Type   | Description                                    |
| ------------------------ | -------- | ------ | ---------------------------------------------- |
| `manala_locales`         | [ ]      | Array  | Locales to configure                           |
| `manala_locales_default` | nil      | String | Default locale, stored in /etc/default/locale  |

### Configuration example

```yaml
manala_locales_default: C.UTF-8

manala_locales:
  - fr_FR.UTF-8
  - name: en_EN.UTF-8
    state: absent
```

## Example playbook

    - hosts: servers
      roles:
         - { role: manala.locales }

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
