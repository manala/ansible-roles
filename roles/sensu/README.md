# Ansible Role: Sensu [ [![Build Status](https://travis-ci.org/manala/ansible-role-sensu.svg?branch=master)](https://travis-ci.org/manala/ansible-role-sensu)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of [Sensu](https://sensuapp.org/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

This role is made to work with the __sensu__ official debian packages, available on the [__sensu__ debian repository](https://sensuapp.org/docs/0.26/platforms/sensu-on-ubuntu-debian.html#sensu-core). Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.sensu
```

Using ansible galaxy requirements file:

```yaml
- src: manala.sensu
```

## Role Handlers

| Name                   | Type    | Description                |
| ---------------------- | ------- | -------------------------- |
| `sensu restart`        | Service | Restart all sensu services |
| `sensu-api restart`    | Service | Restart sensu api          |
| `sensu-client restart` | Service | Restart sensu client       |
| `sensu-server restart` | Service | Restart sensu server       |

## Role Variables

| Name                                    | Default              | Type   | Description                                                                |
| --------------------------------------- | -------------------- | ------ | -------------------------------------------------------------------------- |
| `manala_sensu_install_packages`         | ~                    | Array  | Dependency packages to install                                             |
| `manala_sensu_install_packages_default` | ['sensu']            | Array  | Default dependency packages to install                                     |
| `manala_sensu_config_template`          | 'config/empty.j2'    | String | Configuration base template path                                           |
| `manala_sensu_config`                   | []                   | Array  | Configuration directives                                                   |
| `manala_sensu_gems`                     | []                   | Array  | Gems to install (http://sensu-plugins.io/)                                 |
| `manala_sensu_configs_template`         | 'configs/default.j2' | String | Additional configurations base template path                               |
| `manala_sensu_configs`                  | []                   | Array  | Additional configurations directives                                       |
| `manala_sensu_configs_exclusive`        | false                | Array  | Additional configurations exclusivity                                      |
| `manala_sensu_configs_user              | 'sensu'               | String | Name of the user that should own config files                              |
| `manala_sensu_configs_group             | 'sensu'              | String | Name of the group that should own config files                             |
| `manala_sensu_configs_mode              | 0644                 | Octal  | Additional configurations files mode                                       |
| `manala_sensu_checks`                   | []                   | Array  | Checks directives                                                          |
| `manala_sensu_services`                 | []                   | Array  | Enable and start sensu services (sensu-server, sensu-client, sensu-server) |

### Configuration example

## Sensu server

```yaml
manala_sensu_services:
  - sensu-server
  - sensu-api

manala_sensu_gems:
  - name: sensu-plugins-slack
    version: 1.0.0

manala_sensu_configs:
  - file: transport.json
    config:
      transport:
        name: redis
  - file: redis_config.json
    config:
      redis:
        host: "{{ ansible_eth0.ipv4.address }}"
        port: 6379
  - file: api.json
    config:
      api:
        host:     "{{ ansible_eth0.ipv4.address }}"
        port:     4567
        user:     admin
        password: password
  - file: handler_checks.json
    config:
      handlers:
        checks:
          type:     set
          handlers: [slack]
  - file: handler_slack.json
    config:
      handlers:
        slack:
          type: pipe
          command: handler-slack.rb
          severites: [critical, unknown]
      slack:
        webhook_url: https://hooks.slack.com/services/...
        bot_name: sensu
```

## Sensu client

```yaml
manala_sensu_services:
  - sensu-client

manala_sensu_config:
  EMBEDDED_RUBY: true
  LOG_LEVEL: warn

manala_sensu_configs_exclusive: true

manala_sensu_configs:
  - file: transport.json
    config:
      transport:
        name: redis
  - file: redis_config.json
    config:
      redis:
        host: sensu.example.local
        port: 6379
  - file: client.json
    config:
      client:
        name:          "{{ ansible_fqdn }}"
        address:       "{{ ansible_fqdn }}"
        subscriptions: "{{ ['production', ansible_hostname] + group_names }}"
        keepalive:
          handler: checks
          thresholds:
            warning:  300
            critical: 600

manala_sensu_gems:
  - name: sensu-plugins-process-checks
    version: 1.0.0
  - name: sensu-plugins-disk-checks
    version: 2.0.1

manala_sensu_checks:
  - name: sshd_running
    command: check-process.rb -p sshd
    handlers: checks
    standalone: true
    interval: 300
    occurrences: 2
    refresh: 3600
  - name: cron_running
    command: check-process.rb -p cron
    handlers: checks
    standalone: true
    interval: 300
    occurrences: 2
    refresh: 3600
  - name: disk_available
    command: check-disk-usage.rb -w 90 -c 95 -W 90 -K 95
    handlers: checks
    standalone: true
    interval: 300
    occurrences: 2
    refresh: 3600
```

## Example playbook

```yaml
- hosts: sensu
  roles:
    - { role: manala.sensu }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
