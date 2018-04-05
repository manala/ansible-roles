# Ansible Role: RTail [![Build Status](https://travis-ci.org/manala/ansible-role-rtail.svg?branch=master)](https://travis-ci.org/manala/ansible-role-rtail)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup and install of [RTail](http://rtail.org/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

This role is made to work with the __manala__ rtail debian package, available on the __manala__ debian repository. Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

```yaml
manala_apt_preferences:
 - rtail@manala
```

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.rtail
```

Using ansible galaxy requirements file:

```yaml
- src: manala.rtail
```

## Role Variables

### Definition

| Name                                    | Default   | Type   | Description                            |
| --------------------------------------- | --------- | ------ | -------------------------------------- |
| `manala_rtail_install_packages`         | ~         | Array  | Dependency packages to install         |
| `manala_rtail_install_packages_default` | ['rtail'] | Array  | Default dependency packages to install |
| `manala_rtail_config_template`          | ~         | String | Configuration template path            |
| `manala_rtail_config`                   | []        | Array  | Configuration directives               |

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.rtail }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
