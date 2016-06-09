# Ansible Role: OhMyZsh (see: [https://github.com/robbyrussell/oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh))

This role will deal with the following configuration:
- Install ohmyzsh globally
- Setup a local zshrc file

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

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
| `manala_ohmyzsh_update`         | false                      | Boolean   | Whether or not we should auto retrieve new revision of ohMyZsh  |
| `manala_ohmyzsh_users_template` | users/default.j2           | String    | User config template                                            |
| `manala_ohmyzsh_users`          | []                         | Array     | Collection of users with ohMyZsh custom configurations.         |

### Oh My Zsh configuration

The `manala_ohmyzsh_users_template` key will allow you to use differents main configuration templates. The role is shipped with basic templates :

- base (Simple template with common configuration)
- dev (Dev configuration, provide a different OhMyZsh theme than production template)
- empty ("Let me handle this" template, no default configuration inside.)
- prod (For production purpose.)

#### Example

```yaml
manala_ohmyzsh_users_template: users/default.j2
```

The `manala_ohmyzsh_dir` key is used to specify the path where to checkout oh-my-zsh

#### Example

```yaml
manala_ohmyzsh_dir: /usr/local/share/oh-my-zsh
```

The `manala_ohmyzsh_update` option will allow Oh My Zsh to retrieve new revisions from the repository.

#### Example

```yaml
manala_ohmyzsh_update: false
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

env:        prod

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
