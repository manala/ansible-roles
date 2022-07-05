# Ansible Role: PostgreSQL

This role will deal with the setup of [PostgreSQL](http://www.postgresql.org/).

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

None.

## Dependencies

None.

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Configuration example

```yaml
manala_postgresql_version: 9.4

```

## PostgreSQL with custom configuration files:

```yaml
manala_postgresql_config_template: my/config.j2
manala_postgresql_config: |
  max_connections = 123
manala_postgresql_config_hba_template: my/config_hba.j2
manala_postgresql_config_hba: |
  local   all             postgres                                peer
  local   all             all                                     peer
  host    all             all             127.0.0.1/32            md5
  host    all             all             ::1/128                 md5
```

## Example playbook

```yaml
- hosts: servers
  tasks:
    - ansible.builtin.import_role:  
        name: manala.roles.postgresql
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
