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

| Name                                      | Default              | Type         | Description                              |
| ----------------------------------------- | -------------------- | ------------ | ---------------------------------------- |
| `manala_rsyslog_install_packages`         | ~                    | Array        | Dependency packages to install           |
| `manala_rsyslog_install_packages_default` | ['rsyslog']          | Array        | Default dependency packages to install   |
| `manala_rsyslog_config_template`          | 'config/_default.j2' | String       | Configuration base template path         |
| `manala_rsyslog_config`                   | ~                    | Array/String | Configuration directives                 |
| `manala_rsyslog_configs_exclusive`        | false                | Array        | Additional configurations exclusivity    |
| `manala_rsyslog_configs_dir`              | '/etc/rsyslog.d'     | String       | Additional configurations directory path |
| `manala_rsyslog_configs_defaults`         | {}                   | Array        | Additional configurations defaults       |
| `manala_rsyslog_configs`                  | []                   | Array        | Additional configurations directives     |

### Configuration example

Content based
```yaml
manala_rsyslog_config: |
  $FileOwner root
  $FileGroup adm
  $FileCreateMode 0640
  $DirCreateMode 0755
  $Umask 0022
```

Template based
```yaml
manala_rsyslog_config_template: my/rsyslog.conf.j2
```

Dict's array parameters based (deprecated):
```yaml
manala_rsyslog_config_template: config/default.prod.j2
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

A state (present|absent|ignore) can be provided.

```yaml
manala_rsyslog_configs:
  # Config based
  - file: config.conf
    config:
      foo.*: -/var/log/foo.log
      bar.*: -/var/log/bar.log
  # Content based
  - file: content.conf
    config: |
      foo.* -/var/log/foo.log
      bar.* -/var/log/bar.log
  # Template based (file name based on template)
  - template: rsyslog/bar.conf.j2
    config:
      foo: bar
  # Template based (force file name)
  - file: baz.conf
    template: rsyslog/bar.conf.j2
    config:
      foo: bar
  # Dicts array template based (deprecated)
  - file: foo.conf
    template: configs/rules.prod.j2
    config:
      - auth,authpriv.*           /var/log/auth.log
      - '*.*;auth,authpriv.none   -/var/log/syslog'
      - daemon.*                  -/var/log/daemon.log
      - kern.*                    -/var/log/kern.log
      - mail.*                    -/var/log/mail.log
      - user.*                    -/var/log/user.log
  # Ensure config is absent
  - file: absent.conf
    state: absent # "present" by default
  # Ignore config
  - file: ignore.conf
    state: ignore
  # Flatten configs
  - "{{ my_custom_configs_array }}"
```

`manala_rsyslog_configs_exclusive` allow you to clean up existing rsyslog configuration files into directory defined by the `manala_rsyslog_configs_dir` key. Made to be sure no old or manually created files will alter current configuration.

```yaml
manala_rsyslog_configs_exclusive: true
```

## Example playbook

```yaml
- hosts: all
  roles:
    - role: manala.rsyslog
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
