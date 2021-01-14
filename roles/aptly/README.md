# Ansible Role: Aptly [![Build Status](https://travis-ci.org/manala/ansible-role-aptly.svg?branch=master)](https://travis-ci.org/manala/ansible-role-aptly)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of [Aptly](https://www.aptly.info/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.aptly
```

Using ansible galaxy requirements file:

```yaml
- src: manala.aptly
```

## Role Handlers

None.

## Role Variables

### Definition

| Name                                    | Default            | Type         | Description                            |
| --------------------------------------- | ------------------ | ------------ | -------------------------------------- |
| `manala_aptly_install_packages`         | ~                  | Array        | Dependency packages to install         |
| `manala_aptly_install_packages_default` | ['bzip2', 'aptly'] | Array        | Default dependency packages to install |
| `manala_aptly_user`                     | ~                  | String       | User                                   |
| `manala_aptly_config_file`              | '/etc/aptly.conf'  | String       | Config file path                       |
| `manala_aptly_config_template`          | ~                  | String       | Config template path                   |
| `manala_aptly_config`                   | ~                  | Array/String | Config                                 |
| `manala_aptly_repositories`             | []                 | Array        | Collection of repositories             |

### Configuration example

User:

```yaml
manala_aptly_user: aptly
```

Use template:

```yaml
manala_aptly_config_template: my/aptly.conf.j2
manala_aptly_config:
  foo: bar
```

Use dict parameters:
```yaml
manala_aptly_config:
  rootDir: /tmp/aptly
  architectures:
    - amd64
```

Use raw config:
```yaml
manala_aptly_config: |
  {
      "rootDir": "/tmp/aptly",
      "architectures": [
          "amd64"
      ]
  }
```

Use dict's array parameters (deprecated):
```yaml
manala_aptly_config:
  - rootDir: /tmp/aptly
  - architectures:
    - amd64
```

Repositories:

```yaml
manala_aptly_repositories:
  - name: stretch
    comment: Stretch
    component: main
    distribution: stretch
    origin: Foo
    label: Bar
  - name: buster
    comment: Buster
    component: main
    distribution: buster
    origin: Foo
    label: Bar
  # Ignore repository
  - name: ignore
    state: ignore
  # Flatten repositories
  - "{{ my_custom_repositories_array }}"
```

## Example playbook

 ```yaml
 - hosts: servers
   roles:
     - role: manala.aptly
 ```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
