# Ansible Role: Cloud_init [![Build Status](https://travis-ci.org/manala/ansible-role-cloud_init.svg?branch=master)](https://travis-ci.org/manala/ansible-role-cloud_init)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the configuration of [Cloud-init](https://cloud-init.io/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.cloud_init
```

Using ansible galaxy requirements file:

```yaml
- src: manala.cloud_init
```

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Configuration example

```yaml
manala_cloud_init_configs:
  - file: 99_hostname.cfg
    config: |
      fqdn: foo.manala.io
      hostname: foo
```

## Example playbook

```yaml
- hosts: all
  roles:
    - role: manala.cloud_init
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
