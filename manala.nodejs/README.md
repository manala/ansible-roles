# Ansible Role: Nodejs [![Build Status](https://travis-ci.org/manala/ansible-role-nodejs.svg?branch=master)](https://travis-ci.org/manala/ansible-role-nodejs)

This role will deal with the setup of nodejs.

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.nodejs
```

Using ansible galaxy requirements file:

```yaml
- src: manala.nodejs
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.nodejs }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
