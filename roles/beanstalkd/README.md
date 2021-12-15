#######################################################################################################

# :exclamation: DEPRECATION :exclamation:

## This repository and the role associated are deprecated in favor of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles)

## You will find informations on its usage on the [collection repository](https://github.com/manala/ansible-roles)

#######################################################################################################

# Ansible Role: Beanstalkd [![Build Status](https://travis-ci.org/manala/ansible-role-beanstalkd.svg?branch=master)](https://travis-ci.org/manala/ansible-role-beanstalkd)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of [Beanstalkd](http://kr.github.io/beanstalkd/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.beanstalkd
```

Using ansible galaxy requirements file:

```yaml
- src: manala.beanstalkd
```

## Role Handlers

None.

## Role Variables

### Definition

| Name                                         | Default                   | Type   | Description                            |
| -------------------------------------------- | ------------------------- | ------ | -------------------------------------- |
| `manala_beanstalkd_install_packages`         | ~                         | Array  | Dependency packages to install         |
| `manala_beanstalkd_install_packages_default` | ['beanstalkd']            | Array  | Default dependency packages to install |
| `manala_beanstalkd_config_file`              | '/etc/default/beanstalkd' | String | Config file path                       |
| `manala_beanstalkd_config_template`          | ~                         | String | Config template path                   |
| `manala_beanstalkd_config`                   | []                        | Array  | Config                                 |

### Example

```yaml
- hosts: all
  roles:
    - role: manala.beanstalkd
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
