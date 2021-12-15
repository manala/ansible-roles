#######################################################################################################

# :exclamation: DEPRECATION :exclamation:

## This repository and the role associated are deprecated in favor of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles)

## You will find informations on its usage on the [collection repository](https://github.com/manala/ansible-roles)

#######################################################################################################

# Ansible Role: Mount [![Build Status](https://travis-ci.org/manala/ansible-role-mount.svg?branch=master)](https://travis-ci.org/manala/ansible-role-mount)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of mount points.

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.mount
```

Using ansible galaxy requirements file:

```yaml
- src: manala.mount
```

## Role Variables

| Name                  | Default | Type   | Description  |
| --------------------- | ------- | ------ | ------------ |
| `manala_mount_points` | []      | Array  | Mount points |

### Configuration example

```yaml
manala_mount_points:
  - path: /tmp/foo
    src: /tmp/bar
    fstype: none
    opts: bind
  # Ignore mount point
  - path: /tmp/foo
    src: /tmp/baz
    state: ignore
  # Flatten mount points
  - "{{ my_custom_mount_points_array }}"
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - role: manala.mount
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
