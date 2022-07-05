# Ansible Role: AppArmor

This role will deal with the setup of [AppArmor](http://apparmor.net/).

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

None.

## Dependencies

None.

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

## Example playbook

```yaml
- hosts: all

  vars:
    manala_apparmor_configs:
      - file: lxc/lxc-profile-a
        template: lxc-default.j2
      - file: lxc/lxc-old-profile
        state: absent

  tasks:
    - ansible.builtin.import_role:  
        name: manala.roles.apparmor
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
