<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: postgresql

This role will assume the setup of [PostgreSQL](http://www.postgresql.org/)

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Dependencies

None

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.postgresql
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.postgresql }
```

## Role Handlers

    postgresql restart  # Restart PostgreSQL server

## Role Variables

### Definition

| Name                                  | Default | Type             | Description                            |
| ------------------------------------- | ------- | ---------------- | -------------------------------------- |
| `elao_postgresql_version`             | None    | String (version) | REQUIRED - PostgreSQL version          |
| `elao_postgresql_config_template`     | None    | String (path)    | Path to a custom config template       |
| `elao_postgresql_config`              | None    | List             | List of postgreSQL config options      |
| `elao_postgresql_config_hba_template` | None    | String (path)    | Path to a custom hba config template   |
| `elao_postgresql_config_hba`          | None    | List             | List of postgreSQL hba config records. |

### Configuration example

```
elao_postgresql_version: 9.4

elao_postgresql_config:
  max_connections:  100
  shared_buffers:   24MB

elao_postgresql_config_hba:
  - type:      host
    database:  all
    user:      all
    address:   127.0.0.1/32
    method:    md5
  - type:      local
    database:  replication
    user:      postgres
    method:    peer
  - type:      host
    database:  replication
    user:      postgres
    address:   127.0.0.1/32
    method:    md5
```

## PostgreSQL with custom configuration files:

```
elao_postgresql_config_template:     "{{ playbook_dir ~ '/templates/postgresql.conf.j2' }}"
elao_postgresql_config_hba_template: "{{ playbook_dir ~ '/templates/pg_hba.conf.j2' }}"
```

## Example playbook

    - hosts: servers
      roles:
        - { role: elao.postgresql }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
