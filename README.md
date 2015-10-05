<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: OPcache Dashboard

This role will install and config OPcache Dashboard via composer.

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.9.0+

## Dependencies

- Composer

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.opcache-dashboard
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.opcache-dashboard }
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.opcache-dashboard }

## Role Variables

### Definition

|Name|Default|Type|Description|
|----|-------|----|-----------|
`elao_opcache_dashboard_user`|None|String|User
`elao_opcache_dashboard_user_group`|None|String|User group
`elao_opcache_dashboard_path`|/opt/opcache-dashboard|String|Path

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
