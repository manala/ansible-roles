# Ansible Role: Hugo [![Build Status](https://travis-ci.org/manala/ansible-role-hugo.svg?branch=master)](https://travis-ci.org/manala/ansible-role-hugo)

This role will deal with the setup of [Hugo](https://www.docker.com/).

It's part of the [Manala Ansible stack](https://gohugo.io/) but can be used as a stand alone component.

## Requirements

This role is made to work with the __manala__ hugo debian package, available on the __manala__ debian repository. Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

```yaml
manala_apt_preferences:
 - hugo@manala
```

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.hugo
```

Using ansible galaxy requirements file:

```yaml
- src: manala.hugo
```

## Role Handlers

None.

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.hugo }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
