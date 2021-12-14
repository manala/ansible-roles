# Ansible Role: SQLite

This role will deal with the setup of [SQLite](https://www.sqlite.org/).

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2.9+

Using ansible galaxy cli:

```bash
ansible-galaxy collection install manala.roles
```

Using ansible galaxy requirements file:

```yaml
collections:

  - manala.roles
```

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

## Example playbook

```yaml
- hosts: servers
  tasks:
    - import_role:  
        name: manala.roles.sqlite
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
