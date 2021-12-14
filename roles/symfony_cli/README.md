# Ansible Role: Symfony Cli

This role will deal with the setup of [Symfony Cli](https://symfony.com/download)

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy collection install manala.roles
```

Using ansible galaxy requirements file:

```yaml
collections:
  - manala.roles
```

## Role Handlers

None.

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

## Example playbook

```yaml
- hosts: all
  collections:
    - manala.roles
  tasks:
    - import_role:
        name: symfony_cli
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
