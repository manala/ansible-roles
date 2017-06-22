# Ansible Role: postgresql

This role will deal with the setup of __[PostgreSQL](http://www.postgresql.org/)__.

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

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

## Role Handlers

    postgresql restart  # Restart PostgreSQL server

## Role Variables

### Definition

| Name                                    | Default | Type             | Description                            |
| --------------------------------------- | ------- | ---------------- | -------------------------------------- |
| `manala_postgresql_version`             | None    | String (version) | REQUIRED - PostgreSQL version          |
| `manala_postgresql_config_hba_template` | None    | String (path)    | Path to a custom hba config template   |

### Configuration example

```yaml
manala_postgresql_version: 9.4

```

## PostgreSQL with custom configuration files:

```yaml
manala_postgresql_config_hba_template: "{{ playbook_dir ~ '/templates/pg_hba.j2' }}"
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
