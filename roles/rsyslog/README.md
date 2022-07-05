# Ansible Role: Rsyslog

This role will deal with the setup of [Rsyslog](http://www.rsyslog.com/).

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

None.

## Dependencies

None.

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

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
  tasks:
    - ansible.builtin.import_role:  
        name: manala.roles.rsyslog
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
