#######################################################################################################

# :exclamation: DEPRECATION :exclamation:

## This repository and the role associated are deprecated in favor of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles)

## You will find informations on its usage on the [collection repository](https://github.com/manala/ansible-roles)

#######################################################################################################

# Ansible Role: PhpMyAdmin [![Build Status](https://travis-ci.org/manala/ansible-role-phpmyadmin.svg?branch=master)](https://travis-ci.org/manala/ansible-role-phpmyadmin)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup and config of [PhpMyAdmin](https://www.phpmyadmin.net/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

This role is made to work with the __manala__ phpmyadmin debian package, available on the __manala__ debian repository. Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

```yaml
manala_apt_preferences:
  - phpmyadmin@manala
```

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.phpmyadmin
```

Using ansible galaxy requirements file:

```yaml
- src: manala.phpmyadmin
```

## Role Variables

### Definition

| Name                                         | Default        | Type    | Description                            |
| -------------------------------------------- | -------------- | ------- | -------------------------------------- |
| `manala_phpmyadmin_install_packages`         | ~              | Array   | Dependency packages to install         |
| `manala_phpmyadmin_install_packages_default` | ['phpmyadmin'] | Array   | Default dependency packages to install |
| `manala_phpmyadmin_configs_exclusive`        | false          | Boolean | Configurations exclusivity             |
| `manala_phpmyadmin_configs`                  | []             | Array   | Configurations                         |

### Configuration example

```yaml
---

manala_phpmyadmin_configs_exclusive: true
manala_phpmyadmin_configs:
  - file:     config.inc.php
    template: configs/default.dev.j2
    config:
      - blowfish_secret: "WU9VIEdPVCBSSUNLIFJPTExFRA=="
    servers:
      - id: 1
        config:
          - host: mysql
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.phpmyadmin }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
