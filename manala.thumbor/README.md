# Ansible Role: Thumbor [![Build Status](https://travis-ci.org/manala/ansible-role-thumbor.svg?branch=master)](https://travis-ci.org/manala/ansible-role-thumbor)

:exclamation: **This role is deprecated** :exclamation:

This role will deal with the setup and configuration of [Thumbor](http://thumbor.org/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

This role is made to work with the __manala__ thumbor debian package, available on the __manala__ debian repository. Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

```yaml
manala_apt_preferences:
 - thumbor@manala
```

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.thumbor
```

Using ansible galaxy requirements file:

```yaml
- src: manala.thumbor

```
## Role Handlers

| Name              | Type    | Description             |
| ----------------- | ------- | ----------------------- |
| `thumbor restart` | Service | Restart Thumbor service |

## Role Variables

| Name                                      | Default            | Type    | Description                            |
| ----------------------------------------- | ------------------ | ------- | -------------------------------------- |
| `manala_thumbor_install_packages`         | ~                  | Array   | Dependency packages to install         |
| `manala_thumbor_install_packages_default` | ['thumbor']        | Array   | Default dependency packages to install |
| `manala_thumbor_key_file`                 | '/etc/thumbor.key' | String  | Key file path                          |
| `manala_thumbor_key`                      | ~                  | String  | Key                                    |
| `manala_thumbor_configs_exclusive`        | false              | Boolean | Configurations exclusivity             |
| `manala_thumbor_configs_dir`              | '/etc/thumbor.d'   | String  | Configurations dir path                |
| `manala_thumbor_configs_template`         | 'configs/empty.j2' | String  | Default configurations template path   |
| `manala_thumbor_configs`                  | []                 | Array   | Configurations                         |
| `manala_thumbor.services`                 | true               | Boolean | Handle services                        |

### Configuration example

```yaml

manala_thumbor_key: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

manala_thumbor_configs:
  - file: debian.conf
    template: configs/debian.j2
  - file: thumbor.conf
    template: configs/default.prod.j2
  - file: app.conf
    config:
      - MAX_WIDTH: 100
      - UPLOAD_MAX_SIZE: 1024
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.thumbor }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
