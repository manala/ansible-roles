<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

[![Ansible Role](https://img.shields.io/ansible/role/5541.svg?style=plastic)](https://galaxy.ansible.com/list#/roles/5541) [![Platforms](https://img.shields.io/badge/platforms-debian-lightgrey.svg?style=plastic)](#) [![License](http://img.shields.io/:license-mit-lightgrey.svg?style=plastic)](#)

# Ansible Role: GIT

This role will assume the setup and configuration of git by:
- Installing GIT package
- Define the gitconfig file
- Allow setup of the giconfig file

It's part of the ELAO <a href="http://www.manalas.com" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

- Ansible 1.9.0+

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install elao.git,2.0
```

Using ansible galaxy requirements file:

```yaml
- src:     elao.git
  version: 2.0
```

### Ansible 1 (no longer maintained)

Using ansible galaxy cli:

```bash
ansible-galaxy install elao.git,1.0
```

Using ansible galaxy requirements file:

```yaml
- src:     elao.git
  version: 1.0
```

## Role Handlers

None

## Role Variables

| Name                       | Default           | Type          | Description                      |
|--------------------------- |------------------ |-------------- |--------------------------------- |
| `elao_git_config_file`     | /etc/gitconfig    | String (path) | Path to config file              |
| `elao_git_config_template` | config/empty.j2   | String (path) | Path to config template          |
| `elao_git_config`          | []                | Array         | List of git config options       |
| `elao_git_repositories`    | []                | Array         | List of repositories to checkout |

### GIT configuration

The `elao_git_config_file` key allow you to specify the path to the config file.

#### Example:

```yaml
---

elao_git_config_file: "{{ playbook_dir }}/templates/git/config.j2"
```

The `elao_git_config_template` key will allow you to use differents main configuration templates. The role is shipped with basic templates :

- base (Simple template with no default configuration)
- dev (This configuration will provide options for Vagrant VM, like ohmyzsh)
- test
- prod (For production purpose. Light configuration template)

GIT experienced users can provide their own custom template with the `elao_git_config_template` key.

The `elao_git_config` key allow to define git config keys like the following:

#### Example:

```yaml
---

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

### Auto-checkout of required repositories

The `elao_git_repositories` key is a "special one", it's designed to allow automatic checkout of specified repositories:

#### Variables

| Name      | Default      | Type       | Description                                                     |
|-----------|------------- |----------- |---------------------------------------------------------------- |
| `repo`    | ~ (required) | String     | git, SSH, or HTTP protocol address of the git repository        |
| `dest`    | ~ (required) | String     | PAbsolute path of where the repository should be checked out to |
| `version` | HEAD         | String     | What version of the repository to check out                     |
| `update`  | true         | Boolean    | If no, do not retrieve new revisions from the origin repository |

#### Example:

```yaml
---
elao_git_repositories:
  - repo:    https://github.com/symfony/symfony1.git
    dest:    /usr/share/symfony/symfony-1.4
    version: v1.4.20
    update:  false
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.git }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
