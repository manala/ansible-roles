# Ansible Role: Rsyslog [![Build Status](https://travis-ci.org/manala/ansible-role-rsyslog.svg?branch=master)](https://travis-ci.org/manala/ansible-role-rsyslog)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of [Rsyslog](http://www.rsyslog.com/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.rsyslog
```

Using ansible galaxy requirements file:

```yaml
- src: manala.rsyslog
```

## Role Handlers

| Name            | Type    | Description             |
| --------------- | ------- | ----------------------- |
| rsyslog restart | Service | Restart rsyslog service |


## Role Variables

| Name                              | Default                | Type   | Description                                           |
| --------------------------------- | ---------------------- | ------ | ----------------------------------------------------- |
| `manala_rsyslog_config_template`  | config/default.j2      | String | Rsyslog config base template (version 8.4.2)          |
| `manala_rsyslog_config`           | []                     | Array  | Rsyslog config directives                             |
| `manala_rsyslog_configs_template` | configs/empty.j2       | String | Rsyslog configs base template                         |
| `manala_rsyslog_configs`          | []                     | Array  | Rsyslog additional configs                            |
| `manala_rsyslog_configs_exclusive`| false                  | Array  | If true, will remove extra files in /etc/rsyslog.d    |

### Configuration example

```yaml
manala_rsyslog_config_template: config/default.{{ env }}.j2
manala_rsyslog_config:
  - $ModLoad imklog: false
  - $ModLoad immark: true
  - |
    *.=info;*.=notice;*.=warn;\
        auth,authpriv.none;\
        cron,daemon.none;\
        mail,news.none    -/var/log/messages

manala_rsyslog_configs_exclusive: true
manala_rsyslog_configs:
  - file: rules.conf
    template: configs/rules.prod.j2
  - file: extra_rules.conf
    config:
      - auth,authpriv.*           /var/log/auth.log
      - '*.*;auth,authpriv.none   -/var/log/syslog'
      - daemon.*                  -/var/log/daemon.log
      - kern.*                    -/var/log/kern.log
      - mail.*                    -/var/log/mail.log
      - user.*                    -/var/log/user.log
```

## Example playbook

```yaml
- hosts: all
  roles:
    - { role: manala.rsyslog }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
