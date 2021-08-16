# Ansible Role: Logrotate [![Build Status](https://travis-ci.org/manala/ansible-role-logrotate.svg?branch=master)](https://travis-ci.org/manala/ansible-role-logrotate)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will assume the setup of Logrotate.

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.logrotate
```

Using ansible galaxy requirements file:

```yaml
- src: manala.logrotate
```

## Role Handlers

None

## Role Variables

| Name                                        | Default            | Type    | Description                                |
| ------------------------------------------- | ------------------ | ------- | ------------------------------------------ |
| `manala_logrotate_install_packages`         | ~                  | Array   | Dependency packages to install             |
| `manala_logrotate_install_packages_default` | ['logrotate']      | Array   | Default dependency packages to install     |
| `manala_logrotate_configs_exclusive`        | false              | Boolean | Exclusion of existing files Configurations |
| `manala_logrotate_configs_dir`              | '/etc/logrotate.d' | String  | Configurations directory path              |
| `manala_logrotate_configs_defaults`         | {}                 | Array   | Configurations defaults                    |
| `manala_logrotate_configs`                  | []                 | Array   | Configurations directives                  |

### Configurations examples

```yaml
manala_logrotate_configs:
  # Config based
  - file: config
    config:
      /var/log/nginx/example/*.log:
        size: 200M
        missingok: true
        rotate: 0
  # Content based
  - file: content
    config: |
      /var/log/nginx/example/*/*.log
      /var/log/nginx/example/*/*/*.log {
          size 200M
          missingok
          rotate 0
          compress
          delaycompress
          notifempty
          create 0640 www-data adm
          sharedscripts
      }
  # Template based (file name based on template)
  - template: telegraf/bar.j2
    config:
      foo: bar
  # Template based (force file name)
  - file: baz
    template: telegraf/bar.j2
    config:
      foo: bar
  # Ensure config is absent
  - file: absent
    state: absent # "present" by default
  # Ignore config
  - file: ignore
    state: ignore
  # Flatten configs
  - "{{ my_custom_configs_array }}"
```

`manala_logrotate_configs_exclusive` allow you to clean up existing logrotate configuration files into directory defined by the `manala_logrotate_configs_dir` key. Made to be sure no old or manually created files will alter current configuration.

```yaml
manala_logrotate_configs_exclusive: true
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - role: manala.logrotate
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
