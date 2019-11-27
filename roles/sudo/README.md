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
| `manala_sudo_sudoers`                  | []               | Array   | Sudoers files directives               |

### Example

```yaml
- hosts: all
  vars:
    manala_sudo_sudoers:
      # Template based
      - file: foo_template
        template: sudo/app.j2
      # Config based, empty template by default
      - file: foo
        config:
          - vagrant: ALL=NOPASSWD:ALL
      # Raw content based
      - file: foo_content
        content: |
          user ALL=NOPASSWD:ALL
        state: absent
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
