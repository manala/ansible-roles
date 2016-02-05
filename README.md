<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

[![Ansible Role](https://img.shields.io/ansible/role/5540.svg?style=plastic)](https://galaxy.ansible.com/list#/roles/5540) [![Platforms](https://img.shields.io/badge/platforms-debian-lightgrey.svg?style=plastic)](#) [![License](http://img.shields.io/:license-mit-lightgrey.svg?style=plastic)](#)

# Ansible Role: ZSH

This role will assume the following configuration:
- Install zsh package

It's part of the ELAO <a href="http://www.manalas.com" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install elao.zsh,2.0
```

Using ansible galaxy requirements file:

```yaml
- src:     elao.zsh
  version: 2.0
```

### Ansible 1 (no longer maintained)

Using ansible galaxy cli:

```bash
ansible-galaxy install elao.zsh,1.0
```

Using ansible galaxy requirements file:

```yaml
- src:     elao.zsh
  version: 1.0
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