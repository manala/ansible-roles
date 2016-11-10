# Ansible Role: Fail2Ban [![Build Status](https://travis-ci.org/manala/ansible-role-fail2ban.svg?branch=master)](https://travis-ci.org/manala/ansible-role-fail2ban)

This role will deal with the setup and config of fail2ban

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

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

| Name                              | Default         | Type    | Description          |
| --------------------------------- | --------------- | ------- | ---------------------|
| `manala_fail2ban_config_template` | config/empty.j2 | String  | Main config template |
| `manala_fail2ban_config`          | []              | Array   | Main config          |

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
