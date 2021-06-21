# Ansible Role: Supervisor [![Build Status](https://travis-ci.org/manala/ansible-role-supervisor.svg?branch=master)](https://travis-ci.org/manala/ansible-role-supervisor)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of [Supervisor](http://supervisord.org/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

This role is made to work with the __manala__ supervisor debian package, available on the __manala__ debian repository. Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

```yaml
manala_apt_preferences:
  - supervisor@manala
```

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.supervisor
```

Using ansible galaxy requirements file:

```yaml
- src: manala.supervisor
```

## Role Handlers

| Name                 | Type    | Description                |
| -------------------- | ------- | -------------------------- |
| `supervisor restart` | Service | Restart supervisor service |

## Role Variables

| Name                                         | Default                            | Type         | Description                                           |
| -------------------------------------------- | ---------------------------------- | ------------ | ----------------------------------------------------- |
| `manala_supervisor_install_packages`         | ~                                  | Array        | Dependency packages to install                        |
| `manala_supervisor_install_packages_default` | ['supervisor']                     | Array        | Default dependency packages to install                |
| `manala_supervisor_config_file`              | '/etc/supervisor/supervisord.conf' | String       | Main configuration file path                          |
| `manala_supervisor_config_template`          | 'config/_default.j2'               | String       | Main configuration template path                      |
| `manala_supervisor_config`                   | ~                                  | Array/String | Main configuration directives                         |
| `manala_supervisor_configs_exclusive`        | false                              | Boolean      | Exclusion of existing files additional configurations |
| `manala_supervisor_configs_dir`              | '/etc/supervisor/conf.d'           | String       | Additional configurations directory path              |
| `manala_supervisor_configs_defaults`         | {}                                 | Array        | Additional configurations defaults                    |
| `manala_supervisor_configs`                  | []                                 | Array        | Additional configurations directives                  |
| `manala_supervisor_log_dir`                  | '/var/log/supervisor'              | String       | Log directory path                                    |

### Configuration example

Use debian default main config template (recommended):
```yaml
manala_supervisor_config_template: config/debian/supervisord.conf.j2
manala_supervisor_config:
  supervisord:
    logfile: /var/log/supervisord.log # Change or add only some parameters
```

Start from a fresh empty main config, using dict parameters:
```yaml
manala_supervisor_config:
  unix_http_server:
    file: /tmp/supervisor.sock
    chmod: "0700"
    chown: nobody:nogroup
  supervisord:
    logfile: /var/log/supervisord.log
    ...
```

Use raw main config:
```yaml
manala_supervisor_config: |
  [unix_http_server]
  file=/tmp/supervisor.sock
  chmod=0700
  chown=nobody:nogroup

  [supervisord]
  logfile=/var/log/supervisord.log
  ...
```

Use dict's array parameters (deprecated):
```yaml
manala_supervisor_config:
  - loglevel: info
```

Enable http server:
```yaml
manala_supervisor_configs:
  # Template based (file name based on template)
  - template: configs/inet_http_server.conf.j2
    config:
      port: "*:9001"
  # Template based (force file name)
  - file: inet.conf
    template: configs/inet_http_server.conf.j2
    config:
      port: "*:9001"      
```

Programs:
```yaml
manala_supervisor_configs:
  - file: programs_dict.conf
    config:
      program:foo:
        command: /bin/foo
        priority: 123
        autostart: true
        stopsignal: HUP
        environment:
          FOO: bar
          BAR: 123
      program:bar:
        command: /bin/bar
  - file: programs_raw.conf
    config: |
      [program:foo]
      command=/bin/foo
  - file: foo_dicts_array.conf # Deprecated
    config:
      - foo:
        - command: bar
        - environment:
            FOO: bar
            BAR: 12
  # Ensure config is absent
  - file: absent.conf
    state: absent # "present" by default
  # Ignore config
  - file: ignore.conf
    state: ignore
  # Flatten configs
  - "{{ my_custom_configs_array }}"
```

Raw content

```yaml
manala_supervisor_configs:
  - file: bar.conf
    config: |
      [program:example]
      command=/usr/bin/example --loglevel=%(ENV_LOGLEVEL)s
```

`manala_supervisor_configs_exclusive` allow you to clean up existing supervisor configuration files into directory defined by the `manala_supervisor_configs_dir` key. Made to be sure no old or manually created files will alter current configuration.

```yaml
manala_supervisor_configs_exclusive: true
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - role: manala.supervisor
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
