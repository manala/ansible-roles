# Ansible Role: Vim [![Build Status](https://travis-ci.org/manala/ansible-role-vim.svg?branch=master)](https://travis-ci.org/manala/ansible-role-vim)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup and configuration of Vim.

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.vim
```

Using ansible galaxy requirements file:

```yaml
- src: manala.vim
```

## Role Handlers

None

## Role Variables

| Name                                  | Default                | Type   | Description                            |
| ------------------------------------- | ---------------------- | ------ | -------------------------------------- |
| `manala_vim_install_packages`         | ~                      | Array  | Dependency packages to install         |
| `manala_vim_install_packages_default` | ['vim']                | Array  | Default dependency packages to install |
| `manala_vim_config_template`          | 'config/empty.j2'      | String | `vimrc.local` template path            |
| `manala_vim_config_file`              | '/etc/vim/vimrc.local' | String | Configuration file path                |
| `manala_vim_config`                   | []                     | Array  | Configuration directives               |

### Configuring VIM

The `manala_nginx_config_template` key will allow you to use differents main configuration templates. The role is shipped with basic templates :

- base (Simple template with common configuration)
- dev (Development configuration)
- empty ("Let me handle this" template, no default configuration inside.)
- prod (For production purpose.)

#### Example

```yaml
---
env:        prod

manala_vim_config_template: config/default.{{ env }}.j2
```
In combination with it you can specify the vim configuration file with the `manala_vim_config_file`:

```yaml
---

manala_vim_config_file:     /etc/vim/vimrc.local
```

The `manala_vim_config` is used ton configure vim, you can specify any of the vim options (see: [http://vimconfig.com/](http://vimconfig.com/)) like following:

```yaml
manala_vim_config:
    syntax:     "on"
    encoding:   "utf8"
    expandtab:  true   # Use spaces instead of tabs
    smarttab:   true   # Be smart when using tabs ;)
    shiftwidth: 4      # 1 tab == 4 spaces
    tabstop:    4
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.vim }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
