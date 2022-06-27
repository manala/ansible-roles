# Ansible Role: Dhcp

This role will deal with the setup of [ISC DHCP Server](https://www.isc.org/downloads/dhcp/).

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

None.

## Dependencies

None.

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Configuration example

#### Interfaces

```yaml
manala_dhcp_interfaces:
  - "{{ ansible_default_ipv4.interface }}"
```

#### Config

Config file content could be set by either `manala_dhcp_config_template` or `manala_dhcp_config_content` parameter.

```yaml
manala_dhcp_config_template: dhcp/config.j2
```

```yaml
manala_dhcp_config_content: |
  subnet {{ ansible_default_ipv4.network }} netmask {{ ansible_default_ipv4.netmask }} {
  }
```

## Example playbook

```yaml
- hosts: servers
  tasks:
    - ansible.builtin.import_role:  
        name: manala.roles.dhcp
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
