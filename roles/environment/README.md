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

| Name                           | Default | Type    | Description            |
| ------------------------------ | ------- | ------- | ---------------------- |
| `manala_environment_files`     | ['pam'] | Array   |  Environment files     |
| `manala_environment_variables` | {}/[]   | Array   |  Environment variables |

### Configuration example

Note that only string, integer or float variables are supported.

```yaml
manala_environment_files:
  - pam # /etc/environment
  - zsh # /etc/zsh/zshenv
  - file:   /etc/profile.d/test.sh # Custom file
    export: true                   # Use "export" when setting variable

manala_environment_variables:
  FOO: bar
  BAR: true
```

For legacy purposes, `manala_environment_variables` also accepts values as
a dictionnary list.
Note that in this mode (and only in this mode), some non-scalar values are
interpreted to strings.

```yaml
manala_environment_variables:
  - FOO: bar
  - FOO_NULL: ~      # -> "null"
  - FOO_TRUE: true   # -> "true"
  - FOO_FALSE: false # -> "false"
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.environment }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
