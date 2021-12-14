# Ansible Role: Kernel [![Build Status](https://travis-ci.org/manala/ansible-role-kernel.svg?branch=master)](https://travis-ci.org/manala/ansible-role-kernel)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will assume the setup of kernel.

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.kernel
```

Using ansible galaxy requirements file:

```yaml
- src: manala.kernel
```

## Role Handlers

None

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Configuration example

```yaml
manala_kernel_parameters:
  - parameter: net.ipv4.ip_nonlocal_bind
    value: 1

manala_kernel_modules:
  - ip_vs
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - role: manala.kernel
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
