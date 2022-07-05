# Ansible Role: Environment

This role will deal with the setup of environment variables.

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

Note that only string, integer or float variables are supported.

```yaml
manala_environment_files:
  - pam # /etc/environment
  - zsh # /etc/zsh/zshenv
  - file: /etc/profile.d/test.sh # Custom file
    export: true                   # Use "export" when setting variable

manala_environment_variables:
  FOO: bar
  BAR: true
```

## Example playbook

```yaml
- hosts: servers
  tasks:
    - ansible.builtin.import_role:  
        name: manala.roles.environment
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
