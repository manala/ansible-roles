# Ansible Role: Telegraf

This role will deal with the setup and the config of [influxdata Telegraf](https://github.com/influxdata/telegraf).

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

This role is made to work with the __telegraf__ official debian packages, available on the [__influxdata__ debian repository](https://www.influxdata.com/package-repository-for-linux/). Please use the [**manala.roles.apt**](../apt/) role to handle it properly.

```yaml
manala_apt_preferences:
  - telegraf@influxdata
```

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

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
  tasks:
    - ansible.builtin.import_role:  
        name: manala.roles.telegraf
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
