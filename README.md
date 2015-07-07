<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: GIT

This role will assume the setup and configuration of git by:
- Installing GIT package
- Define the gitconfig file
- Allow setup of the giconfig file

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Dependencies

None.

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.git
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.git }
```

## Role Handlers

None

## Role Variables

### Definition

|Name|Default|Type|Description|
|----|----|-----------|-------|
`elao_git_config_file`|/etc/gitconfig|String (path)|Path to config file
`elao_git_config_template`|config/default.j2|String (path)|Path to config template
`elao_git_config`|Array|List|List of git config options

### Configuration example

```
---

elao_git_config_template: "{{ playbook_dir }}/templates/git/config.j2"

elao_git_config:
  - user:
    - name:           "Guewen FAIVRE"
    - email:          "guewen.faivre@elao.com"

  - core:
    - autocrlf:       input
    - compression:    9
    - excludesfile:   "~/.gitignore_global"
    - filemode:       false

  - remote "france":
    - url:            git://repohost/project1.git
    - fetch:          +refs/heads/*:refs/remotes/origin/*

  - color:
    - ui:             "true"

  - color:
    - option:         branch
    - current:        yellow reverse
    - local:          yellow
    - remote:         green

  - color:
    - option:         diff
    - meta:           yellow bold
    - frag:           magenta bold
    - old:            red bold
    - new:            green bold

  - color:
    - option:         status
    - added:          yellow
    - changed:        green
    - untracked:      red

  - alias:
    - br:             branch -av
    - ci:             commit

```

For git experienced users you can provide your own custom template with the `elao_git_config_template` key

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.git }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
