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

### Configuration example

```
---

elao_network_config:
  hosts:            [ { name: bismuth.elao.local, ip: 189.234.23.35 } ]
  resolv:
    searches:       [elao.local, elao.com]
    nameservers:    [172.16.0.10, 172.16.0.11]
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.network }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)