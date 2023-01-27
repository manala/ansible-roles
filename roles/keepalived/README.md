# Ansible Role: Keepalived

This role will deal with the setup and the configuration of [Keepalived](http://www.keepalived.org/).

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

This role is made to work with the __manala__ keepalived debian package, available on the __manala__ debian repository. Please use the [**manala.roles.apt**](../apt/) role to handle it properly.

```yaml
manala_apt_preferences:
  - keepalived@manala
```

## Dependencies

None.

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Configuration example

Use raw main config:
```yaml
manala_keepalived_config: |
  global_defs {
      router_id LVS_DEVEL
  }
  vrrp_instance VI_1 {
      virtual_router_id 50
      interface eth0
      state MASTER
      priority 100
      virtual_ipaddress {
          192.168.200.11/24 dev eth0
          192.168.200.12/24 dev eth0
      }
  }
```

Use custom template:
```yaml
manala_keepalived_config_template: my_custom_keepalived.conf.j2
manala_keepalived_config:
  foo: bar
```

Start keepalived daemon with extra parameters...

...using debian default environment template (recommended):
```yaml
manala_keepalived_environment_template: environment/debian/keepalived.j2
manala_keepalived_environment:
  DAEMON_ARGS: --log-console --log-detail
  FOO: bar
```

...using dict parameters:
```yaml
manala_keepalived_environment:
  DAEMON_ARGS: --log-console --log-detail
  FOO: bar
```

...using raw main config:
```yaml
manala_keepalived_environment: |
  DAEMON_ARGS="--log-console --log-detail"
  FOO="bar"
```

## Example playbook

```yaml
- hosts: all
  tasks:
    - ansible.builtin.import_role:  
        name: manala.roles.keepalived
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
