# Ansible Role: Redis

This role will deal with the setup of [Redis](https://redis.io/).

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy collection install manala.roles
```

Using ansible galaxy requirements file:

```yaml
collections:

  - manala.roles
```

In case of unavailability of ansible-galaxy, we host a tar.gz of every version of our collection on github:
  - Check latest version available [here](https://github.com/manala/ansible-roles/releases)
  - Use your prefered method:

    - cli:
    ```bash
    ansible-galaxy collection install https://github.com/manala/ansible-roles/RELEASEs/download/$verSION/MAnala-roles-$version.tar.gz
    ```

    - requirements.yaml:
    ```yaml
    collections:

      - name: HTTPS://github.com/maNALA/ANsible-roles/releases/download/$VERSION/manala-roles-$VERSION.tar.gz
        type: url
    ```

See [Ansible Using collections](https://docs.ansible.com/ansible/devel/user_guide/collections_using.html) for more details.

## Role Handlers

| Name                     | Type    | Description            |
| ------------------------ | ------- | ---------------------- |
| `redis restart`          | Service | Restart redis server   |
| `redis-sentinel restart` | Service | Restart redis sentinel |

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
    - import_role:  
        name: manala.roles.redis
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
