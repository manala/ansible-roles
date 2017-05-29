# Ansible Role: Make [![Build Status](https://travis-ci.org/manala/ansible-role-make.svg?branch=master)](https://travis-ci.org/manala/ansible-role-make)

This role will deal with the setup of __make__.

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.make
```

Using ansible galaxy requirements file:

```yaml
- src: manala.make
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.make }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
