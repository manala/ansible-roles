<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

[![Ansible Role](https://img.shields.io/ansible/role/5538.svg?style=plastic)](https://galaxy.ansible.com/list#/roles/5538) [![Platforms](https://img.shields.io/badge/platforms-debian-lightgrey.svg?style=plastic)](#) [![License](http://img.shields.io/:license-mit-lightgrey.svg?style=plastic)](#)

# Ansible Role: Alternatives

This role will assume the setup of alternatives

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.s

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.alternatives,2.0
```

Using ansible galaxy requirements file:

```yaml
- src:     manala.alternatives
  version: 2.0
```

### Ansible 1 (no longer maintained)

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.alternatives,1.0
```

Using ansible galaxy requirements file:

```yaml
- src:     manala.alternatives
  version: 1.0
```

## Role Variables

| Name                 | Default| Type  | Description   |
|--------------------- |------- |------ |-------------  |
| manala_alternatives  | []     | Array | Alternatives  |

### Configuration

`manala_alternatives` allow you to managed custom alternatives path.

```yaml
manala_alternatives:
  - name: editor
    path: /usr/bin/vim.basic
```

## Example playbook

    - hosts: servers
      roles:
         - { role: manala.alternatives }

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
