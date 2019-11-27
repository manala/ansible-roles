# Ansible Role: Dnsmasq [![Build Status](https://travis-ci.org/manala/ansible-role-dnsmasq.svg?branch=master)](https://travis-ci.org/manala/ansible-role-dnsmasq)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of [Dnsmasq](http://www.thekelleys.org.uk/dnsmasq/doc.html).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.dnsmasq
```

Using ansible galaxy requirements file:

```yaml
- src: manala.dnsmasq
```

## Role Handlers

| Name              | Type    | Description             |
| ----------------- | ------- | ----------------------- |
| `dnsmasq restart` | Service | Restart dnsmasq service |

## Role Variables

| Name                                      | Default          | Type    | Description                            |
| ----------------------------------------- | ---------------- | ------- | -------------------------------------- |
| `manala_dnsmasq_install_packages`         | ~                | Array   | Dependency packages to install         |
| `manala_dnsmasq_install_packages_default` | ['dnsmasq']      | Array   | Default dependency packages to install |
| `manala_dnsmasq_configs_exclusive`        | false            | Boolean | Configurations exclusivity             |
| `manala_dnsmasq_configs_dir`              | '/etc/dnsmasq.d' | String  | Configurations directory path          |
| `manala_dnsmasq_configs_template`         |  ~               | String  | Configurations template                |
| `manala_dnsmasq_configs`                  | []               | Array   | Configurations                         |

### Configuration example

```yaml
manala_dnsmasq_configs:
  - file:     dev.conf
    template: configs/default.dev.j2
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.dnsmasq }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
