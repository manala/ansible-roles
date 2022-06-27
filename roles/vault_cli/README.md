# Ansible Role: vault_cli

This role will deal with the installation of [vault](https://www.vaultproject.io/downloads)

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

This role needs the __unzip__ debian packages. Please use the [**manala.roles.apt**](../apt/) role to handle it properly.

```yaml
manala_apt_packages:
  - unzip
```

## Dependencies

None.

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

## Example playbook

```yaml
- hosts: all
  tasks:
    - ansible.builtin.import_role:
        name: manala.roles.vault_cli
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
