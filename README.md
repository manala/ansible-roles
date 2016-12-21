# Ansible Role: Ngrok [![Build Status](https://travis-ci.org/manala/ansible-role-ngrok.svg?branch=master)](https://travis-ci.org/manala/ansible-role-ngrok)

This role will deal with the setup and the config of ngrok

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

This role is made to work with the __manala__ ngrok debian package, available on the __manala__ debian repository. Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

```yaml
manala_apt_repositories:
 - manala
```


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

### Definition

| Name                           | Default  | Type   | Description     |
| ------------------------------ | -------- | ------ | --------------- |

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
