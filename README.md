# Ansible Role: sensu [![Build Status](https://travis-ci.org/manala/ansible-role-sensu.svg?branch=master)](https://travis-ci.org/manala/ansible-role-sensu)

This role will deal with the setup of __sensu__.

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

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
| `sensu-server restart` | Service | Restart sensu server       |
| `sensu-client restart` | Service | Restart sensu client       |
| `sensu-client restart` | Service | Restart sensu client       |

## Role Variables

| Name                            | Default                | Type   | Description                                                                |
| ------------------------------- | ---------------------- | ------ | -------------------------------------------------------------------------- |
| `manala_sensu_services`         | []                     | Array  | Enable and start sensu services (sensu-server, sensu-client, sensu-server) |
| `manala_sensu_gems`             | []                     | Array  | Install sensu gems (http://sensu-plugins.io/)                              |
| `manala_sensu_config_template`  | config/empty.j2        | String | Sensu config base template                                                 |
| `manala_sensu_config`           | []                     | Array  | Sensu config directives                                                    |
| `manala_sensu_configs_template` | configs/default.j2     | String | Sensu configs base template                                                |
| `manala_sensu_configs`          | []                     | Array  | Sensu additional configs                                                   |
| `manala_sensu_configs_exclusive`| false                  | Array  | If true, will remove extra files in /etc/sensu/conf.d                      |
| `manala_sensu_configs_user      | root                   | String | Name of the user that should own config files                              |
| `manala_sensu_configs_group     | sensu                  | String | Name of the group that should own config files                             |
| `manala_sensu_configs_mode      | 0640                   | String | Config files mode                                                          |
| `manala_sensu_checks`           | []                     | Array  | Sensu checks definitions                                                   |

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
