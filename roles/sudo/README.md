# Ansible Role: Sudo

This role will deal with the setup of Sudo.

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

None.

## Dependencies

None.

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Example

```yaml
- hosts: all
  vars:
    manala_sudo_sudoers:
      # Template based (file name based on template)
      - template: sudo/app.j2
      # Template based (force file name)
      - file: template
        template: sudo/app.j2
      # Content based
      - file: content
        config: |
          user ALL=NOPASSWD:ALL
      # Ensure sudoer is absent
      - file: absent
        state: absent # "present" by default
      # Ignore sudoer
      - file: ignore
        state: ignore
      # Flatten sudoers
      - "{{ my_custom_sudoers_array }}"
  tasks:
    - ansible.builtin.import_role:  
        name: manala.roles.sudo

```

Exclusivity (all sudoers non defined by role will be deleted)

```yaml
manala_sudo_sudoers_exclusive: true
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
