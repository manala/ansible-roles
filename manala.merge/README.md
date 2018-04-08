# Ansible Role: Merge [![Build Status](https://travis-ci.org/manala/ansible-role-merge.svg?branch=master)](https://travis-ci.org/manala/ansible-role-merge)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the merging of ansible variables.

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

### Examples

Merge hashes and store results elements as facts.

Hashes can be specified directly as dict, or as reference with a string.

Scalar values are overriden, where dict and list values are merged.

```yaml
- hosts: all
  vars:
    foo: bar
    bar:
      - bar_1
    baz:
      1: baz_1
    # First hash
    hash_1:
      foo: foo
      bar:
        - bar_2
    # Second hash
    hash_2:
      bar:
        - bar_3
    manala_merge_hashes:
      - hashes:
          - hash_1 # First hash reference
          - hash_2 # Second hash reference
          # Third hash
          - baz:
              2: baz_2
  roles:
    - manala.merge
  tasks:
    - debug:
        var: foo # -> foo
    - debug:
        var: bar # -> ['bar_1', 'bar_2', 'bar_3']
    - debug:
        var: baz # -> {1: 'baz_1', 2: 'baz_2'}
```

Hash references can be specified as regex.

```yaml
- hosts: all
  vars:
    # First hash
    hash_1:
      foo: foo
    # Second hash
    hash_2:
      bar: bar
    manala_merge_hashes:
      - hashes:
          - hash_(\w*)
  roles:
    - manala.merge
  tasks:
    - debug:
        var: foo # -> foo
    - debug:
        var: bar # -> bar
```

Resulting facts name can be prefixed.

```yaml
- hosts: all
  vars:
    manala_merge_hashes:
      - hashes:
          - foo: foo
            bar: bar
        prefix: foo_
  roles:
    - manala.merge
  tasks:
    - debug:
        var: foo_foo # -> foo
    - debug:
        var: foo_bar # -> bar
```

Resulting facts name can be stored in an isolated var.

```yaml
- hosts: all
  vars:
    manala_merge_hashes:
      - hashes:
          - foo: foo
            bar: bar
        var: foo
  roles:
    - manala.merge
  tasks:
    - debug:
        var: foo # -> {'foo': 'foo', 'bar': 'bar'}
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
