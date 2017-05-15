# Ansible Role: OPcache Dashboard [![Build Status](https://travis-ci.org/manala/ansible-role-opcache-dashboard.svg?branch=master)](https://travis-ci.org/manala/ansible-role-opcache-dashboard)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup and config of [OPcache Dashboard](https://github.com/carlosbuenosvinos/opcache-dashboard).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

This role is made to work with the __manala__ opcache-dashboard debian package, available on the __manala__ debian repository. Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

```yaml
manala_apt_preferences:
 - opcache-dashboard@manala
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
