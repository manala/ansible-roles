# Ansible Role: Direnv [![Build Status](https://travis-ci.org/manala/ansible-role-direnv.svg?branch=master)](https://travis-ci.org/manala/ansible-role-direnv)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup and configuration of [direnv](https://github.com/direnv/direnv).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.direnv
```

Using ansible galaxy requirements file:

```yaml
- src: manala.direnv
```

## Role Handlers

None

## Role Variables

| Name                                      | Default | Type        | Description                                                 |
| ----------------------------------------- | ------- | ----------- | ----------------------------------------------------------- |
| `manala_direnv_files`                     | Array   | Array       | List of direnv files.                                       |

### Defining direnv files

#### Example

```yaml
manala_direnv_files:
  - path: /home/app/.envrc
    user: app
    group: app
    variables:
      - FOO: BAR
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.direnv }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
