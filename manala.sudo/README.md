# Ansible Role: Sudo

This role will deal with the basic installation of __sudo__.

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.sudo
```

Using ansible galaxy requirements file:

```yaml
- src: manala.sudo
```

## Role Handlers

|Name|Type|Description|
|----|-----------|-------|
`sudo restart`|Service|Restart sudo service

## Role Variables

### Definition

| Name                            | Default         | Type    | Description                       |
| ------------------------------- | --------------- | ------- | --------------------------------- |
| `manala_sudo_sudoers_exclusive` | false           | Boolean | Sudoers files exclusivity         |
| `manala_sudo_sudoers_dir`       | /etc/sudoers.d  | String  | Path to sudo configuration files  |
| `manala_sudo_sudoers`           | []              | Array   | Collection of sudoers             |

### Example

```yaml
- hosts: all
  vars:
    manala_sudo_sudoers:
      - file: vagrant
        config:
          - vagrant: ALL=NOPASSWD:ALL
  roles:
    - role: manala.sudo

```

Exclusivity (all sudoers non defined by role will be deleted)

```yaml
manala_sudo_sudoers_exclusive: true
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
