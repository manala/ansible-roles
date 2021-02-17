# Ansible Role: Git [![Build Status](https://travis-ci.org/manala/ansible-role-git.svg?branch=master)](https://travis-ci.org/manala/ansible-role-git)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup and configuration of git by:
- Installing GIT package
- Define the gitconfig file
- Allow setup of the giconfig file

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

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

| Name                                  | Default           | Type         | Description                            |
| ------------------------------------- | ----------------- | ------------ | -------------------------------------- |
| `manala_git_install_packages`         | ~                 | Array        | Dependency packages to install         |
| `manala_git_install_packages_default` | ['git']           | Array        | Default dependency packages to install |
| `manala_git_config_file`              | '/etc/gitconfig'  | String       | Configuration file path                |
| `manala_git_config_template`          | 'config/empty.j2' | String       | Configuration template path            |
| `manala_git_config`                   | ~                 | Array/String | Git config options                     |
| `manala_git_repositories`             | []                | Array        | List of repositories to checkout       |

### GIT configuration

The `manala_git_config_file` key allow you to specify the path to the config file.

GIT experienced users can provide their own custom template with the `manala_git_config_template` key.

Use template:
```yaml
manala_git_config_template: my/gitconfig.j2
manala_git_config:
  foo: bar
```

Use dict parameters:
```yaml
manala_git_config:
  user:
    name: Foo Bar
    email: foo.bar@manala.io
  core:
    filemode: false
```

Use raw config:
```yaml
manala_git_config: |
  [user]
      name = Foo Bar
      email = foo.bar@manala.io
  [core]
      filemode = false
```

Use dict's array parameters (deprecated):
```yaml
manala_git_config:
  - user:
    - name: Foo Bar
    - email: foo.bar@manala.io
  - core:
    - filemode: false
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
| `user`    | ~            | String     | Checkout repository as specified user                           |

#### Example:

```yaml
manala_git_repositories:
  - repo:    https://github.com/symfony/symfony1.git
    dest:    /usr/share/symfony/symfony-1.4
    version: v1.4.20
    update:  false
    user:    app
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - role: manala.git
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
