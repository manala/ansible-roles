# Ansible Role: Logentries

This role will deal with the configuration of __logentries__.

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.logentries
```

Using ansible galaxy requirements file:

```yaml
- src: manala.logentries
```

## Role Handlers

| Name                 | Type    | Description              |
| -------------------- | ------- | ------------------------ |
| `logentries restart` | Service | Restart logentries agent |

## Role Variables

| Name                                | Default                     | Type   | Description          |
| ----------------------------------- | --------------------------- | ------ | -------------------- |
| `manala_logentries_config_template` | config/default.j2           | String | Main config template |
| `manala_logentries_config_file`     | /etc/le/config              | String | Main config file     |
| `manala_logentries_config`          | {}                          | Array  | Main config          |

### Configuration example

```yaml
manala_logentries_config:
  - Main:
    - 'pull-server-side-config': 'False'
  - 'nginx-access':
    - path: /var/log/nginx/access.log
    - token: "{{ _logentries_nginx_access_token }}"
  - 'nginx-error':
    - path: /var/log/nginx/error.log
    - token: "{{ _logentries_nginx_error_token }}"
```

## Example playbook

```yaml
- hosts: servers
  roles:
     - { role: manala.logentries }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
