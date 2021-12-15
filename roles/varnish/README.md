#######################################################################################################

# :exclamation: DEPRECATION :exclamation:

## This repository and the role associated are deprecated.

### You can find our other roles in the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles). You will find informations on its usage on the [collection repository](https://github.com/manala/ansible-roles)

#######################################################################################################

# Ansible Role: Varnish [![Build Status](https://travis-ci.org/manala/ansible-role-varnish.svg?branch=master)](https://travis-ci.org/manala/ansible-role-varnish)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of [Varnish](https://varnish-cache.org/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

Ansible 1.9.4+
--------------

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.varnish
```

Using ansible galaxy requirements file:

```yaml
- src: manala.varnish
```

Role Handlers
-------------

| Name              | Type    | Description            |
| ----------------- | ------- | ---------------------- |
| `varnish restart` | Service | Restart varnish server |

Role Variables
--------------

| Name                                      | Default                | Type    | Description                                  |
| ----------------------------------------- | ---------------------- | ------- | -------------------------------------------- |
| `manala_varnish_version`                  | ~                      | String  | Version (autodetect if null)                 |
| `manala_varnish_install_packages`         | ~                      | String  | Dependency packages to install               |
| `manala_varnish_install_packages_default` | ['varnish']            | String  | Default dependency packages to install       |
| `manala_varnish_config_file`              | '/etc/default/varnish' | String  | Main configuration file path                 |
| `manala_varnish_config_template`          | 'config/default.j2'    | String  | The default template (based on package file) |
| `manala_varnish_config`                   | []                     | Array   | Configuration directives                     |
| `manala_varnish_configs_exclusive`        | false                  | Boolean | Exclusion of existings files                 |
| `manala_varnish_configs_dir`              | '/etc/varnish/'        | String  | Path to the main configuration directory     |
| `manala_varnish_configs_template`         | ~                      | String  | Main config template                         |
| `manala_varnish_configs`                  | 'default.vcl'          | Array   | List of VCL files                            |

### Varnish configuration

The `manala_varnish_config_template` key will allow you to use differents main configuration templates. The role is shipped with basic templates :

- default (File shipped with the distribution package, minimal configuration)
- default.prod (This configuration is recommended for production purposes)

#### Example:
```yaml
manala_varnish_config_template: config/default.prod.j2
```

The `manala_varnish_config` key is made to allow you to define custom directives.

#### Example:

```yaml
manala_varnish_config:
    - START:                    true
    - NFILES:                   131072
    - MEMLOCK:                  82000
    - VARNISH_VCL_CONF:         /etc/varnish/foobar.vcl
    - VARNISH_LISTEN_ADDRESS:   "{{ ansible_eth0.ipv4.address }}"
    - VARNISH_LISTEN_PORT:      80
    - VARNISH_STORAGE_SIZE:     3G
    - VARNISH_STORAGE:          "malloc,${VARNISH_STORAGE_SIZE}"
```

### Exclusivity

`manala_varnish_configs_exclusive` allow you to clean up existing varnish VCL configuration files into directory defined by the `manala_varnish_configs_dir` key. Made to be sure no old or manually created files will alter current configuration.

```yaml
manala_varnish_configs_exclusive: true
```

Example playbook
----------------

```yaml
- hosts: servers
  roles:
    - { role: manala.varnish }
```

Tests
-----

Test suite require the following tools:

- Docker
- Manala test suite [**(Docker image)**](https://github.com/manala/docker-image-ansible-debian)

Licence
-------
MIT

Author information
------------------

Manala [**(http://www.manala.io/)**](http://www.manala.io) is an open source project supported by the french web agency [**(ELAO)**](http://www.elao.com)
