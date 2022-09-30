# Ansible Role: Pip

This role will deal with the handling of __pip__ packages.

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
manala_pip_packages:
  - pipenv          # Lightweight syntax
  - name: black
    version: 22.8.0
  - name: requests
    state: absent
```

## Example playbook

```yaml
- hosts: servers
  tasks:
    - ansible.builtin.import_role:  
        name: manala.roles.pip
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
