# Ansible Role: Promtail

This role will deal with the setup of [Promtail](https://grafana.com/docs/loki/latest/clients/promtail/)

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

None.

## Dependencies

None.

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

## Example

```yaml
- hosts: all
  vars:
    nginx: true
    php: true
    haproxy: true
  tasks:
    - ansible.builtin.import_role:
        name: manala.roles.promtail
      vars:
        manala_promtail_service_args:
          - --log.level debug  # Debug mode
        manala_promtail_config: |
          ...

```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
