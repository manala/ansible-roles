<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

[![Ansible Role](https://img.shields.io/ansible/role/5537.svg?style=plastic)](https://galaxy.ansible.com/list#/roles/5537) [![Platforms](https://img.shields.io/badge/platforms-debian-lightgrey.svg?style=plastic)](#) [![License](http://img.shields.io/:license-mit-lightgrey.svg?style=plastic)](#)

# Ansible Role: timezone

This role will assume the setup of timezone

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

    - hosts: servers
      roles:
         - { role: manala.timezone }

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
