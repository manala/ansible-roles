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

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

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
