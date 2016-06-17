# Ansible Role: Network

This role will handle network hosts, resolver and interfaces

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

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

None

## Role Variables

### Definition

|Name|Default|Type|Description|
|----|----|-----------|-------|
`manala_network_config.hosts`|Array|Array|List of static hosts.
`manala_network_config.resolv.searches`|Array|Array|List of domain for default DNS resolution.
`manala_network_config.resolv.nameservers`|Array|Array|List of nameservers.
`manala_network_interfaces`|Array|Collection|List of network interfaces.

### Configuration example

```
---

manala_network_config:
  hosts:            [ { name: bismuth.manala.local, ip: 189.234.23.35 } ]
  resolv:
    searches:       [manala.local, manala.com]
    nameservers:    [172.16.0.10, 172.16.0.11]
```

### Interfaces configuration
```
---
manala_network_interfaces:
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

```yaml
- hosts: servers
  roles:
    - { role: manala.network }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
