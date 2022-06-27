# Ansible Role: Supervisor

This role will deal with the setup of [Supervisor](http://supervisord.org/).

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

This role is made to work with the __manala__ supervisor debian package, available on the __manala__ debian repository. Please use the [**manala.roles.apt**](../apt/) role to handle it properly.

```yaml
manala_apt_preferences:
  - supervisor@manala
```

## Dependencies

None.

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

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
  tasks:
    - ansible.builtin.import_role:  
        name: manala.roles.supervisor
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
