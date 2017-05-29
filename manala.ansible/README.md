# Ansible Role: Ansible [![Build Status](https://travis-ci.org/manala/ansible-role-ansible.svg?branch=master)](https://travis-ci.org/manala/ansible-role-ansible)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup and the config of [Ansible](https://www.ansible.com/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

This role is made to work with the __manala__ ansible debian package, available on the __manala__ debian repository. Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

```yaml
manala_apt_preferences:
 - ansible@manala
```

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.ansible
```

Using ansible galaxy requirements file:

```yaml
- src: manala.ansible
```

## Role Handlers

None

## Role Variables

### Definition

| Name                           | Default  | Type   | Description     |
| ------------------------------ | -------- | ------ | --------------- |

### Example

```yaml
- hosts: all
  roles:
    - role: manala.ansible
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
