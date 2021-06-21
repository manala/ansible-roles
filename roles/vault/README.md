# Ansible Role: Vault [![Build Status](https://travis-ci.org/manala/ansible-role-vault.svg?branch=master)](https://travis-ci.org/manala/ansible-role-vault)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup and configuration of [Hashicorp Vault server](https://www.vaultproject.io/).

This role does *not* :
- [Initialize](https://www.vaultproject.io/intro/getting-started/deploy.html#initializing-the-vault) the vault
- [Unseal](https://www.vaultproject.io/docs/concepts/seal.html#unsealing) the vault
- Provide a way to retrieve vault secret from ansible. For that, you can use offical [hashi_vault lookup](https://github.com/ansible/ansible/blob/devel/lib/ansible/plugins/lookup/hashi_vault.py)

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

This role is made to work with the __manala__ vault debian package, available on the __manala__ debian repository. Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

```yaml
manala_apt_preferences:
  - vault@manala
```

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.vault
```

Using ansible galaxy requirements file:

```yaml
- src: manala.vault
```

## Role Variables

### Definition

| Name                                    | Default                 | Type   | Description                            |
| --------------------------------------- | ----------------------- | ------ | -------------------------------------- |
| `manala_vault_install_packages`         | ~                       | Array  | Dependency packages to install         |
| `manala_vault_install_packages_default` | ['vault']               | Array  | Default dependency packages to install |
| `manala_vault_config_file`              | '/etc/vault/config.hcl' | String | Main configuration file path           |
| `manala_vault_config_template`          | ~                       | String | Main configuration template path       |

## Configuration example

```yaml
manala_vault_config_template: vault/vault/config.hcl.j2
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.vault }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
