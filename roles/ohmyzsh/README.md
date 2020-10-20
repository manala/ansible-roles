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

| Name                                     | Default                      | Type    | Description                                                    |
| ---------------------------------------- | ---------------------------- | ------- | -------------------------------------------------------------- |
| `manala_ohmyzsh_dir`                     | '/usr/local/share/oh-my-zsh' | String  | Oh My Zsh installation directory                               |
| `manala_ohmyzsh_users_template`          | 'users/default.j2'           | String  | User config template                                           |
| `manala_ohmyzsh_users`                   | []                           | Array   | Collection of users with ohMyZsh custom configurations.        |
| `manala_ohmyzsh.update`                  | false                        | Boolean | Whether or not we should auto retrieve new revision of ohMyZsh |
| `manala_ohmyzsh_custom_themes_exclusive` | false                        | Boolean | Exclusion of existing custom themes                            |
| `manala_ohmyzsh_custom_themes_dir`       | '/etc/supervisor/conf.d'     | String  | Custom themes directory path                                   |
| `manala_ohmyzsh_custom_themes_defaults`  | {}                           | Array   | Custom themes defaults                                         |
| `manala_ohmyzsh_custom_themes`           | []                           | Array   | Custom themes                                                  |


### Oh My Zsh configuration

The `manala_ohmyzsh_users_template` key will allow you to use different main configuration templates. The role is shipped with basic templates :

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

| Name       | Default                      | Type   | Description                               |
| ---------- | ---------------------------- | ------ | ----------------------------------------- |
| `user`     | ~ (required)                 | String | User account name                         |
| `home`     | root or '/home/' ~ item.user | String | User account home directory               |
| `template` | ~ (required)                 | String | Template used for Oh My Zsh configuration |
| `config`   | []                           | Array  | List of Oh My Zsh options                 |
| `state`    | 'present'                    | String | State                                     |


```yaml
---

env: prod

manala_ohmyzsh_users:
  - user: root
    template: users/default.{{ env }}.j2
    config:
      - ZSH_THEME: default.prod
      - plugins: (git debian common-aliases history history-substring-search)
  - user: foo
    group: root # Default to user primary group, but can be overriden
    template: users/default.{{ env }}.j2
    config:
      - ZSH_THEME: default.prod
      - plugins: (git debian common-aliases history history-substring-search)
  - user: bar
    state: ignore # Entry will be ignored
```

### Custom themes

`manala_ohmyzsh_custom_themes_exclusive` allow you to clean up existing custom themes into directory defined by the `manala_ohmyzsh_custom_themes_dir` key. Made to be sure no old or manually created files will alter current configuration.

```yaml
manala_ohmyzsh_custom_themes_exclusive: true
```

```yaml
manala_ohmyzsh_custom_themes:
  - file: foo.zsh-theme
    config: |
      PROMPT="%{$fg[red]%}%n%{$reset_color%}@%{$fg[blue]%}%m %{$fg[yellow]%}%~ %{$reset_color%}%% "
  # Template based (file name based on template)
  - template: ohmyzsh/custom/template.zsh-theme.j2
  # Template based (force file name)
  - file: bar.zsh-theme
    template: ohmyzsh/custom/template.zsh-theme.j2
  # Ensure config is absent
  - file: absent.zsh-theme
    state: absent # "present" by default
  # Ignore config
  - file: ignore.zsh-theme
    state: ignore
```

Note: to ensure backward compatibility, this role will install these custom themes templates by default:

- custom/themes/default.dev.j2
- custom/themes/default.demo.j2
- custom/themes/default.staging.j2
- custom/themes/default.prod.j2

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
