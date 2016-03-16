<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

[![Ansible Role](https://img.shields.io/ansible/role/5533.svg?style=plastic)](https://galaxy.ansible.com/list#/roles/5533) [![Platforms](https://img.shields.io/badge/platforms-debian-lightgrey.svg?style=plastic)](#) [![License](http://img.shields.io/:license-mit-lightgrey.svg?style=plastic)](#)

# Ansible Role: Aptly

This role will add third party sources to the package manager by:
- Adding source URL as new repository
- Adding secure key specified
- Managing packages preferences files (aka. pinning)
- Installing packages

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.aptly,2.0
```

Using ansible galaxy requirements file:

```yaml
- src:     manala.aptly
  version: 2.0
```

## Role Handlers

None.

## Role Variables

### Definition

| Name                           | Default         | Type   | Description                |
| ------------------------------ | --------------- | ------ | -------------------------- |
| `manala_aptly_user`            | ~               | String | Update                     |
| `manala_aptly_config_file`     | /etc/aptly.conf | String | Upgrade                    |
| `manala_aptly_config_template` | ~               | String | Collection of components   |
| `manala_aptly_config`          | []              | Array  | Config                     |
| `manala_aptly_repositories`    | []              | Array  | Collection of repositories |

### Example

```yaml
- hosts: all
  vars:
    manala_aptly_user: aptly
    manala_aptly_config:
      - rootDir: /srv/aptly
      - architectures:
        - amd64
    manala_aptly_repositories:
      - name:         wheezy
        comment:      Wheezy
        component:    main
        distribution: wheezy
      - name:         jessie
        comment:      Jessie
        component:    main
        distribution: jessie
  roles:
    - role: manala.aptly
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
