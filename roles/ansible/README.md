# Ansible Role: Ansible [![Build Status](https://travis-ci.org/manala/ansible-role-ansible.svg?branch=master)](https://travis-ci.org/manala/ansible-role-ansible)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup and the config of [Ansible](https://www.ansible.com/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

This role is made to work with the __manala__ ansible debian package, available on the __manala__ debian repository. Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

```yaml
manala_apt_preferences:
  - ansible@manala
```

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.ansible
```

Using ansible galaxy requirements file:

```yaml
- src: manala.ansible
```

## Role Handlers

None

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Configuration example

```yaml
manala_ansible_hosts: |
  foo ansible_host=foo.com ansible_user=foo
  [bar]
  foo
  [bar:vars]
  bar=baz

manala_ansible_config: |
  [defaults]
  forks = 123
  ask_sudo_pass = False
  module_set_locale =: True

manala_ansible_host_vars_exclusive: true
manala_ansible_host_vars:
  - file: foo.yml
    vars: |
      foo: ~
      bar: bar
      baz: 123
  - file: bar.yml
    state: absent

manala_ansible_group_vars_exclusive: true
manala_ansible_group_vars:
  - file: foo.yml
    vars: |
      foo: ~
      bar: bar
      baz: 123
  - file: bar.yml
    state: absent      
```

### Example

```yaml
- hosts: all
  roles:
    - role: manala.ansible
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
