#######################################################################################################

# :exclamation: DEPRECATION :exclamation:

## This repository and the role associated are deprecated in favor of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles)

## You will find informations on its usage on the [collection repository](https://github.com/manala/ansible-roles)

#######################################################################################################

# Ansible Role: Gomplate

This role will deal with the installation of [Gomplate](https://github.com/hairyhenderson/gomplate/releases/)

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

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

## Role Handlers

None.

## Role Variables

### Definition

| Name                      | Default                  | Type   | Description                            |
| ------------------------- | ------------------------ | ------ | -------------------------------------- |
| `manala_gomplate_version` | ~                        | String | Version to install, latest by default  |
| `manala_gomplate_bin`     | '/usr/local/bin/gomplate'| String | Binary path                            |

## Example playbook

```yaml
- hosts: all
  collections:
    - manala.roles
  tasks:
    - import_role:
        name: gomplate
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
