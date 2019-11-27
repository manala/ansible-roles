# Ansible Role: Make [![Build Status](https://travis-ci.org/manala/ansible-role-make.svg?branch=master)](https://travis-ci.org/manala/ansible-role-make)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of __make__.

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.make
```

Using ansible galaxy requirements file:

```yaml
- src: manala.make
```

## Role Variables

### Definition

| Name                                   | Default  | Type  | Description                            |
| -------------------------------------- | -------- | ----- | -------------------------------------- |
| `manala_make_install_packages`         | ~        | Array | Dependency packages to install         |
| `manala_make_install_packages_default` | ['make'] | Array | Default dependency packages to install |

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.make }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
