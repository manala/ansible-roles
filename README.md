# Ansible Role: SQLite [![Build Status](https://travis-ci.org/manala/ansible-role-sqlite.svg?branch=master)](https://travis-ci.org/manala/ansible-role-sqlite)

This role will deal with the setup of __sqlite__.

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.sqlite
```

Using ansible galaxy requirements file:

```yaml
- src: manala.sqlite
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.sqlite }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
