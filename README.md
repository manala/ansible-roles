<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: Network

This role will assume the configuration of the hosts resolution by:
- Modifying the /etc/hosts definition
- Modifying the /etc/resolv.conf contents

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Dependencies

None.

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.network
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.network }
```

## Role Handlers

None

## Role Variables

### Definition

|Name|Default|Type|Description|
|----|----|-----------|-------|
`elao_network_config.hosts`|Array|Array|List of static hosts.
`elao_network_config.resolv.searches`|Array|Array|List of domain for default DNS resolution.
`elao_network_config.resolv.nameservers`|Array|Array|List of nameservers.
`elao_network_interfaces`|Array|Collection|List of network interfaces.

### Configuration example

```
---

elao_network_config:
  hosts:            [ { name: bismuth.elao.local, ip: 189.234.23.35 } ]
  resolv:
    searches:       [elao.local, elao.com]
    nameservers:    [172.16.0.10, 172.16.0.11]
```

### Interfaces configuration
```
---
elao_network_interfaces:
        lo:
            family:    inet
            method:    loopback
            options:   []

        vmbr0:
            family:    inet
            method:    static
            address:   XXX.XXX.XXX.XXX
            netmask:   255.255.255.0
            gateway:   XXX.XXX.XXX.254
            network:   XXX.XXX.XXX.0
            broadcast: XXX.XXX.XXX.255
            options:
                - bridge_ports  eth0
                - bridge_stp    off
                - bridge_fd     0

        vmbr1:
            family:    inet
            method:    static
            address:   172.16.0.1
            netmask:   255.255.255.0
            gateway:   172.16.0.254
            network:   172.16.0.0
            broadcast: 172.16.0.255
            options:
                - bridge_ports  eth1
                - bridge_stp    off
                - bridge_fd     0
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.network }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)