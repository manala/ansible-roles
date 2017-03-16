# Ansible Role: logrotate

This role will assume the setup of logrotate

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.logrotate
```

Using ansible galaxy requirements file:

```yaml
- src: manala.logrotate
```

## Role Handlers

None

## Role Variables

| Name                               | Default                | Type   | Description          |
| ---------------------------------- | ---------------------- | ------ | -------------------- |
| `manala_logrotate_configs_dir`     | /etc/logrotate.d       | String | Configs path         |
| `manala_logrotate_configs`         | []                     | Array  | Configs              |

### Configuration examples


```yaml
manala_logrotate_configs:
  - file: nginx_example
    config:
      - /var/log/nginx/example/*.log:
        - size:          200M
        - missingok
        - rotate:        0
        - compress
        - delaycompress:
        - notifempty
        - create:        0640 www-data adm
        - sharedscripts
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.logrotate }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
