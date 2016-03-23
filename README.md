<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: elao.elasticsearch

This role will assume the setup of elasticsearch server.

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Dependencies

None.

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.elasticsearch
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.elasticsearch }
```

## Role Handlers

| Name                    | Type    | Description           |
| ----------------------- | ------- | --------------------- |
| `elasticsearch restart` | Service | Restart elasticsearch |

## Role Variables

### Definition

| Name                         | Default  | Type  | Description                |
| ---------------------------- | -------- | ----- | -------------------------- |
| `elao_elasticsearch_plugins` | []       | Array | Plugins                    |

### Example

```yaml
- hosts: all
  vars:
    elao_elasticsearch_plugins:
      - name:       head
        repository: mobz/elasticsearch-head
  roles:
    - role: elao.elasticsearch
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: elao.elasticsearch }
```

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
