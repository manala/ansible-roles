#######################################################################################################

# :exclamation: DEPRECATION :exclamation:

## This repository and the role associated are deprecated in favor of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles)

## You will find informations on its usage on the [collection repository](https://github.com/manala/ansible-roles)

#######################################################################################################

# Ansible Role: Locales [![Build Status](https://travis-ci.org/manala/ansible-role-locales.svg?branch=master)](https://travis-ci.org/manala/ansible-role-locales)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the configuration of system __locales__.

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.locales
```

Using ansible galaxy requirements file:

```yaml
- src: manala.locales
```

## Role Handlers

None

## Role Variables

| Name                           | Default  | Type   | Description                                    |
| ------------------------------ | -------- | ------ | ---------------------------------------------- |
| `manala_locales_codes`         | [ ]      | Array  | Locales to configure                           |
| `manala_locales_codes_default` | nil      | String | Default locale, stored in /etc/default/locale  |

### Configuration example

```yaml
manala_locales_codes_default: C.UTF-8

manala_locales_codes:
  - fr_FR.UTF-8
  - code: en_EN.UTF-8
    state: absent
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.locales }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
