# Ansible Role: HAProxy [![Build Status](https://travis-ci.org/manala/ansible-role-haproxy.svg?branch=master)](https://travis-ci.org/manala/ansible-role-haproxy)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of [HAProxy](http://www.haproxy.org/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.haproxy
```

Using ansible galaxy requirements file:

```yaml
- src: manala.haproxy
```

## Role Handlers
| Name              | Type    | Description             |
| ----------------- | ------- | ----------------------- |
| `haproxy reload`  | Service | Reload haproxy service  |
| `haproxy restart` | Service | Restart haproxy service |

## Role Variables

| Name                                      | Default                      | Type         | Description                            |
| ----------------------------------------- | ---------------------------- | ------------ | -------------------------------------- |
| `manala_haproxy_install_packages`         | ~                            | Array        | Dependency packages to install         |
| `manala_haproxy_install_packages_default` | []                           | Array        | Default dependency packages to install |
| `manala_haproxy_errorfiles_dir`           | '/etc/haproxy/errors'        | String       | Errorfiles directory path              |
| `manala_haproxy_errorfiles`               | []                           | Array        | Errorfiles                             |
| `manala_haproxy_config_file`              | '/etc/haproxy/haproxy.cfg'   | String       | Configuration file path                |
| `manala_haproxy_config_template`          | 'config/http_default.cfg.j2' | String       | Configuration template                 |
| `manala_haproxy_configs_exclusive`        | false                        | Boolean      | Configurations exclusivity             |
| `manala_haproxy_configs_dir`              | '/etc/haproxy/conf.d'        | String       | Configurations dir path                |
| `manala_haproxy_configs_defaults`         | {}                           | Array        | Configuration defaults                 |
| `manala_haproxy_configs`                  | []                           | Array        | Configurations                         |
| `manala_haproxy_environment_file`         | '/etc/default/haproxy'       | String       | Environment file path                  |
| `manala_haproxy_environment_template`     | 'environment/_default.j2'    | String       | Environment base template              |
| `manala_haproxy_environment`              | ~                            | Array/String | Environment directives                 |

### Configuration example

Handle errorfiles

```yaml
manala_haproxy_errorfiles:
  - name: 400.http
    template: errorfiles/400.http.j2
  - name: maintenance.http
    template: errorfiles/maintenance.http.j2
```

Use custom config template

```yaml
manala_haproxy_config_template: haproxy/haproxy.cfg.j2
```

### Split configuration files

As mentioned in the documentation it's possible to split configuration files as haproxy will load all files found in a specific folder when this one is provided to the `-f` option at service startup.
On Debian this configuration path is handle by the `/etc/default/haproxy` file and the `CONFIG` environment variable.

**Be carefull:** *Files are added in lexical order (using LC_COLLATE=C) to the list of configuration files to be loaded*

#### Defining configuration files

```yaml
  manala_haproxy_environment:
    CONFIG: "{{ manala_haproxy_configs_dir }}" # /etc/haproxy/conf.d

  manala_haproxy_configs_exclusive: true
  manala_haproxy_configs:
    # Template based
    - file: 010-global.cfg
      template: all/haproxy/010-global.j2
      # Raw content based
    - file: 020-defaults.cfg
      config: |
        defaults
            log     global
            option  dontlognull
            option  abortonclose
    # Ensure config is absent
    - file: absent.cfg
      state: absent # "present" by default
    # Ignore config
    - file: ignore.cfg
      state: ignore
    # Flatten configs
    - "{{ my_custom_configs_array }}"
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - role: manala.haproxy
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
