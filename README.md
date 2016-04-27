# Ansible Role: Merge

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

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
