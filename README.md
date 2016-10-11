# Ansible Role: Files

This role will deal with the configuration of files.

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.files
```

Using ansible galaxy requirements file:

```yaml
- src: manala.files
```

## Role Variables

| Name                               | Default | Type   | Description               |
| ---------------------------------- | ------- | ------ | ------------------------- |
| `manala_files_attributes`          | []      | Array  | Files attributes          |
| `manala_files_attributes_defaults` | []      | Array  | Files attributes defaults |

### Configuration example

```yaml
manala_files_attributes:
  - path: /var/log/symfony
    state: directory
  - path: /var/cache/symfony
    state: directory
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.files }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
