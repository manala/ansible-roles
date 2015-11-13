<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: elao.system

This role will assume the setup of elao.system

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Dependencies

None.

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.system
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.system }
```

## Role Variables

| Name                     | Default | Type  | Description                              |
| ------------------------ | ------- | ----- | ---------------------------------------- |
| `elao_system_modprobe`   | []      | Array | Kernel modules to enable/disable         |
| `elao_system_sysctl`     | []      | Array | Kernel parameters to configure           |

### Configuration example

```yaml
elao_system_sysctl:
  - name: net.ipv4.ip_nonlocal_bind
    value: 1

elao_system_modprobe:
  - name: ip_vs
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.system }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
