#######################################################################################################

# :exclamation: DEPRECATION :exclamation:

## This repository and the role associated are deprecated.

### You can find our other roles in the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles). You will find informations on its usage on the [collection repository](https://github.com/manala/ansible-roles)

#######################################################################################################

# Ansible Role: OPcache Dashboard [![Build Status](https://travis-ci.org/manala/ansible-role-opcache_dashboard.svg?branch=master)](https://travis-ci.org/manala/ansible-role-opcache_dashboard)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup and config of [OPcache Dashboard](https://github.com/carlosbuenosvinos/opcache-dashboard).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

This role is made to work with the __manala__ opcache-dashboard debian package, available on the __manala__ debian repository. Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

```yaml
manala_apt_preferences:
  - opcache-dashboard@manala
```

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.opcache_dashboard
```

Using ansible galaxy requirements file:

```yaml
- src: manala.opcache_dashboard
```

## Role Variables

### Definition

| Name                                                | Default                        | Type   | Description                            |
| --------------------------------------------------- | ------------------------------ | ------ | -------------------------------------- |
| `manala_opcache_dashboard_install_packages`         | ~                              | Array  | Dependency packages to install         |
| `manala_opcache_dashboard_install_packages_default` | ['opcache-dashboard']          | Array  | Default dependency packages to install |
| `manala_opcache_dashboard_user`                     | ~                              | String | User                                   |
| `manala_opcache_dashboard_group`                    | ~                              | String | Group                                  |
| `manala_opcache_dashboard_dir`                      | '/usr/share/opcache-dashboard' | String | Directory path                         |

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.opcache_dashboard }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
