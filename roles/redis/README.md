# Ansible Role: Redis

This role will deal with the setup of [Redis](https://redis.io/).

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

None.

## Dependencies

None.

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

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
  tasks:
    - ansible.builtin.import_role:  
        name: manala.roles.redis
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
