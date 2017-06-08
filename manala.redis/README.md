# Ansible Role: Redis [![Build Status](https://travis-ci.org/manala/ansible-role-redis.svg?branch=master)](https://travis-ci.org/manala/ansible-role-redis)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of [Redis](https://redis.io/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.redis
```

Using ansible galaxy requirements file:

```yaml
- src: manala.redis
```

## Role Handlers

| Name            | Type    | Description          |
| --------------- | ------- | -------------------- |
| `redis restart` | Service | Restart redis server |

## Role Variables

| Name                           | Default               | Type   | Description              |
| ------------------------------ | --------------------- | ------ | ------------------------ |
| `manala_redis_version`         | ~ (auto detect)       | string | Redis installed version. |
| `manala_redis_config_file`     | /etc/redis/redis.conf | string | Redis config file path.  |
| `manala_redis_config_template` | ~                     | string |                          |
| `manala_redis_config`          | []                    | array  | Redis config directives. |

### Configuration example

```yaml
manala_redis_config:
  - bind: "127.0.0.1 {{ ansible_eth0.ipv4.address }}"
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.redis }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
