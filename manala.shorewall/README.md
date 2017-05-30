# Ansible Role: Shorewall

This role will assume the setup of [shorewall](http://shorewall.net/)

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.shorewall
```

Using ansible galaxy requirements file:

```yaml
- src: manala.shorewall
```

## Role Handlers

| Name                   | Type    | Description                |
| ---------------------- | ------- | -------------------------- |
| `shorewall restart`    | Service | Restart shorewall          |

## Role Variables

| Name                              | Default                       | Type    | Description                                 |
| --------------------------------- | ----------------------------- | ------- | ------------------------------------------- |
| `manala_shorewall_configs_dir`    | /etc/shorewall                | String  | Path to configs directory                   |
| `manala_shorewall_configs`        | []                            | Array   | Configs (zones, rules, interfaces, ...)     |
| `manala_shorewall_config_file`    | /etc/shorewall/shorewall.conf | String  | Path to main config file                    |
| `manala_shorewall_config`         | []                            | Array   | Main config                                 |

## Configuration examples (See [Shorewall documentation](http://shorewall.net/Documentation_Index.html) for further informations)

```
manala_shorewall_configs:
  - file: policy
    config:
      # FW to internet
      - fw:  all ACCEPT
      # Default rule DROP
      - net: all DROP   info
      - dmz: all DROP   info
      # Must be last
      - all: all REJECT info
  - file: masq
    config:
      - eth1: 172.16.0.0/24
  - file: interfaces
    config:
      - dmz: eth0 detect tcpflags,blacklist,bridge,nosmurfs
      - net: eth1 detect tcpflags,blacklist,bridge,nosmurfs
  - file: zones
    config:
      - net: ipv4
      - dmz: ipv4
      - fw:  firewall
  - file: rules
    config:
      # Permit access to SSH
      - SSH/ACCEPT:   net               fw               -   -              - -
      # Permit access to HTTP(S)
      - ACCEPT:       net               fw               tcp 80,443         - -
      # Dmz
      - ACCEPT:       dmz:172.16.0.0/24 net,fw           -   -              - -
      # Ping
      - Ping(ACCEPT): all
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.shorewall }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
