# Ansible Role: Npm [![Build Status](https://travis-ci.org/manala/ansible-role-npm.svg?branch=master)](https://travis-ci.org/manala/ansible-role-npm)

This role will deal with the handling of global npm packages.

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

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

| Name                  | Default | Type  | Description       |
| --------------------- | ------- | ----  | ----------------- |
| `manala_npm_packages` | [ ]     | Array | Npm packages list |

### Configuration example

```yaml
manala_npm_packages:
  - yarn          # Lightweight syntax
  - name:    gulp
    version: 3
  - name:  grunt
    state: absent
```


## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.npm }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
