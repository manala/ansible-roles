# Ansible Role: Ngrok [![Build Status](https://travis-ci.org/manala/ansible-role-ngrok.svg?branch=master)](https://travis-ci.org/manala/ansible-role-ngrok)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup and the config of [Ngrok](https://ngrok.com/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

This role is made to work with the __manala__ ngrok debian package, available on the __manala__ debian repository. Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

```yaml
manala_apt_preferences:
 - ngrok@manala
```

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.ngrok
```

Using ansible galaxy requirements file:

```yaml
- src: manala.ngrok
```

## Role Handlers

None

## Role Variables

### Definition

| Name                                    | Default      | Type    | Description                            |
| --------------------------------------- | ------------ | ------- | -------------------------------------- |
| `manala_ngrok_install_packages`         | ~            | Array   | Dependency packages to install         |
| `manala_ngrok_install_packages_default` | ['ngrok']    | Array   | Default dependency packages to install |
| `manala_ngrok_configs_exclusive`        | false        | Boolean | Configurations exclusivity             |
| `manala_ngrok_configs_dir`              | '/etc/ngrok' | String  | Configurations directory path          |
| `manala_ngrok_configs_template`         | ~            | String  | Configurations template path           |
| `manala_ngrok_configs`                  | []           | Array   | Configurations                         |

### Example

```yaml
- hosts: all
  roles:
    - role: manala.ngrok
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
