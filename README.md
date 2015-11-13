<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

[![Ansible Role](https://img.shields.io/ansible/role/5540.svg?style=plastic)](https://galaxy.ansible.com/list#/roles/5540) [![Platforms](https://img.shields.io/badge/platforms-debian-lightgrey.svg?style=plastic)](#) [![License](http://img.shields.io/:license-mit-lightgrey.svg?style=plastic)](#)

# Ansible Role: ZSH

This role will assume the following configuration:
- Install zsh package

It's part of the ELAO <a href="http://www.manalas.com" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.zsh,1.0
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.zsh }
```

## Role Variables

| Name              | Default  | Type    | Description              |
| ----------------- | -------- | ------- | ------------------------ |
| `elao_zsh_bin`    | /bin/zsh | String  | Path to zsh binary file  |

### Example
```yaml
elao_zsh_bin: /bin/zsh
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.zsh }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)