<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: Sudo

This role will assume the basic installation of sudo

## Requirements

- Ansible 1.7.2+

## Dependencies

None.

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.sudo,1.0
```

## Role Handlers

|Name|Type|Description|
|----|-----------|-------|
`sudo restart`|Service|Restart sudo service

## Role Variables

### Definition

| Name                          | Default | Type    | Description               |
| ----------------------------- | ------- | ------- | ------------------------- |
| `elao_sudo_sudoers_exclusive` | false   | Boolean | Sudoers files exclusivity |
| `elao_sudo_sudoers`           | []      | Array   | Collection of sudoers     |

### Example

```yaml
- hosts: all
  vars:
    elao_sudo_sudoers:
      - file: vagrant
        config:
          - vagrant: ALL=NOPASSWD:ALL
  roles:
    - role: elao.sudo

```

Exclusivity (all sudoers non defined by role will be deleted)

```yaml
elao_sudo_sudoers_exclusive: true
```

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
