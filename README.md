# Ansible Role: Vim

This role will deal with the setup and configuration of Vim by:
- Installing package
- Allow vim configuration by using the `/etc/vim/vimrc.local` file

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

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

| Name                         | Default              | Type         | Description                        |
|----------------------------- |--------------------- |------------- |----------------------------------- |
| `manala_vim_config_template` | config/empty.j2      | String (path)| Path to `vimrc.local` template     |
| `manala_vim_config_file`     | /etc/vim/vimrc.local | String       | Path to the vim configuration file |
| `manala_vim_config`          | Array                | List         | List of vim options                |

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
