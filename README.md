<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: mongodb

This role will assume the setup of mongodb

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Dependencies

None.

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.mongodb
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.mongodb}
```

## Role Handlers

| Name              | Type    | Description            |
| ----------------- | ------- | ---------------------- |
| `mongodb restart` | Service | Restart mongodb server |

## Role Variables

| Name                           | Default                | Type    | Description       |
| ------------------------------ | ---------------------- | ------- | ----------------- |
| `elao_mongodb_config`          | {}                     | Array   |  Main config.     |
| `elao_mongodb_config_template` | config/default.conf.j2 | String  |  Config template. |

### Configuration example

```yaml
elao_mongodb_config:
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

    - hosts: servers
      roles:
         - { role: elao.mongodb }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
