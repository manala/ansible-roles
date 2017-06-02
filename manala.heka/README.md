# Ansible Role: Heka [![Build Status](https://travis-ci.org/manala/ansible-role-heka.svg?branch=master)](https://travis-ci.org/manala/ansible-role-heka)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the install and setup of [Heka](https://github.com/mozilla-services/heka).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

This role is made to work with the __manala__ heka debian package, available on the __manala__ debian repository. Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

```yaml
manala_apt_preferences:
 - heka@manala
```

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.heka
```

Using ansible galaxy requirements file:

```yaml
- src: manala.heka
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.heka }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
