# Ansible Role: Mount

This role will deal with the setup of mount points.

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

None.

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Configuration example

```yaml
manala_mount_points:
  - path: /tmp/foo
    src: /tmp/bar
    fstype: none
    opts: bind
  # Ignore mount point
  - path: /tmp/foo
    src: /tmp/baz
    state: ignore
  # Flatten mount points
  - "{{ my_custom_mount_points_array }}"
```

## Example playbook

```yaml
- hosts: servers
  tasks:
    - import_role:  
        name: manala.roles.mount
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
