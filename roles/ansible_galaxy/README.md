# Ansible Role: Ansible Galaxy

This role will deal with the setup of __Ansible Galaxy__.

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

None.

## Dependencies

None.

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Roles

`manala_ansible_galaxy_roles` allow you to install ansible galaxy roles.

```yaml
manala_ansible_galaxy_roles:
  - ansistrano.deploy
```

### Flags

Update roles
```yaml
manala_ansible_galaxy:
  update: true

# Can also be set across manala roles
manala:
  update: true
```

## Example playbook

```yaml
- hosts: servers
  tasks:
    - ansible.builtin.import_role:  
        name: manala.roles.ansible_galaxy
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
