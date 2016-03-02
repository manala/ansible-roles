<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

[![Ansible Role](https://img.shields.io/ansible/role/5533.svg?style=plastic)](https://galaxy.ansible.com/list#/roles/5533) [![Platforms](https://img.shields.io/badge/platforms-debian-lightgrey.svg?style=plastic)](#) [![License](http://img.shields.io/:license-mit-lightgrey.svg?style=plastic)](#)

# Ansible Role: Merge

It's part of the ELAO <a href="http://www.manalas.com" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install ElaoInfra.merge,2.0
```

Using ansible galaxy requirements file:

```yaml
- src:     ElaoInfra.merge
  version: 2.0
```

## Role Handlers

None.

## Role Variables

### Definition

| Name                | Default | Type  | Description |
| ------------------- | ------- | ----- | ----------- |
| `elao_apt_patterns` | []      | Array | Patterns    |

### Example

```yaml
- hosts: all
  vars:
    elao_merge_patterns:
      - _all
      - _env
      - _group_({{ group_names|join('|') }})
      - _host
  roles:
    - ElaoInfra.merge
```

### Patterns

...

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
