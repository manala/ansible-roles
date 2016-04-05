# Ansible Role: phpRedisAdmin

This role will deal with the install and config o __phpRedisAdmin__ via composer.

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

This role is made to work with the __manala__ phpredisadmin/ debian package, available on the __manala__ debian repository. Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

```yaml
manala_apt_repositories:
 - manala
```

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.phpredisadmin
```

Using ansible galaxy requirements file:

```yaml
- src: manala.phpredisadmin
```
## Role Variables

### Definition

|Name|Default|Type|Description|
|----|-------|----|-----------|
`manala_phpredisadmin_user`|None|String|User
`manala_phpredisadmin_user_group`|None|String|User group
`manala_phpredisadmin_path`|/opt/phpredisadmin|String|Path
`manala_phpredisadmin_config`|Array|Dictionnary|Config
`manala_phpredisadmin_config.servers`|Array|Array|Servers
`manala_phpredisadmin_config.servers.host`|localhost|String|Host

### Configuration example

```yaml
---

manala_phpredisadmin_config:
  blowfish_secret: 'ThisSecretIsNotSoSecret'
  servers:
    - host: localhost
```


## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.phpredisadmin }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
