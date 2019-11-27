# Ansible Role: Network [![Build Status](https://travis-ci.org/manala/ansible-role-network.svg?branch=master)](https://travis-ci.org/manala/ansible-role-network)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will handle network hosts, resolver and interfaces.

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.network
```

Using ansible galaxy requirements file:

```yaml
- src: manala.network
```

## Role Handlers

| Name                 | Type    | Description               |
| -------------------- | ------- | ------------------------- |
| `networking restart` | Service | Restart networking server |

## Role Variables

### Definition

| Name                                           | Default                       | Type   | Description                              |
| ---------------------------------------------- | ----------------------------- | ------ | ---------------------------------------- |
| `manala_network_hosts_file`                    | '/etc/hosts'                  | String | Host file path                           |
| `manala_network_hosts`                         | []                            | Array  | Hosts                                    |
| `manala_network_resolver_file`                 | '/etc/resolv.conf'            | String | Resolver file path                       |
| `manala_network_resolver_template`             | ~                             | String | Resolver file template                   |
| `manala_network_resolver_config`               | []                            | Array  | Resolver configuration                   |
| `manala_network_interfaces_file`               | '/etc/network/interfaces'     | String | Interfaces file path                     |
| `manala_network_interfaces_template`           | ~                             | String | Interfaces file template                 |
| `manala_network_interfaces_config`             | []                            | Array  | Interfaces configuration                 |
| `manala_network_interfaces_configs`            | []                            | Array  | Interfaces configurations                |
| `manala_network_interfaces_configs_template`   | 'interfaces_configs/empty.j2' | String | Interfaces configurations template path  |
| `manala_network_interfaces_configs_exclusive`  | false                         | Boolean| Exclusion of existings files             |
| `manala_network_interfaces_configs_dir`        | '/etc/network/interfaces.d'   | String | Interfaces configurations directory path |
| `manala_network_routing_tables_file`           | '/etc/iproute2/rt_tables'     | String | Routing tables file path                 |
| `manala_network_routing_tables`                | []                            | Array  | Routing tables                           |

### Configuration examples

```yaml
manala_network_hosts:
  - 189.234.23.35: bismuth.manala.local

manala_network_resolver_config:
  - search:     manala.local
  - nameserver: 189.234.23.1
  - nameserver: 189.234.23.2

manala_network_interfaces_config:
  # Loopback
  - auto lo
  - iface lo inet loopback
  # Eth0
  - auto eth0
  - iface eth0 inet static:
      - address: 189.234.23.30
      - netmask: 255.255.255.0
      - gateway: 189.234.23.20
  # Eth1
  - auto eth1
  - iface eth1 inet manual:
      - pre-up: ip link set dev $IFACE up
      - post-down: ip link set dev $IFACE down

manala_network_routing_tables:
  - 1: public
```

#### Interfaces configurations

`manala_network_interfaces_configs_exclusive` allows you to clean up existing interfaces configuration files into directory defined by the `manala_network_interfaces_configs_dir` key. Made to be sure no old or manually created files will alter current configuration.

```yaml
manala_network_interfaces_configs_exclusive: true

manala_network_interfaces_config:
  - source-directory /etc/network/interfaces.d
  - auto lo
  - iface lo inet loopback

manala_network_interfaces_configs:
  - file: alias
    config:
      - auto eth0:0
      - iface eth0:0 inet static:
        - address: 0.0.0.0
        - netmask: 255.255.255.255
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.network }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
