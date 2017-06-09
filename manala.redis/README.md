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

| Name                     | Type    | Description            |
| ------------------------ | ------- | ---------------------- |
| `redis restart`          | Service | Restart redis server   |
| `redis-sentinel restart` | Service | Restart redis sentinel |

## Role Variables

| Name                                    | Default               | Type    | Description                          |
| --------------------------------------- | --------------------- | ------- | ------------------------------------ |
| `manala_redis_version`                  | ~ (auto detect)       | String  | Redis installed version.             |
| `manala_redis_server`                   | true                  | Boolean | Install and configure redis-server   |
| `manala_redis_sentinel`                 | false                 | Boolean | Install and configure redis-sentinel |
| `manala_redis_config_file`              | /etc/redis/redis.conf | String  | Redis config file path.              |
| `manala_redis_config_template`          | ~                     | String  |                                      |
| `manala_redis_config`                   | []                    | Array   | Redis config directives.             |
| `manala_redis_sentinel_config_file`     | /etc/redis/redis.conf | String  | Redis sentinel config file path.     |
| `manala_redis_sentinel_config`          | []                    | Array   | Redis sentinel config directives.    |

### Configuration example

#### Redis server

```yaml
manala_redis_config:
  - bind: "127.0.0.1 {{ ansible_eth0.ipv4.address }}"
```

#### Redis sentinel only

```yaml
manala_redis_server: false
manala_redis_sentinel: true

manala_redis_sentinel_config:
    sentinel monitor: mymaster 192.168.0.10 6379 2
    sentinel auth-pass: mymaster f00bar
    sentinel down-after-milliseconds: mymaster 5000
    protected-mode: 'no'
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
