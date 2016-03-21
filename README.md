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
ansible-galaxy install manala.merge,2.0
```

Using ansible galaxy requirements file:

```yaml
- src:     manala.merge
  version: 2.0
```

## Role Handlers

None.

## Role Variables

### Definition

| Name                  | Default | Type  | Description |
| --------------------- | ------- | ----- | ----------- |
| `manala_apt_patterns` | []      | Array | Patterns    |

### Example

```yaml
- hosts: all
  vars:
    manala_merge_patterns:
      - _all
      - _env
      - _group_({{ group_names|join('|') }})
      - _host
  roles:
    - manala.merge
```

### Patterns

...

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
