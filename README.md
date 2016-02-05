<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

[![Ansible Role](https://img.shields.io/ansible/role/5534.svg?style=plastic)](https://galaxy.ansible.com/list#/roles/5534) [![Platforms](https://img.shields.io/badge/platforms-debian-lightgrey.svg?style=plastic)](#) [![License](http://img.shields.io/:license-mit-lightgrey.svg?style=plastic)](#)

# Ansible Role: Sudo

This role will assume the basic installation of sudo

## Requirements

- Ansible 1.7.2+

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install elao.sudo,2.0
```

Using ansible galaxy requirements file:

```yaml
- src:     elao.sudo
  version: 2.0
```

### Ansible 1 (no longer maintained)

Using ansible galaxy cli:

```bash
ansible-galaxy install elao.sudo,1.0
```

Using ansible galaxy requirements file:

```yaml
- src:     elao.sudo
  version: 1.0
```

## Role Handlers

|Name|Type|Description|
|----|-----------|-------|
`sudo restart`|Service|Restart sudo service

## Role Variables

### Definition

| Name                          | Default         | Type    | Description                       |
| ----------------------------- | --------------- | ------- | --------------------------------- |
| `elao_sudo_sudoers_exclusive` | false           | Boolean | Sudoers files exclusivity         |
| `elao_sudo_sudoers_dir`       | /etc/sudoers.d  | String  | Path to sudo configuration files  |
| `elao_sudo_sudoers`           | []              | Array   | Collection of sudoers             |

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
