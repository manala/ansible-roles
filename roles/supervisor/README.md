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

| Name                                         | Default        | Type  | Description                            |
| -------------------------------------------- | -------------- | ----- | -------------------------------------- |
| `manala_supervisor_install_packages`         | ~              | Array | Dependency packages to install         |
| `manala_supervisor_install_packages_default` | ['supervisor'] | Array | Default dependency packages to install |
| `manala_supervisor_config                    | []             | Array | Main configuration directives          |
| `manala_supervisor_configs                   | []             | Array | Additional configurations directives   |

### Configuration example

```yaml
manala_supervisor_config:
  - loglevel: info
```

Enable http server

```yaml
manala_supervisor_configs:
  - file:     inet_http_server.conf
    template: configs/inet_http_server.dev.j2
    config:
      - port: "*:9001"
```

Program

```yaml
manala_supervisor_configs:
  - file: foo.conf
    template: configs/program.dev.j2
    config:
      - foo:
        - command: bar
        - environment:
            FOO: bar
            BAR: 12
  - file: bar.conf
    state: absent
```

Raw content

```yaml
manala_supervisor_configs:
  - file: bar.conf
    content: |
      [program:example]
      command=/usr/bin/example --loglevel=%(ENV_LOGLEVEL)s
```

`manala_supervisor_configs_exclusive` allow you to clean up existing supervisor configuration files into directory defined by the `manala_supervisor_configs_dir` key. Made to be sure no old or manually created files will alter current configuration.

```yaml
manala_supervisor_configs_exclusive: true
```

A state (present|absent) can be provided.

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.supervisor }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
