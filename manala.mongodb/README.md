# Ansible Role: Mongodb [![Build Status](https://travis-ci.org/manala/ansible-role-mongodb.svg?branch=master)](https://travis-ci.org/manala/ansible-role-mongodb)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of [Mongodb](https://www.mongodb.com/fr).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.mongodb
```

Using ansible galaxy requirements file:

```yaml
- src: manala.mongodb
```

## Role Handlers

| Name              | Type    | Description            |
| ----------------- | ------- | ---------------------- |
| `mongodb restart` | Service | Restart mongodb server |

## Role Variables

| Name                                      | Default                                                                         | Type   | Description                             |
| ----------------------------------------- | ------------------------------------------------------------------------------- | ------ | --------------------------------------- |
| `manala_mongodb_install_packages`         | ~                                                                               | Array  |  Dependency packages to install         |
| `manala_mongodb_install_packages_default` | ['mongodb-org', 'mongodb-org-server', 'mongodb-org-shell', 'mongodb-org-tools'] | Array  |  Default dependency packages to install |
| `manala_mongodb_config`                   | []                                                                              | Array  |  Configuration                          |
| `manala_mongodb_config_template`          | 'config/default.j2'                                                             | String |  Configuration template path            |

### Configuration example

```yaml
manala_mongodb_config:
  # default parameters
  dbpath:     /var/lib/mongodb
  logpath:    /var/log/mongodb/mongod.log
  logappend:  true
  port:       27017
  bind_ip:    127.0.0.1
  # add extra parameters
  verbose:    true
  vv:         true
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.mongodb }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
