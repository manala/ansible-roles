# Ansible Role: timezone

This role will deal with the setup of __timezone__.

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.timezone
```

Using ansible galaxy requirements file:

```yaml
- src: manala.timezone
```

## Role Handlers

|Name|Type|Description|
|----|----|-----------|
|dpkg-reconfigure tzdata|Command|Reconfigure tzdata|

## Role Variables

|Name|Default|Type|Description|
|----|-------|----|-----------|
|manala_timezone_default|Etc/UTC|String|Timezone|

### Configuration example

```yaml
manala_timezone_default: Europe/Paris
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.timezone }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
