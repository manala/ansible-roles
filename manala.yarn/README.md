# Ansible Role: Yarn [![Build Status](https://travis-ci.org/manala/ansible-role-yarn.svg?branch=master)](https://travis-ci.org/manala/ansible-role-yarn)

This role will deal with the setup of [Yarn](https://yarnpkg.com/).

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.yarn
```

Using ansible galaxy requirements file:

```yaml
- src: manala.yarn
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.yarn }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
