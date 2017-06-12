# Ansible Role: elasticsearch

This role will deal with the setup of __elasticsearch__.

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.elasticsearch
```

Using ansible galaxy requirements file:

```yaml
- src: manala.elasticsearch
```

## Role Handlers

| Name                    | Type    | Description           |
| ----------------------- | ------- | --------------------- |
| `elasticsearch restart` | Service | Restart elasticsearch |

## Role Variables

### Definition

| Name                           | Default  | Type  | Description                |
| ------------------------------ | -------- | ----- | -------------------------- |
| `manala_elasticsearch_plugins` | []       | Array | Plugins                    |

### Example

```yaml
- hosts: all
  vars:
    manala_elasticsearch_plugins:
      - name:       head
        repository: mobz/elasticsearch-head
  roles:
    - role: manala.elasticsearch
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.elasticsearch }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
