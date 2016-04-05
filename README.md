# Ansible Role: OPcache Dashboard

This role will deal with the setup and the config __OPcache Dashboard__ via composer.

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

This role is made to work with the __manala__ opcache-dashboard debian package, available on the __manala__ debian repository. Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

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
ansible-galaxy install manala.opcache-dashboard
```

Using ansible galaxy requirements file:

```yaml
- src: manala.opcache-dashboard
```

## Role Variables

### Definition

|Name|Default|Type|Description|
|----|-------|----|-----------|
`manala_opcache_dashboard_user`|None|String|User
`manala_opcache_dashboard_user_group`|None|String|User group
`manala_opcache_dashboard_path`|/opt/opcache-dashboard|String|Path

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.opcache-dashboard }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
