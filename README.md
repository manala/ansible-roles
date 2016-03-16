<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

[![Ansible Role](https://img.shields.io/ansible/role/5540.svg?style=plastic)](https://galaxy.ansible.com/list#/roles/5540) [![Platforms](https://img.shields.io/badge/platforms-debian-lightgrey.svg?style=plastic)](#) [![License](http://img.shields.io/:license-mit-lightgrey.svg?style=plastic)](#)

# Ansible Role: Zsh

This role will assume the following configuration:
- Install zsh package

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.zsh,2.0
```

Using ansible galaxy requirements file:

```yaml
- src:     manala.zsh
  version: 2.0
```

### Ansible 1 (no longer maintained)

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.zsh,1.0
```

Using ansible galaxy requirements file:

```yaml
- src:     manala.zsh
  version: 1.0
```

## Role Variables

| Name                | Default  | Type    | Description              |
| ------------------- | -------- | ------- | ------------------------ |
| `manala_zsh_bin`    | /bin/zsh | String  | Path to zsh binary file  |

### Example
```yaml
manala_zsh_bin: /bin/zsh
```

## Example playbook

    - hosts: servers
      roles:
         - { role: manala.zsh }

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
