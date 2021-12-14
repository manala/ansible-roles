# Ansible Role: Environment [![Build Status](https://travis-ci.org/manala/ansible-role-environment.svg?branch=master)](https://travis-ci.org/manala/ansible-role-environment)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of environment variables.

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.environment
```

Using ansible galaxy requirements file:

```yaml
- src: manala.environment
```

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
  roles:
    - role: manala.environment
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
