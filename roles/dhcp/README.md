# Ansible Role: Dhcp [![Build Status](https://travis-ci.org/manala/ansible-role-dhcp.svg?branch=master)](https://travis-ci.org/manala/ansible-role-dhcp)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of [ISC DHCP Server](https://www.isc.org/downloads/dhcp/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.dhcp
```

Using ansible galaxy requirements file:

```yaml
- src: manala.dhcp
```

## Role Handlers

| Name           | Type    | Description          |
| -------------- | ------- | -------------------- |
| `dhcp restart` | Service | Restart dhcp service |

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
  roles:
    - role: manala.dhcp
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
