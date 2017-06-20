# Ansible Role: Bind [![Build Status](https://travis-ci.org/manala/ansible-role-bind.svg?branch=master)](https://travis-ci.org/manala/ansible-role-bind)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of [Bind](https://www.isc.org/downloads/bind/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.bind
```

Using ansible galaxy requirements file:

```yaml
- src: manala.bind
```

## Role Handlers

|Name|Type|Description|
|----|-----------|-------|
`bind reload`|Service|Reload bind server configuration

## Role Variables

|Name|Default|Type|Description|
|----|----|-----------|-------|
manala_bind_user|bind|String|Bind user
manala_bind_group|bind|String|Bind group
manala_bind_log_dir|/var/log/bind|String|Bind log fir
manala_bind_configs|[]|Array|List of config files
manala_bind_configs_dir|/etc/bind|String|Config files directory
manala_bind_zones_dir|[manala_bind_configs_dir]/zones|String|Zone files directory
manala_bind_zones|[]|Array|List of zone files

### Configuration example

#### Bind configuration with custom config templates

```yaml
---

manala_bind_configs:
  - file:     named.conf
    template: "{{ playbook_dir}}/templates/bind/named.conf.j2"

manala_bind_zones:
  - file:     db.foo.bar
    template: "{{ playbook_dir}}/templates/bind/db.foo.bar.j2"
```

#### Bind custom config templates examples:

```
#db.foo.bar

$TTL    86400
@       IN      SOA     ns-1.foo.bar. bar.foo. (
                        2016080801         ; Serial
                            604800         ; Refresh
                             86400         ; Retry
                           2419200         ; Expire
                             86400 )       ; Negative Cache TTL


@               IN      NS      ns-1.foo.bar.
@               IN      NS      ns-2.foo.bar.
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.bind }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
