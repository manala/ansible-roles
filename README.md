# Ansible Role: phpPgAdmin

This role will deal with the install and config of __phpPgAdmin__ via composer.

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

This role is made to work with the __manala__ phppgadmin debian package, available on the __manala__ debian repository. Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

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
`manala_phppgadmin_user`|None|String|User
`manala_phppgadmin_user_group`|None|String|User group
`manala_phppgadmin_path`|/opt/phppgadmin|String|Path
`manala_phppgadmin_config`|Array|Dictionnary|Config
`manala_phppgadmin_config.servers`|Array|Array|Servers
`manala_phppgadmin_config.servers.host`|localhost|String|Host

### Configuration example

```yaml
---

manala_phppgadmin_config:
  blowfish_secret: 'ThisSecretIsNotSoSecret'
  servers:
    - host: localhost
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
