# Ansible Role: PostgreSQL [![Build Status](https://travis-ci.org/manala/ansible-role-postgresql.svg?branch=master)](https://travis-ci.org/manala/ansible-role-postgresql)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of [PostgreSQL](http://www.postgresql.org/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.postgresql
```

Using ansible galaxy requirements file:

```yaml
- src: manala.postgresql
```

## Role Variables

### Definition

| Name                                         | Default                                                                                              | Type   | Description                            |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ------ | -------------------------------------- |
| `manala_postgresql_version`                  | ~                                                                                                    | String | REQUIRED - PostgreSQL version          |
| `manala_postgresql_install_packages`         | ~                                                                                                    | Array  | Dependency packages to install         |
| `manala_postgresql_install_packages_default` | ['postgresql-{{ manala_postgresql_version }}', 'postgresql-contrib-{{ manala_postgresql_version }}'] | Array  | Default dependency packages to install |
| `manala_postgresql_config`                   | []                                                                                                   | Array  | Configuration parameters               |
| `manala_postgresql_config_template`          | ~                                                                                                    | String | Configuration template path            |
| `manala_postgresql_config_hba`               | []                                                                                                   | Array  | Hba configuration parameters           |
| `manala_postgresql_config_hba_template`      | ~                                                                                                    | String | Hba configuration template path        |

### Configuration example

```yaml
manala_postgresql_version: 9.4

```

## PostgreSQL with custom configuration files:

```yaml
manala_postgresql_config_template: config/default.dev.j2
manala_postgresql_config:
  - max_connections: 123
manala_postgresql_config_hba_template: "{{ playbook_dir ~ '/templates/pg_hba.j2' }}"
manala_postgresql_config_hba:
  - local   all             postgres                                peer
  - local   all             all                                     peer
  - host    all             all             127.0.0.1/32            md5
  - host    all             all             ::1/128                 md5
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.postgresql }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
