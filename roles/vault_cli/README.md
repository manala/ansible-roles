# Ansible Role: vault_cli

This role will deal with the installation of [vault](https://www.vaultproject.io/downloads)

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

### Definition

| Name                       | Default                  | Type   | Description                            |
| -------------------------- | ------------------------ | ------ | -------------------------------------- |
| `manala_vault_cli_version` | ~                        | String | Version to install, latest by default  |
| `manala_vault_cli_bin`     | '/usr/local/bin/vault'   | String | Binary path                            |

## Example playbook

```yaml
- hosts: all
  collections:
    - manala.roles
  tasks:
    - import_role:
        name: vault_cli
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
