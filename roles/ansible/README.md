# Ansible Role: Ansible

This role will deal with the setup and the config of [Ansible](https://www.ansible.com/).

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

This role is made to work with the __manala__ ansible debian package, available on the __manala__ debian repository. Please use the [**manala.roles.apt**](../apt/) role to handle it properly.

```yaml
manala_apt_preferences:
  - ansible@manala
```

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

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
  tasks:
    - ansible.builtin.import_role:  
        name: manala.roles.ansible
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
