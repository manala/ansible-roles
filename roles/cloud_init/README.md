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

| Name                                         | Default                  | Type   | Description                            |
| -------------------------------------------- | ------------------------ | -------| -------------------------------------- |
| `manala_cloud_init_install_packages`         | ~                        | String | Dependency packages to install         |
| `manala_cloud_init_install_packages_default` | ['cloud-init']           | String | Default dependency packages to install |
| `manala_cloud_init_configs_exclusive`        | false                    | String | Configs exclusivity                    |
| `manala_cloud_init_configs_dir`              | '/etc/cloud/cloud.cfg.d' | String | Configs directory path                 |
| `manala_cloud_init_configs_defaults`         | {}                       | Array  | Configs defaults                       |
| `manala_cloud_init_configs`                  | []                       | Array  | Configs collection                     |

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
