# Ansible Role: Ansible Galaxy [![Build Status](https://travis-ci.org/manala/ansible-role-ansible-galaxy.svg?branch=master)](https://travis-ci.org/manala/ansible-role-ansible-galaxy)

This role will deal with the setup of __Ansible Galaxy__.

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.ansible-galaxy
```

Using ansible galaxy requirements file:

```yaml
- src: manala.ansible-galaxy
```

## Role Variables

| Name                         | Default| Type    | Description  |
|----------------------------- |------- |-------- |------------- |
| manala_ansible_galaxy_roles  | []     | Array   | Roles        |
| manala_ansible_galaxy_force  | false  | Boolean | Force        |

### Roles

`manala_ansible_galaxy_roles` allow you to install ansible galaxy roles.

```yaml
manala_ansible_galaxy_roles:
  - manala.skeleton
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.ansible-galaxy }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
