# Ansible Role: Alternatives [![Build Status](https://travis-ci.org/manala/ansible-role-alternatives.svg?branch=master)](https://travis-ci.org/manala/ansible-role-alternatives)

This role will deal with the setup of __alternatives__.

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

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

| Name                           | Default| Type  | Description   |
|------------------------------- |------- |------ |-------------  |
| manala_alternatives_selections | []     | Array | Alternatives  |

### Configuration

`manala_alternatives_selections` allow you to manage custom alternatives selections.

```yaml
manala_alternatives_selections:
  - selection: editor
    path:      /usr/bin/vim.basic
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.alternatives }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
