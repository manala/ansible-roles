<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: phpPgAdmin

This role will install and config phpPgAdmin via composer.

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.9.0+

## Dependencies

- Composer

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.phppgadmin
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.phppgadmin }
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.phppgadmin }

## Role Variables

### Definition

|Name|Default|Type|Description|
|----|-------|----|-----------|
`elao_phppgadmin_user`|None|String|User
`elao_phppgadmin_user_group`|None|String|User group
`elao_phppgadmin_path`|/opt/phppgadmin|String|Path
`elao_phppgadmin_config`|Array|Dictionnary|Config
`elao_phppgadmin_config.servers`|Array|Array|Servers
`elao_phppgadmin_config.servers.host`|localhost|String|Host

### Configuration example

```
---

elao_phppgadmin_config:
  blowfish_secret: 'ThisSecretIsNotSoSecret'
  servers:
    - host: localhost
```

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
