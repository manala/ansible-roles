# Ansible Role: Alternatives [![Build Status](https://travis-ci.org/manala/ansible-role-alternatives.svg?branch=master)](https://travis-ci.org/manala/ansible-role-alternatives)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of __alternatives__.

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.alternatives
```

Using ansible galaxy requirements file:

```yaml
- src: manala.alternatives
```

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Configuration

`manala_alternatives_selections` allow you to manage custom alternatives selections.

```yaml
manala_alternatives_selections:
  - selection: editor
    path: /usr/bin/vim.basic
  # Ignore selection
  - selection: foo
    path: /bin/bar
    state: ignore
  # Flatten selections
  - "{{ my_custom_selections_array }}"
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - role: manala.alternatives
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
