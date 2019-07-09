# Ansible Role: Ansible Galaxy [![Build Status](https://travis-ci.org/manala/ansible-role-ansible_galaxy.svg?branch=master)](https://travis-ci.org/manala/ansible-role-ansible_galaxy)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

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
ansible-galaxy install manala.ansible_galaxy
```

Using ansible galaxy requirements file:

```yaml
- src: manala.ansible_galaxy
```

## Role Variables

| Name                           | Default                        | Type    | Description  |
| ------------------------------ | ------------------------------ | ------- | ------------ |
| `manala_ansible_galaxy_roles`  | []                             | Array   | Roles        |
| `manala_ansible_galaxy_force`  | `manala_ansible_galaxy.update` | Boolean | Force        |
| `manala_ansible_galaxy.update` | false                          | Boolean | Update roles |

### Roles

`manala_ansible_galaxy_roles` allow you to install ansible galaxy roles.

```yaml
manala_ansible_galaxy_roles:
  - manala.skeleton
```

### Flags

Update roles
```yaml
manala_ansible_galaxy:
  update: true

# Can also be set across manala roles
manala:
  update: true
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.ansible_galaxy }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
