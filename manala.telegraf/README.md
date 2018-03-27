# Ansible Role: Telegraf [![Build Status](https://travis-ci.org/manala/ansible-role-telegraf.svg?branch=master)](https://travis-ci.org/manala/ansible-role-telegraf)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup and the config of [influxdata Telegraf](https://github.com/influxdata/telegraf).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

This role is made to work with the __telegraf__ official debian packages, available on the [__influxdata__ debian repository](https://www.influxdata.com/package-repository-for-linux/). Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.telegraf
```

Using ansible galaxy requirements file:

```yaml
- src: manala.telegraf
```

## Role Handlers

| Name               | Type    | Description            |
| ------------------ | ------- | ---------------------- |
| `telegraf restart` | Service | Restart telegraf agent |

## Role Variables

| Name                                       | Default              | Type   | Description                                  |
| ------------------------------------------ | -------------------- | ------ | -------------------------------------------- |
| `manala_telegraf_install_packages`         | ~                    | String | Dependency packages to install               |
| `manala_telegraf_install_packages_default` | ['telegraf']         | String | Default dependency packages to install       |
| `manala_telegraf_config_template`          | 'config/empty.j2'    | String | Main configuration base template path        |
| `manala_telegraf_config`                   | []                   | Array  | Main configuration directives                |
| `manala_telegraf_configs_template`         | 'configs/default.j2' | String | Additional configurations base template path |
| `manala_telegraf_configs`                  | []                   | Array  | Additional configurations directives         |
| `manala_telegraf_configs_exclusive`        | false                | Array  | Additional configurations exclusivity        |

### Configuration example

See https://github.com/influxdata/telegraf/blob/master/docs/CONFIGURATION.md

```yaml
manala_telegraf_config:
  - agent:
    - hostname: "{{ ansible_fqdn }}"
    - quiet: true

manala_telegraf_configs_exclusive: true
manala_telegraf_configs:
  - file:     output_influxdb.conf
    template: configs/output_influxdb.conf.j2
    config:
      - urls: ["udp://127.0.0.1:8090"]
      - database: telegraf
      - username: telegraf
      - password: password

  - file:     input_system.conf
    template: configs/input_system.conf.j2

  - file:     input_cpu.conf
    template: configs/input_cpu.conf.j2

  - file:     input_custom.conf
    template: "{{ playbook_dir }}/templates/telegraf/input_custom.conf.j2"
```

## Example playbook

```yaml
- hosts: all
  roles:
    - { role: manala.telegraf }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
