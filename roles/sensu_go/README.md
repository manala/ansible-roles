# Ansible Role: Sensu Go

This role will deal with the setup of [Sensu Go](https://sensu.io/).

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

This role is made to work with the __sensu go__ official packages, available on the [__sensu go__ repository](https://packagecloud.io/sensu/stable/). Please use the [**manala.roles.apt**](../apt/) role to handle it properly.

```yaml
manala_apt_preferences:
  - sensu-go@sensu-go
```

## Dependencies

None.

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Configuration example

## Sensu Go backend

```yaml
manala_sensu_go_backend: true

manala_sensu_go_backend_config:
  - state-dir: /tmp
```

## Sensu Go agent

```yaml
manala_sensu_go_agent_config:
  - backend-url: ['ws://127.0.0.1:8081']
  - subscriptions: ['linux', 'mysql', 'foo']
```

## Example playbook

```yaml
- hosts: sensu
  tasks:
    - ansible.builtin.import_role:
        name: manala.roles.sensu_go
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
