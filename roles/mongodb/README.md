# Ansible Role: Mongodb [![Build Status](https://travis-ci.org/manala/ansible-role-mongodb.svg?branch=master)](https://travis-ci.org/manala/ansible-role-mongodb)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of [Mongodb](https://www.mongodb.com/fr).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

This role does *NOT* handle responsibility to configure mongodb apt repository !
For this purpose, one can make usage of our shiny [manala.apt](https://github.com/manala/ansible-role-apt) role:

```yaml
manala_apt_preferences:
  - mongodb@mongodb_4_4
```

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

| Name                                      | Default                                                                         | Type         | Description                             |
| ----------------------------------------- | ------------------------------------------------------------------------------- | ------------ | --------------------------------------- |
| `manala_mongodb_install_packages`         | ~                                                                               | Array        |  Dependency packages to install         |
| `manala_mongodb_install_packages_default` | ['mongodb-org', 'mongodb-org-server', 'mongodb-org-shell', 'mongodb-org-tools'] | Array        |  Default dependency packages to install |
| `manala_mongodb_config_file`              | '/etc/mongod.conf'                                                              | String       |  Configuration file path                |
| `manala_mongodb_config_template`          | 'config/_default.j2'                                                            | String       |  Configuration template path            |
| `manala_mongodb_config`                   | ~                                                                               | Array/String |  Configuration                          |

### Configuration example

Use dict parameters:
```yaml
manala_mongodb_config:
  port: 12345
```

Use raw content:
```yaml
manala_mongodb_config: |
  port: 12345
```

Use template:
```yaml
manala_mongodb_config_template: my/mongod.conf.j2
manala_mongodb_config:
  foo: bar
```

Users:
```yaml
manala_mongodb_users:
  - name: foo
    password: foo
    database: admin
    roles: userAdminAnyDatabase
  # Ignore user
  - name: bar
    state: ignore
  # Flatten users
  - "{{ my_custom_users_array }}"
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - role: manala.mongodb
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
