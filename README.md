<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

[![Ansible Role](https://img.shields.io/ansible/role/5539.svg?style=plastic)](https://galaxy.ansible.com/list#/roles/5539) [![Platforms](https://img.shields.io/badge/platforms-debian-lightgrey.svg?style=plastic)](#) [![License](http://img.shields.io/:license-mit-lightgrey.svg?style=plastic)](#)

# Ansible Role: Vim

This role will assume the setup and configuration of Vim by:
- Installing package
- Allow vim configuration by using the `/etc/vim/vimrc.local` file

It's part of the ELAO [Ansible stack](http://www.manalas.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.9.0+

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install elao.vim,2.0
```

Using ansible galaxy requirements file:

```yaml
- src:     elao.vim
  version: 2.0
```

### Ansible 1 (no longer maintained)

Using ansible galaxy cli:

```bash
ansible-galaxy install elao.vim,1.0
```

Using ansible galaxy requirements file:

```yaml
- src:     elao.vim
  version: 1.0
```

## Role Handlers

None

## Role Variables

| Name                       | Default              | Type         | Description                        |
|--------------------------- |--------------------- |------------- |----------------------------------- |
| `elao_vim_config_template` | config/empty.j2      | String (path)| Path to `vimrc.local` template     |
| `elao_vim_config_file`     | /etc/vim/vimrc.local | String       | Path to the vim configuration file |
| `elao_vim_config`          | Array                | List         | List of vim options                |

### Configuring VIM

The `elao_nginx_config_template` key will allow you to use differents main configuration templates. The role is shipped with basic templates :

- base (Simple template with common configuration)
- dev (Development configuration)
- empty ("Let me handle this" template, no default configuration inside.)
- prod (For production purpose.)

#### Example

```yaml
---
_env:        prod

elao_vim_config_template: config/{{ _env }}.j2
```
In combination with it you can specify the vim configuration file with the `elao_vim_config_file`:

```yaml
---

elao_vim_config_file:     /etc/vim/vimrc.local
```

The `elao_vim_config` is used ton configure vim, you can specify any of the vim options (see: [http://vimconfig.com/](http://vimconfig.com/)) like following:

```yaml
elao_vim_config:
    syntax:     "on"
    encoding:   "utf8"
    expandtab:  true   # Use spaces instead of tabs
    smarttab:   true   # Be smart when using tabs ;)
    shiftwidth: 4      # 1 tab == 4 spaces
    tabstop:    4
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.vim }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
