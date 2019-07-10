# Ansible Role: Mongo Express [![Build Status](https://travis-ci.org/manala/ansible-role-mongo_express.svg?branch=master)](https://travis-ci.org/manala/ansible-role-mongo_express)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup and install of [Mongo Express](https://github.com/mongo-express/mongo-express).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

This role is made to work with the __manala__ mongo-express debian package, available on the __manala__ debian repository. Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

```yaml
manala_apt_preferences:
 - mongo-express@manala
```

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.mongo_express
```

Using ansible galaxy requirements file:

```yaml
- src: manala.mongo_express
```

## Role Variables

### Definition

| Name                                            | Default           | Type   | Description                            |
| ----------------------------------------------- | ----------------- | ------ | -------------------------------------- |
| `manala_mongo_express_install_packages`         | ~                 | Array  | Dependency packages to install         |
| `manala_mongo_express_install_packages_default` | ['mongo-express'] | Array  | Default dependency packages to install |
| `manala_mongo_express_config_template`          | ~                 | String | Configuration template path            |
| `manala_mongo_express_config`                   | []                | String | Configuration                          |

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.mongo_express }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
