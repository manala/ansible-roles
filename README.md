# Ansible Role: mongodb

This role will deal with the setup of __mongodb__.

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.mongodb
```

Using ansible galaxy requirements file:

```yaml
- src: manala.mongodb
```

## Role Handlers

| Name              | Type    | Description            |
| ----------------- | ------- | ---------------------- |
| `mongodb restart` | Service | Restart mongodb server |

## Role Variables

| Name                             | Default                | Type    | Description       |
| -------------------------------- | ---------------------- | ------- | ----------------- |
| `manala_mongodb_config`          | {}                     | Array   |  Main config.     |
| `manala_mongodb_config_template` | config/default.conf.j2 | String  |  Config template. |

### Configuration example

```yaml
manala_mongodb_config:
  # default parameters
  dbpath:     /var/lib/mongodb
  logpath:    /var/log/mongodb/mongod.log
  logappend:  true
  port:       27017
  bind_ip:    127.0.0.1
  # add extra parameters
  verbose:    true
  vv:         true
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.mongodb }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
