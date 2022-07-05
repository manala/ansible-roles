# Ansible Role: Cloud_init

This role will deal with the configuration of [Cloud-init](https://cloud-init.io/).

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
  tasks:
    - ansible.builtin.import_role:  
        name: manala.roles.cloud_init
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
