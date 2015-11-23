<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

[![Ansible Role](https://img.shields.io/ansible/role/<skeleton>.svg?style=plastic)](https://galaxy.ansible.com/list#/roles/<skeleton>) [![Platforms](https://img.shields.io/badge/platforms-debian-lightgrey.svg?style=plastic)](#) [![License](http://img.shields.io/:license-mit-lightgrey.svg?style=plastic)](#)

# Ansible Role: <skeleton>

This role will assume the setup of <skeleton>

It's part of the ELAO <a href="http://www.manalas.com" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

- Ansible 1.9.0+

## Dependencies

None.

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.<skeleton>,1.0
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.<skeleton> }
```

## Role Handlers

| Name                 | Type    | Description               |
| -------------------- | ------- | ------------------------- |
| `<skeleton> restart` | Service | Restart <skeleton> server |

## Role Variables

| Name                                | Default                           | Type    | Description                                 |
| ----------------------------------- | --------------------------------  | ------- | ------------------------------------------- |
| `elao_<skeleton>_config_template`   | config/<skeleton>_default.conf.j2 | String  | Main config template                        |
| `elao_<skeleton>_config`            | {}                                | Array   | Main config                                 |
| `elao_<skeleton>_configs`           | {}                                | Array   | Configs                                     |
| `elao_<skeleton>_configs_template`  | configs/empty.conf.j2             | String  | Configs default template                    |
| `elao_<skeleton>_configs_exclusive` | false                             | Boolean | Exclusion of existings files                |
| `elao_<skeleton>_configs_dir`       | /etc/<skeleton>/conf.d            | String  | Path to the main configuration directory    |
| `elao_<skeleton>_user`              | <skeleton>                        | String  | Service and config files owner              |

### Configuration example

```yaml
elao_<skeleton>_config:
  foo: bar
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.<skeleton> }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
