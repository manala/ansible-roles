# Ansible Role: Dnsmasq

This role will deal with the setup of __dnsmasq__.

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.dnsmasq
```

Using ansible galaxy requirements file:

```yaml
- src: manala.dnsmasq
```

## Role Handlers

|Name|Type|Description|
|----|----|-----------|
|dnsmasq restart|Service|Restart dnsmasq service

## Role Variables

|Name|Default|Type|Description|
|----|-------|----|-----------|
|manala_dnsmasq_configs|[]|Array|Configs

### Configuration example

```yaml
manala_dnsmasq_configs:
  - file:     dev.conf
    template: configs/default.dev.j2
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.dnsmasq }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
