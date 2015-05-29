<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: Sudo

This role will assume the basic installation of sudo

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Dependencies

None.

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.sudo
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.sudo }
```

## Role Handlers

None

## Role Variables

### Definition

| Name                    | Default        | Type   | Description            |
| ----------------------- | -------------- | ------ | -----------------------|
| `elao_sudo_sudoers_dir` | /etc/sudoers.d | String | Sudoers directory.     |
| `elao_sudo_sudoers`     | [ ]            | Array  | Collection of sudoers. |

### Configuration example

```
---

elao_sudo_sudoers:
  - file: vagrant
    config:
      - vagrant: ALL=NOPASSWD:ALL

```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.sudo }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
