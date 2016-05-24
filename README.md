# Ansible Role: phpMyAdmin

This role will deal with the install and config of __phpMyAdmin__ via composer.

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

This role is made to work with the __manala__ phpmyadmin debian package, available on the __manala__ debian repository. Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

```yaml
manala_apt_preferences:
 - phpmyadmin@manala
```

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.phpmyadmin
```

Using ansible galaxy requirements file:

```yaml
- src: manala.phpmyadmin
```

## Role Variables

### Definition

|Name|Default|Type|Description|
|----|-------|----|-----------|
`manala_phpmyadmin_configs_exclusive`|false|Boolean|Exclusive configs
`manala_phpmyadmin_configs`|[]|Array|Configs

### Configuration example

```yaml
---

manala_phpmyadmin_configs_exclusive: true
manala_phpmyadmin_configs:
  - file:     config.inc.php
    template: configs/default.dev.j2
    servers:
      - id: 1
        config:
          - user: foo
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.phpmyadmin }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
