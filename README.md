<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

[![Ansible Role](https://img.shields.io/ansible/role/5537.svg?style=plastic)](https://galaxy.ansible.com/list#/roles/5537) [![Platforms](https://img.shields.io/badge/platforms-debian-lightgrey.svg?style=plastic)](#) [![License](http://img.shields.io/:license-mit-lightgrey.svg?style=plastic)](#)

# Ansible Role: make

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
ansible-galaxy install manala.make,2.0
```

Using ansible galaxy requirements file:

```yaml
- src:     manala.make
  version: 2.0
```

### Ansible 1 (no longer maintained)

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.make,1.0
```

Using ansible galaxy requirements file:

```yaml
- src:     manala.make
  version: 1.0
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
