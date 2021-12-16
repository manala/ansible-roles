#######################################################################################################

# :exclamation: DEPRECATION :exclamation:

## This repository and the role associated are deprecated in favor of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles)

## You will find informations on its usage on the [collection repository](https://github.com/manala/ansible-roles)

#######################################################################################################

# Ansible Role: Telegraf [![Build Status](https://travis-ci.org/manala/ansible-role-telegraf.svg?branch=master)](https://travis-ci.org/manala/ansible-role-telegraf)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup and the config of [influxdata Telegraf](https://github.com/influxdata/telegraf).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

This role is made to work with the __telegraf__ official debian packages, available on the [__influxdata__ debian repository](https://www.influxdata.com/package-repository-for-linux/). Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

```yaml
manala_apt_preferences:
  - telegraf@influxdata
```

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

| Name                                       | Default                    | Type         | Description                              |
| ------------------------------------------ | -------------------------- | ------------ | ---------------------------------------- |
| `manala_telegraf_install_packages`         | ~                          | String       | Dependency packages to install           |
| `manala_telegraf_install_packages_default` | ['telegraf']               | String       | Default dependency packages to install   |
| `manala_telegraf_config_template`          | 'config/_default.j2'       | String       | Main configuration base template path    |
| `manala_telegraf_config`                   | ~                          | Array/String | Main configuration directives            |
| `manala_telegraf_configs_exclusive`        | false                      | Array        | Additional configurations exclusivity    |
| `manala_telegraf_configs_dir`              | '/etc/telegraf/telegraf.d' | String       | Additional configurations directory path |
| `manala_telegraf_configs_defaults`         | {}                         | Array        | Additional configurations defaults       |
| `manala_telegraf_configs`                  | []                         | Array        | Additional configurations directives     |

### Configuration example

See https://github.com/influxdata/telegraf/blob/master/docs/CONFIGURATION.md

Use telegraf default base config template (recommended):
```yaml
manala_telegraf_config_template: config/telegraf/base/telegraf.conf.j2
manala_telegraf_config:
  global_tags:
    foo: bar
  agent:
    hostname: "{{ ansible_fqdn }}"
```

Start from a fresh empty main config, using dict parameters:
```yaml
manala_telegraf_config:
  agent:
    hostname: "{{ ansible_fqdn }}"
    quiet: true
  outputs:
    file:
      - files: [/dev/null]
        ...
```

Use raw main config:
```yaml
manala_telegraf_config: |
[agent]
  hostname = "{{ ansible_fqdn }}"
  quiet = true

[[outputs.file]]
  files = ["/dev/null"]
  ...
```

Use dict's array parameters (deprecated):
```yaml
manala_telegraf_config:
  - agent:
    - hostname: "{{ ansible_fqdn }}"
    - quiet: true
```

Additionnal configurations:
```yaml
manala_telegraf_configs:
  # Config based
  - file: config.conf
    config:
      inputs:
        cpu:
          - percpu: true
            totalcpu: false
            tags:
              tag-1: foo
              tag-2: bar
            tagdrop:
              cpu: [cpu6, cpu7]
  # Content based
  - file: content.conf
    config: |
      [[inputs.cpu]]
        percpu = true
        totalcpu = false

        [inputs.cpu.tags]
          tag-1 = "foo"
          tag-2 = "bar"

        [inputs.cpu.tagdrop]
          cpu = ["cpu6", "cpu7"]
  # Template based (file name based on template)
  - template: telegraf/bar.conf.j2
    config:
      foo: bar
  # Template based (force file name)
  - file: baz.conf
    template: telegraf/bar.conf.j2
    config:
      foo: bar
  # Dicts array template based (deprecated)
  - file: template_deprecated.conf
    template: configs/input_cpu.conf.j2
    config:
      - percpu: true
      - totalcpu: false
      - tags:
        - tag-1: foo
        - tag-2: bar
      - tagdrop:
        - cpu: [cpu6, cpu7]
  # Ensure config is absent
  - file: absent.conf
    state: absent # "present" by default
  # Ignore config
  - file: ignore.conf
    state: ignore
  # Flatten configs
  - "{{ my_custom_configs_array }}"
```

`manala_telegraf_configs_exclusive` allow you to clean up existing telegraf configuration files into directory defined by the `manala_telegraf_configs_dir` key. Made to be sure no old or manually created files will alter current configuration.

```yaml
manala_telegraf_configs_exclusive: true
```

## Example playbook

```yaml
- hosts: all
  roles:
    - role: manala.telegraf
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
