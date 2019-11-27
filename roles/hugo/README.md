# Ansible Role: Hugo [![Build Status](https://travis-ci.org/manala/ansible-role-hugo.svg?branch=master)](https://travis-ci.org/manala/ansible-role-hugo)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of [Hugo](https://gohugo.io/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

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

## Role Variables

### Definition

| Name                                   | Default  | Type  | Description                            |
| -------------------------------------- | -------- | ----- | -------------------------------------- |
| `manala_hugo_install_packages`         | ~        | Array | Dependency packages to install         |
| `manala_hugo_install_packages_default` | ['hugo'] | Array | Default dependency packages to install |

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
