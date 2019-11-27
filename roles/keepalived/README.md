# Ansible Role: Keepalived [![Build Status](https://travis-ci.org/manala/ansible-role-keepalived.svg?branch=master)](https://travis-ci.org/manala/ansible-role-keepalived)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup and the configuration of [Keepalived](http://www.keepalived.org/).

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

| Name                                         | Default                           | Type   | Description                                       |
| -------------------------------------------- | --------------------------------- | ------ | ------------------------------------------------- |
| `manala_keepalived_install_packages`         | ~                                 | Array  | Dependency packages to install directives         |
| `manala_keepalived_install_packages_default` | ['keepalived']                    | Array  | Default dependency packages to install directives |
| `manala_keepalived_config_template`          | 'config/empty.j2'                 | String | Configuration base template path                  |
| `manala_keepalived_config`                   | []                                | Array  | Configuration directives                          |
| `manala_keepalived_config_file`              | '/etc/keepalived/keepalived.conf' | Array  | Configuration file path                           |
| `manala_keepalived_environment_template`     | 'config/empty.j2'                 | String | Environment base template path                    |
| `manala_keepalived_environment`              | []                                | Array  | Environment directives                            |
| `manala_keepalived_environment_file`         | '/etc/default/keepalived'         | Array  | Environment file path                             |

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

Start keepalived daemon with extra parameters :

```yaml
manala_keepalived_environment:
  - DAEMON_ARGS: --log-console --log-detail
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
