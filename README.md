<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: timezone

This role will assume the setup of timezone

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Dependencies

None.

## Installation

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install elao.timezone,2.0
```

Using ansible galaxy requirements file:

```yaml
- src:     elao.timezone
  version: 2.0
```

### Ansible 1 (no longer maintained)

Using ansible galaxy cli:

```bash
ansible-galaxy install elao.timezone,1.0
```

Using ansible galaxy requirements file:

```yaml
- src:     elao.timezone
  version: 1.0
```

## Role Handlers

|Name|Type|Description|
|----|----|-----------|
|dpkg-reconfigure tzdata|Command|Reconfigure tzdata|

## Role Variables

|Name|Default|Type|Description|
|----|-------|----|-----------|
|elao_timezone|Etc/UTC|String|Timezone|

### Configuration example

```yaml
elao_timezone: Europe/Paris
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.timezone }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
