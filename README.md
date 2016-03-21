# Ansible Role: Alternatives

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

| Name                 | Default| Type  | Description   |
|--------------------- |------- |------ |-------------  |
| manala_alternatives  | []     | Array | Alternatives  |

### Configuration

`manala_alternatives` allow you to managed custom alternatives path.

```yaml
manala_alternatives:
  - name: editor
    path: /usr/bin/vim.basic
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
