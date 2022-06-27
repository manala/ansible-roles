# Ansible Role: Vim

This role will deal with the setup and configuration of Vim.

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

None.

## Dependencies

None.

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Configuring VIM

The `manala_vim_config_template` key will allow you to use configuration templates.

#### Example

```yaml
manala_vim_config_template: my/vim.j2
```
In combination with it you can specify the vim configuration file with the `manala_vim_config_file`:

```yaml
manala_vim_config_file: /etc/vim/vimrc.local
```

The `manala_vim_config` is used ton configure vim, you can specify any of the vim options (see: [http://vimconfig.com/](http://vimconfig.com/)) like following:

Use dict parameters:
```yaml
manala_vim_config:
  syntax: "on"
  encoding: utf8
  expandtab: true   # Use spaces instead of tabs
  smarttab: true   # Be smart when using tabs ;)
  shiftwidth: 4      # 1 tab == 4 spaces
  tabstop: 4
```

Use raw config:
```yaml
manala_vim_config: |
  set encoding=utf8
  set expandtab
```

## Example playbook

```yaml
- hosts: servers
  tasks:
    - ansible.builtin.import_role:  
        name: manala.roles.vim
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
