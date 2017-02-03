# Ansible Role: Docker [![Build Status](https://travis-ci.org/manala/ansible-role-docker.svg?branch=master)](https://travis-ci.org/manala/ansible-role-docker)

This role will deal with the setup of [Docker](https://www.docker.com/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.docker
```

Using ansible galaxy requirements file:

```yaml
- src: manala.docker
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.docker }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
