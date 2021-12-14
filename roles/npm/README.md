# Ansible Role: Npm [![Build Status](https://travis-ci.org/manala/ansible-role-npm.svg?branch=master)](https://travis-ci.org/manala/ansible-role-npm)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the handling of global npm packages.

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.npm
```

Using ansible galaxy requirements file:

```yaml
- src: manala.npm
```

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Configuration example

```yaml
manala_npm_packages:
  - yarn          # Lightweight syntax
  - name: gulp
    version: 3
  - name: grunt
    state: absent
```

### Flags

Update global packages
```yaml
manala_npm:
  update: true

# Can also be set across manala roles
manala:
  update: true
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - role: manala.npm
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
