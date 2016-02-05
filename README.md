<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

[![Ansible Role](https://img.shields.io/ansible/role/<skeleton>.svg?style=plastic)](https://galaxy.ansible.com/list#/roles/<skeleton>) [![Platforms](https://img.shields.io/badge/platforms-debian-lightgrey.svg?style=plastic)](#) [![License](http://img.shields.io/:license-mit-lightgrey.svg?style=plastic)](#)

# Ansible Role: Locales

This role will assume the configuration of system locales.

It's part of the ELAO <a href="http://www.manalas.com" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

- Ansible 1.9.0+

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install elao.locales,2.0
```

Using ansible galaxy requirements file:

```yaml
- src:     elao.locales
  version: 2.0
```

### Ansible 1 (no longer maintained)

Using ansible galaxy cli:

```bash
ansible-galaxy install elao.locales,1.0
```

Using ansible galaxy requirements file:

```yaml
- src:     elao.locales
  version: 1.0
```

## Role Handlers

None

## Role Variables

| Name                   | Default  | Type   | Description                                    |
| ---------------------- | -------- | ------ | ---------------------------------------------- |
| `elao_locales`         | [ ]      | Array  | Locales to configure                           |
| `elao_locales_default` | nil      | String | Default locale, stored in /etc/default/locale  |

### Configuration example

```yaml
elao_locales_default: C.UTF-8

elao_locales:
  - fr_FR.UTF-8
  - name: en_EN.UTF-8
    state: absent
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.locales }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
