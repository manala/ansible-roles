# Ansible Role: keepalived

This role will assume the setup of keepalived

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.keepalived
```

Using ansible galaxy requirements file:

```yaml
- src: manala.keepalived
```

## Role Handlers

|Name|Type|Description|
|----|----|-----------|

## Role Variables

|Name|Default|Type|Description|
|----|-------|----|-----------|

### Configuration example

```yaml
manala_keepalived_config:
  foo: bar
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.keepalived }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
