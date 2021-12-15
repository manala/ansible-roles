#######################################################################################################

# :exclamation: DEPRECATION :exclamation:

## This repository and the role associated are deprecated in favor of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles)

## You will find informations on its usage on the [collection repository](https://github.com/manala/ansible-roles)

#######################################################################################################

# Ansible Role: Fail2Ban [![Build Status](https://travis-ci.org/manala/ansible-role-fail2ban.svg?branch=master)](https://travis-ci.org/manala/ansible-role-fail2ban)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup and config of [Fail2Ban](https://www.fail2ban.org/wiki/index.php/Main_Page).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.fail2ban
```

Using ansible galaxy requirements file:

```yaml
- src: manala.fail2ban
```

## Role Handlers

| Name               | Type    | Description             |
| ------------------ | ------- | ----------------------- |
| `fail2ban restart` | Service | Restart fail2ban server |

## Role Variables

| Name                                       | Default           | Type   | Description                            |
| ------------------------------------------ | ----------------- | ------ | -------------------------------------- |
| `manala_fail2ban_install_packages`         | ~                 | Array  | Dependency packages to install         |
| `manala_fail2ban_install_packages_default` | ['fail2ban']      | Array  | Default dependency packages to install |
| `manala_fail2ban_config_template`          | 'config/empty.j2' | String | Main config template                   |
| `manala_fail2ban_config`                   | []                | Array  | Main config                            |

### Configuration

```yaml
manala_fail2ban_config:
  - DEFAULT:
    - maxretry: 5
  - apache:
    - enabled: true
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.fail2ban }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
