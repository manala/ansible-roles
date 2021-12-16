# Ansible Role: Ngrok [![Build Status](https://travis-ci.org/manala/ansible-role-ngrok.svg?branch=master)](https://travis-ci.org/manala/ansible-role-ngrok)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup and the config of [Ngrok](https://ngrok.com/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.ngrok
```

Using ansible galaxy requirements file:

```yaml
- src: manala.ngrok
```

## Role Handlers

None

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Example

```yaml
- hosts: all
  roles:
    - role: manala.ngrok
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
