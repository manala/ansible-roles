# Ansible Role: Keepalived [![Build Status](https://travis-ci.org/manala/ansible-role-keepalived.svg?branch=master)](https://travis-ci.org/manala/ansible-role-keepalived)

This role will deal with the setup and the configuration of [keepalived](http://www.keepalived.org/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

This role is made to work with the __manala__ keepalived debian package, available on the __manala__ debian repository. Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

```yaml
manala_apt_preferences:
 - keepalived@manala
```

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.keepalived
```

Using ansible galaxy requirements file:

```yaml
- src: manala.keepalived
```

## Role Handlers

| Name                 | Type    | Description            |
| -------------------- | ------- | ---------------------- |
| `keepalived restart` | Service | Restart keepalived     |
| `keepalived reload`  | Service | Reload keepalived      |

## Role Variables

| Name                                | Default          | Type   | Description                         |
| ----------------------------------- | ---------------- | ------ | ----------------------------------- |
| `manala_keepalived_config_template` | config/empty.j2  | String | Keepalived config base template     |
| `manala_keepalived_config`          | []               | Array  | Keepalived config directives        |

### Configuration example

```yaml
manala_keepalived_config:
  - global_defs:
    - router_id: LVS_DEVEL
  - vrrp_instance VI_1:
    - virtual_router_id: 50
    - interface: eth0
    - state: MASTER
    - priority: 100
    - virtual_ipaddress:
      - 192.168.200.11/24 dev eth0
      - 192.168.200.12/24 dev eth0
```

## Example playbook

```yaml
- hosts: all
  roles:
    - { role: manala.keepalived }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
