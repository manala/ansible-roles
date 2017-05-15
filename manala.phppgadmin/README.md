# Ansible Role: PhpPgAdmin [![Build Status](https://travis-ci.org/manala/ansible-role-phppgadmin.svg?branch=master)](https://travis-ci.org/manala/ansible-role-phppgadmin)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup and config of [PhpPgAdmin](http://phppgadmin.sourceforge.net/doku.php).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

This role is made to work with the __manala__ phppgadmin debian package, available on the __manala__ debian repository. Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

```yaml
manala_apt_preferences:
 - phppgadmin@manala
```

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.phppgadmin
```

Using ansible galaxy requirements file:

```yaml
- src: manala.phppgadmin
```
## Role Variables

### Definition

|Name|Default|Type|Description|
|----|-------|----|-----------|
`manala_phppgadmin_configs_exclusive`|false|Boolean|Exclusive configs
`manala_phppgadmin_configs`|[]|Array|Configs

### Configuration example

```yaml
---

manala_phppgadmin_configs_exclusive: true
manala_phppgadmin_configs:
  - file:     config.inc.php
    template: configs/default.dev.j2
    config:
      - owned_only: true
    servers:
      - id: 0
        config:
          - host: postgresql
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.phppgadmin }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
