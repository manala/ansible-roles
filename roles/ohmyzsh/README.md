# Ansible Role: Oh My Zsh

This role will deal with the setup of [Oh My Zsh](http://ohmyz.sh/).

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

None.

## Dependencies

None.

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Oh My Zsh configuration

The `manala_ohmyzsh_users_defaults` key will allow you to define different users configuration default templates.

```yaml
manala_ohmyzsh_users_defaults:
  template: my/.zshrc.j2
```

The `manala_ohmyzsh_dir` key is used to specify the path where to checkout oh-my-zsh

```yaml
manala_ohmyzsh_dir: /usr/local/share/oh-my-zsh
```

### User configuration

This part allow you, with the key `manala_ohmyzsh_users`, to configure each user account as following:

| Name       | Default                   | Type         | Description                               |
| ---------- | ------------------------- | ------------ | ----------------------------------------- |
| `user`     | ~ (required)              | String       | User account name                         |
| `home`     | 'root' or '~' ~ item.user | String       | User account home directory               |
| `template` | ~                         | String       | Template used for Oh My Zsh configuration |
| `config`   | ~                         | Array/String | List of Oh My Zsh options                 |
| `state`    | 'present'                 | String       | State                                     |

```yaml
manala_ohmyzsh_users:
  # Template (recommended)
  - user: root
    template: users/manala/.zshrc.j2
    config:
      ZSH_THEME: default.prod
      plugins: [git, debian, common-aliases, history, history-substring-search]
  # Dict config
  - user: root
    group: foo # Default to user primary group, but can be overriden
    config:
      ZSH_THEME: default.prod
      plugins: [git, debian, common-aliases, history, history-substring-search]
  # Raw config
  - user: root
    config: |
      # Path to your oh-my-zsh installation.
      export ZSH=$HOME/.oh-my-zsh
  - user: bar
    state: ignore # Entry will be ignored
  # Flatten users
  - "{{ my_custom_users_array }}"
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
  # Flatten themes
  - "{{ my_custom_themes_array }}"
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
  tasks:
    - ansible.builtin.import_role:  
        name: manala.roles.ohmyzsh
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
