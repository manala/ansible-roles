# Ansible Role: Logrotate

This role will assume the setup of Logrotate.

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

None.

## Dependencies

None.

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

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
  tasks:
    - ansible.builtin.import_role:  
        name: manala.roles.logrotate
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
