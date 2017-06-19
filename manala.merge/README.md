# Ansible Role: Merge [![Build Status](https://travis-ci.org/manala/ansible-role-merge.svg?branch=master)](https://travis-ci.org/manala/ansible-role-merge)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.merge
```

Using ansible galaxy requirements file:

```yaml
- src: manala.merge
```

## Role Handlers

None.

## Role Variables

### Definition

| Name                  | Default | Type  | Description |
| --------------------- | ------- | ----- | ----------- |
| `manala_merge_hashes` | []      | Array | Hashes      |
| `manala_merge_prefix` | ~       | String| Prefix      |
| `manala_merge_var`    | ~       | String| Var         |

### Example

```yaml
- hosts: all
  vars:
    manala_merge_hashes:
      - _all
      - _env
      - _group_({{ group_names|join('|') }})
      - _host
      - foo: bar
        bar: foo
  roles:
    - manala.merge
```

### Hashes

...

### Prefix

...

### Var

...

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
