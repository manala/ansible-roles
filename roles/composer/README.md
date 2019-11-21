# Ansible Role: Composer [![Build Status](https://travis-ci.org/manala/ansible-role-composer.svg?branch=master)](https://travis-ci.org/manala/ansible-role-composer)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of [Composer](https://getcomposer.org)

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

This role requires php-cli >=5.3.2. You can use [manala.php](https://github.com/manala/ansible-role-php) role.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.composer
```

Using ansible galaxy requirements file:

```yaml
- src: manala.composer
```

## Role Handlers

None.

## Role Variables

### Definition

| Name                                       | Default                        | Type   | Description                            |
| ------------------------------------------ | ------------------------------ | ------ | -------------------------------------- |
| `manala_composer_install_packages`         | ~                              | Array  | Dependency packages to install         |
| `manala_composer_install_packages_default` | ['openssl', 'ca-certificates'] | Array  | Default dependency packages to install |
| `manala_composer_version`                  | ~                              | String | Version to install, latest by default  |
| `manala_composer_bin`                      | '/usr/local/bin/composer'      | String | Binary path                            |
| `manala_composer_users_auth_template`      | ~                              | String | User auth template path                |
| `manala_composer_users_auth`               | []                             | Array  | User auth config                       |

### Configuration example

#### Composer configuration with github token

```yaml
manala_composer_users_auth:
  - user: foo
    config:
      - github-oauth:
        - github.com: 9927d2878ffa105fc5236c762f2fd7zfd28b841d
      - http-basic:
        - repo.example1.org:
          - username: my-username1
          - password: my-secret-password1
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.composer }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
