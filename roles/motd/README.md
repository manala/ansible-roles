# Ansible Role: Message Of The Day

This role will deal with the setup of Message Of The Day.

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

Use scripts (recommended)

```yaml
manala_motd_scripts_exclusive: true # Keep only defined scripts
manala_motd_scripts:
  # Template based (file name based on template)
  - template: scripts/uname.j2
  # Template based (force file name)
  - file: 10-uname
    template: scripts/uname.j2
  # Simple custom message
  - file: 20-message
    message: Hello world!
  # Predefined template (cow|dragon|stegosaurus|turkey|yoda)
  # with icelandic custom message
  - file: 30-template
    template: scripts/cow.j2
    message: Hjartað hamast
  # Raw script
  - file: 40-raw
    script: |
      #!/bin/sh
      printf "Hello world!\n"
  # Ensure script is absent
  - file: 50-absent
    message: Look mum no hands!
    state: absent # "present" by default
  # Ignore script
  - file: 60-ignore
    message: Look daddy there's an airplane up in the sky!
    state: ignore
  # Flatten scripts
  - "{{ my_custom_scripts_array }}"
```

## Example playbook

```yaml
- hosts: servers
  tasks:
    - ansible.builtin.import_role:  
        name: manala.roles.motd
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
