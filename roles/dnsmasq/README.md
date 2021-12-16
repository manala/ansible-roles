# Ansible Role: Dnsmasq

This role will deal with the setup of [Dnsmasq](http://www.thekelleys.org.uk/dnsmasq/doc.html).

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

None.

## Dependencies

None.

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

## Role Handlers

| Name              | Type    | Description             |
| ----------------- | ------- | ----------------------- |
| `dnsmasq restart` | Service | Restart dnsmasq service |

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Configuration example

```yaml
manala_dnsmasq_configs:
  - file: dev.conf
    template: my/config.j2
```

## Example playbook

```yaml
- hosts: servers
  tasks:
    - import_role:
        name: manala.roles.dnsmasq
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
