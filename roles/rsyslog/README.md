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

| Name              | Type    | Description             |
| ----------------- | ------- | ----------------------- |
| `rsyslog restart` | Service | Restart rsyslog service |


## Role Variables

| Name                                     | Default              | Type   | Description                            |
| ----------------------------------------- | ------------------- | ------ | -------------------------------------- |
| `manala_rsyslog_install_packages`         | ~                   | Array  | Dependency packages to install         |
| `manala_rsyslog_install_packages_default` | ['rsyslog']         | Array  | Default dependency packages to install |
| `manala_rsyslog_config_template`          | 'config/default.j2' | String | Configuration base template path       |
| `manala_rsyslog_config`                   | []                  | Array  | Configuration directives               |
| `manala_rsyslog_configs_template`         | 'configs/empty.j2'  | String | Configurations base template path      |
| `manala_rsyslog_configs`                  | []                  | Array  | Additional configurations              |
| `manala_rsyslog_configs_exclusive`        | false               | Array  | Additional configurations exclusivity  |

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
```

### Configs

`manala_rsyslog_configs` allows you to define rsyslog configuration files using template and config, or raw content.

A state (present|absent) can be provided.

```yaml
manala_rsyslog_configs:
  # Template based
  - file: foo_template.conf
    template: configs/rules.prod.j2
  # Config based, empty template by default
  - file: foo.conf
    config:
      - auth,authpriv.*           /var/log/auth.log
      - '*.*;auth,authpriv.none   -/var/log/syslog'
      - daemon.*                  -/var/log/daemon.log
      - kern.*                    -/var/log/kern.log
      - mail.*                    -/var/log/mail.log
      - user.*                    -/var/log/user.log
  # Raw content based
  - file: foo_content.conf
    content: |
      APT::Install-Recommends "false";
    state: absent
```

`manala_rsyslog_configs_exclusive` allow you to clean up existing rsyslog configuration files into directory defined by the `manala_rsyslog_configs_dir` key. Made to be sure no old or manually created files will alter current configuration.

```yaml
manala_rsyslog_configs_exclusive: true
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
