# Ansible Role: AppArmor [![Build Status](https://travis-ci.org/manala/ansible-role-apparmor.svg?branch=master)](https://travis-ci.org/manala/ansible-role-apparmor)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of [AppArmor](http://apparmor.net/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.apparmor
```

Using ansible galaxy requirements file:

```yaml
- src: manala.apparmor
```

## Role Handlers

| Name              | Type    | Description             |
| ----------------- | ------- | ----------------------- |
| `apparmor reload` | Service | Reload apparmor configs |

## Role Variables

| Name                                       | Default           | Type   | Description                            |
| ------------------------------------------ | ----------------- | ------ | -------------------------------------- |
| `manala_apparmor_install_packages`         | ~                 | Array  | Dependency packages to install         |
| `manala_apparmor_install_packages_default` | ['apparmor']      | Array  | Default dependency packages to install |
| `manala_apparmor_configs_dir`              | '/etc/apparmor.d' | String | Configurations directory path          |
| `manala_apparmor_configs`                  | []                | Array  | Configurations templates               |

## Example playbook

```yaml
- hosts: all

  vars:
    manala_apparmor_configs:
      - file:     lxc/lxc-profile-a
        template: "{{ playbook_dir }}/templates/lxc-default.j2"
      - file:     lxc/lxc-old-profile
        state:    absent

  roles:
    - { role: manala.apparmor }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
