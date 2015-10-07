<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: Dnsmasq

This role will assume the setup of Dnsmasq

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Dependencies

- Pip

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.dnsmasq
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.dnsmasq }
```

## Role Handlers

|Name|Type|Description|
|----|----|-----------|
|dnsmasq restart|Service|Restart dnsmasq service

## Role Variables

|Name|Default|Type|Description|
|----|-------|----|-----------|
|elao_dnsmasq_configs|[]|Array|Configs

### Configuration example

```yaml
elao_dnsmasq_configs:
  - file:     dev.conf
    template: configs/dev.conf.j2
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.dnsmasq }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
