# Ansible Role: Mailhog [![Build Status](https://travis-ci.org/manala/ansible-role-mailhog.svg?branch=master)](https://travis-ci.org/manala/ansible-role-mailhog)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup and the config of [Mailhog](https://github.com/mailhog/MailHog).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

This role is made to work with the __manala__ mailhog debian package, available on the __manala__ debian repository. Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

```yaml
manala_apt_preferences:
  - mailhog@manala
```

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.mailhog
```

Using ansible galaxy requirements file:

```yaml
- src: manala.mailhog
```

## Role Handlers

None.

## Role Variables

### Definition

| Name                                      | Default     | Type   | Description                            |
| ----------------------------------------- | ----------- | ------ | -------------------------------------- |
| `manala_mailhog_install_packages`         | ~           | String | Dependency packages to install         |
| `manala_mailhog_install_packages_default` | ['mailhog'] | String | Default dependency packages to install |
| `manala_mailhog_config_template`          | ~           | String | Configuration template path            |
| `manala_mailhog_config`                   | []          | Array  | Configuration                          |

### Example

```yaml
- hosts: all
  vars:
    manala_mailhog_config_template: config/default.dev.j2
    manala_mailhog_config:
      - ui-bind-addr: 0.0.0.0:8080
  roles:
    - role: manala.mailhog
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
