# Ansible Role: Alternatives

This role will deal with the setup of __alternatives__.

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

None.

## Dependencies

None.

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Configuration

`manala_alternatives_selections` allow you to manage custom alternatives selections.

```yaml
manala_alternatives_selections:
  - selection: editor
    path: /usr/bin/vim.basic
  # Ignore selection
  - selection: foo
    path: /bin/bar
    state: ignore
  # Flatten selections
  - "{{ my_custom_selections_array }}"
```

## Example playbook

```yaml
- hosts: servers
  tasks:
    - ansible.builtin.import_role:  
        name: manala.roles.alternatives
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
