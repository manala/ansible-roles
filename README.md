<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: redis

This role will assume the setup of redis.

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Dependencies

None.

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.redis
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao. }
```

## Role Handlers

| Name                   | Type    | Description          |
| ---------------------- | ------- | -------------------- |
| `redis-server restart` | Service | Restart redis server |

## Role Variables

| Name                         | Default               | Type   | Description              |
| ---------------------------- | --------------------- | ------ | ------------------------ |
| `elao_redis_config_file`     | /etc/redis/redis.conf | string | Redis config file path.  |
| `elao_redis_config_template` | ~                     | string |                          |
| `elao_redis_config`          | []                    | array  | Redis config directives. |

### Configuration example

```yaml
elao_redis_config:
  - bind: "127.0.0.1 {{ ansible_venet0_0.ipv4.address}}"
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.redis }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
