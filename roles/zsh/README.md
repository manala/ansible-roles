# Ansible Role: Zsh [![Build Status](https://travis-ci.org/manala/ansible-role-zsh.svg?branch=master)](https://travis-ci.org/manala/ansible-role-zsh)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of Zsh.

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.zsh
```

Using ansible galaxy requirements file:

```yaml
- src: manala.zsh
```

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Example

```yaml
manala_zsh_bin: /bin/zsh
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - role: manala.zsh
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
