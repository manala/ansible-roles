# Ansible Role: GIT

This role will deal with the setup and configuration of git by:
- Installing GIT package
- Define the gitconfig file
- Allow setup of the giconfig file

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.git
```

Using ansible galaxy requirements file:

```yaml
- src: manala.git
```

## Role Handlers

None

## Role Variables

| Name                         | Default           | Type          | Description                      |
|----------------------------- |------------------ |-------------- |--------------------------------- |
| `manala_git_config_file`     | /etc/gitconfig    | String (path) | Path to config file              |
| `manala_git_config_template` | config/empty.j2   | String (path) | Path to config template          |
| `manala_git_config`          | []                | Array         | List of git config options       |
| `manala_git_repositories`    | []                | Array         | List of repositories to checkout |

### GIT configuration

The `manala_git_config_file` key allow you to specify the path to the config file.

#### Example:

```yaml
---

manala_git_config_file: "{{ playbook_dir }}/templates/git/config.j2"
```

The `manala_git_config_template` key will allow you to use differents main configuration templates. The role is shipped with basic templates :

- base (Simple template with no default configuration)
- dev (This configuration will provide options for Vagrant VM, like ohmyzsh)
- test
- prod (For production purpose. Light configuration template)

GIT experienced users can provide their own custom template with the `manala_git_config_template` key.

The `manala_git_config` key allow to define git config keys like the following:

#### Example:

```yaml
---

manala_git_config:
  - user:
    - name:           "Foo Bar"
    - email:          "foo.bar@manala.io"

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

The `manala_git_repositories` key is a "special one", it's designed to allow automatic checkout of specified repositories:

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
manala_git_repositories:
  - repo:    https://github.com/symfony/symfony1.git
    dest:    /usr/share/symfony/symfony-1.4
    version: v1.4.20
    update:  false
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.git }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
