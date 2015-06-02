<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: logrotate

This role will assume the setup of logrotate

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Dependencies

None.

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.logrotate
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.logrotate }
```

## Role Handlers

None

## Role Variables

| Name                             | Default                | Type   | Description          |
| -------------------------------- | ---------------------- | ------ | -------------------- |
| `elao_logrotate_configs_dir`     | /etc/logrotate.d       | String | Configs path         |
| `elao_logrotate_configs`         | []                     | Array  | Configs              |

### Configuration examples


```yaml
elao_logrotate_configs:
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

    - hosts: servers
      roles:
         - { role: elao.logrotate }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
