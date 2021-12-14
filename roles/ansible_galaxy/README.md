# Ansible Role: Ansible Galaxy [![Build Status](https://travis-ci.org/manala/ansible-role-ansible_galaxy.svg?branch=master)](https://travis-ci.org/manala/ansible-role-ansible_galaxy)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of __Ansible Galaxy__.

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.ansible_galaxy
```

Using ansible galaxy requirements file:

```yaml
- src: manala.ansible_galaxy
```

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Roles

`manala_ansible_galaxy_roles` allow you to install ansible galaxy roles.

```yaml
manala_ansible_galaxy_roles:
  - manala.skeleton
```

### Flags

Update roles
```yaml
manala_ansible_galaxy:
  update: true

# Can also be set across manala roles
manala:
  update: true
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - role: manala.ansible_galaxy
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
