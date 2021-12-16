#######################################################################################################

# :exclamation: DEPRECATION :exclamation:

## This repository and the role associated are deprecated in favor of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles)

## You will find informations on its usage on the [collection repository](https://github.com/manala/ansible-roles)

#######################################################################################################

# Ansible Role: Sudo [![Build Status](https://travis-ci.org/manala/ansible-role-sudo.svg?branch=master)](https://travis-ci.org/manala/ansible-role-sudo)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of Sudo.

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.sudo
```

Using ansible galaxy requirements file:

```yaml
- src: manala.sudo
```

## Role Handlers

| Name           | Type    | Description          |
| -------------- | ------- | -------------------- |
| `sudo restart` | Service | Restart sudo service |

## Role Variables

### Definition

| Name                                   | Default          | Type    | Description                            |
| -------------------------------------- | ---------------- | ------- | -------------------------------------- |
| `manala_sudo_install_packages`         | ~                | Boolean | Dependency packages to install         |
| `manala_sudo_install_packages_default` | ['sudo']         | Boolean | Default dependency packages to install |
| `manala_sudo_sudoers_exclusive`        | false            | Boolean | Sudoers files exclusivity              |
| `manala_sudo_sudoers_dir`              | '/etc/sudoers.d' | String  | Sudoers files directory path           |
| `manala_sudo_sudoers_defaults`         | {}               | Array   | Sudoers files defaults                 |
| `manala_sudo_sudoers`                  | []               | Array   | Sudoers files directives               |

### Example

```yaml
- hosts: all
  vars:
    manala_sudo_sudoers:
      # Template based (file name based on template)
      - template: sudo/app.j2
      # Template based (force file name)
      - file: template
        template: sudo/app.j2
      # Content based
      - file: content
        config: |
          user ALL=NOPASSWD:ALL
      # Config based (deprecated)
      - file: config
        config:
          - vagrant: ALL=NOPASSWD:ALL
      # Ensure sudoer is absent
      - file: absent
        state: absent # "present" by default
      # Ignore sudoer
      - file: ignore
        state: ignore
      # Flatten sudoers
      - "{{ my_custom_sudoers_array }}"
  roles:
    - role: manala.sudo

```

Exclusivity (all sudoers non defined by role will be deleted)

```yaml
manala_sudo_sudoers_exclusive: true
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
