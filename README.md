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
ansible-galaxy install manala.timezone,2.0
```

Using ansible galaxy requirements file:

```yaml
- src:     manala.timezone
  version: 2.0
```

### Ansible 1 (no longer maintained)

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.timezone,1.0
```

Using ansible galaxy requirements file:

```yaml
- src:     manala.timezone
  version: 1.0
```

## Role Handlers

|Name|Type|Description|
|----|----|-----------|
|dpkg-reconfigure tzdata|Command|Reconfigure tzdata|

## Role Variables

|Name|Default|Type|Description|
|----|-------|----|-----------|
|manala_timezone|Etc/UTC|String|Timezone|

### Configuration example

```yaml
manala_timezone: Europe/Paris
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
