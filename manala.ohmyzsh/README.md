# Ansible Role: Oh My Zsh [![Build Status](https://travis-ci.org/manala/ansible-role-ohmyzsh.svg?branch=master)](https://travis-ci.org/manala/ansible-role-ohmyzsh)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of [Oh My Zsh](http://ohmyz.sh/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.ohmyzsh
```

Using ansible galaxy requirements file:

```yaml
- src: manala.ohmyzsh
```

## Role Handlers

None

## Role Variables

| Name                            | Default                    | Type      |Description                                                      |
|-------------------------------- |--------------------------- |---------- |---------------------------------------------------------------- |
| `manala_ohmyzsh_dir`            | /usr/local/share/oh-my-zsh | String    | ohMyZsh installation directory                                  |
| `manala_ohmyzsh_users_template` | users/default.j2           | String    | User config template                                            |
| `manala_ohmyzsh_users`          | []                         | Array     | Collection of users with ohMyZsh custom configurations.         |
| `manala_ohmyzsh.update`         | false                      | Boolean   | Whether or not we should auto retrieve new revision of ohMyZsh  |

### Oh My Zsh configuration

The `manala_ohmyzsh_users_template` key will allow you to use differents main configuration templates. The role is shipped with basic templates :

- base (Simple template with common configuration)
- dev (Dev configuration, provide a different OhMyZsh theme than production template)
- empty ("Let me handle this" template, no default configuration inside.)
- prod (For production purpose.)

```yaml
manala_ohmyzsh_users_template: users/default.j2
```

The `manala_ohmyzsh_dir` key is used to specify the path where to checkout oh-my-zsh

```yaml
manala_ohmyzsh_dir: /usr/local/share/oh-my-zsh
```

### User configuration

This part allow you, with the key `manala_ohmyzsh_users`, to configure each user account as following:

| Name      | Default                      | Type       | Description                               |
|-----------|----------------------------- |----------- |------------------------------------------ |
| `user`    | ~ (required)                 | String     | User account name                         |
| `home`    | root or '/home/' ~ item.user | String     | User account home directory               |
| `template`| ~ (required)                 | String     | Template used for Oh My Zsh configuration |
| `config`  | []                           | Array      | List of Oh My Zsh options                 |


```yaml
---

env: prod

manala_ohmyzsh_users:
  - user:     root
    template: users/default.{{ env }}.j2
    config:
      - ZSH_THEME: default.prod
      - plugins: (git debian common-aliases history history-substring-search)
  - user:     foo
    group:    root # Default to user primary group, but can be overriden
    template: users/default.{{ env }}.j2
    config:
      - ZSH_THEME: default.prod
      - plugins: (git debian common-aliases history history-substring-search)
```

### Flags

Allow Oh My Zsh to retrieve new revisions from the repository
```yaml
manala_ohmyzsh:
  update: true

# Can also be set across manala roles
manala:
  update: true
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.ohmyzsh }
```

## Testing themes

```bash
make dev@jessie
make test-themes
/bin/zsh
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
