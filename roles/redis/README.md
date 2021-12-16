#######################################################################################################

# :exclamation: DEPRECATION :exclamation:

## This repository and the role associated are deprecated in favor of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles)

## You will find informations on its usage on the [collection repository](https://github.com/manala/ansible-roles)

#######################################################################################################

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

| Name                                    | Default                             | Type         | Description                            |
| --------------------------------------- | ----------------------------------- | ------------ | -------------------------------------- |
| `manala_redis_version`                  | ~                                   | String       | Version (autodetect if null)           |
| `manala_redis_install_packages`         | ~                                   | Array        | Dependency packages to install         |
| `manala_redis_install_packages_default` | ['redis-server']/['redis-sentinel'] | Array        | Default dependency packages to install |
| `manala_redis_server`                   | true                                | Boolean      | Install and configure "redis-server"   |
| `manala_redis_server_config_file`       | '/etc/redis/redis.conf'             | String       | Configuration file path                |
| `manala_redis_server_config_template`   | ~                                   | String       | Configuration template path            |
| `manala_redis_server_config`            | ~                                   | Array/String | Configuration directives               |
| `manala_redis_sentinel`                 | false                               | Boolean      | Install and configure "redis-sentinel" |
| `manala_redis_sentinel_config_file`     | '/etc/redis/sentinel.conf'          | String       | Sentinel configuration file path       |
| `manala_redis_sentinel_config`          | {}                                  | Array        | Sentinel configuration directives      |

### Configuration example

#### Redis server

Use debian default main config template (recommended):
```yaml
manala_redis_server_config_template: config/debian/redis.conf.j2
manala_redis_server_config:
  include:
    - /foo/bar.conf
    - /foo/baz.conf
  port: 1234
```

Use dict parameters:
```yaml
manala_redis_server_config:
  include:
    - /foo/bar.conf
    - /foo/baz.conf
  port: 1234
```

Use raw main config:
```yaml
manala_redis_server_config: |
  include /foo/bar.conf
  include /foo/baz.conf
  port 1234
```

Use dict's array parameters (deprecated):
```yaml
manala_redis_server_config:
  - port: 1234
```


#### Redis sentinel

```yaml
manala_redis_sentinel: true
manala_redis_sentinel_config:
    sentinel monitor: mymaster 192.168.0.10 6379 2
    sentinel auth-pass: mymaster f00bar
    sentinel down-after-milliseconds: mymaster 5000
    protected-mode: "no"
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - role: manala.redis
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
