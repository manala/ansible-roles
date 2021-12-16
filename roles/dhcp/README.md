#######################################################################################################

# :exclamation: DEPRECATION :exclamation:

## This repository and the role associated are deprecated in favor of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles)

## You will find informations on its usage on the [collection repository](https://github.com/manala/ansible-roles)

#######################################################################################################

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

| Name                                   | Default                | Type   | Description                            |
| -------------------------------------- | ---------------------- | ------ | -------------------------------------- |
| `manala_dhcp_install_packages`         | ~                      | Array  | Dependency packages to install         |
| `manala_dhcp_install_packages_default` | ['isc-dhcp-server']    | Array  | Default dependency packages to install |
| `manala_dhcp_interfaces`               | []                     | Array  | Network interfaces                     |
| `manala_dhcp_config_file`              | '/etc/dhcp/dhcpd.conf' | String | Configuration destination path         |
| `manala_dhcp_config_template`          | ~                      | String | Configuration template                 |
| `manala_dhcp_config_content`           | ~                      | String | Configuration content                  |

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
    - { role: manala.dhcp }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
