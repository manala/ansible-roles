<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: Vim

This role will assume the setup and configuration of Vim by:
- Installing package
- Allow vim configuration by using the `/etc/vim/vimrc.local` file

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.vim
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.vim }
```

## Role Handlers

None

## Role Variables

### Definition

|Name|Default|Type|Description|
|----|----|-----------|-------|
`elao_vim_config_template`|config/default.j2|String (path)|Path to `vimrc.local` template
`elao_vim_config`|Array|List|List of vim options

### Configuration example

```
---

elao_vim_config_template: "{{ playbook_dir ~ '/templates/vim/config.j2' }}"

elao_vim_config:
    syntax:     "on"
    encoding:   "utf8"
    mouse:      "a"
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
