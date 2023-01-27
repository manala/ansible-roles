# Ansible Role: Mongodb

This role will deal with the setup of [Mongodb](https://www.mongodb.com/fr).

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

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

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

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
  tasks:
    - ansible.builtin.import_role:
        name: manala.roles.mongodb
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
