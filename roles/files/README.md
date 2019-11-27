# Ansible Role: Files [![Build Status](https://travis-ci.org/manala/ansible-role-files.svg?branch=master)](https://travis-ci.org/manala/ansible-role-files)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the attributes of files.

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

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
  - path: /var/log/app
    state: directory
```

Get url:
```yaml
manala_files_attributes:
  - path: /tmp/bar
    url:  http://example.com/foo
```

Get url and unarchive:
```yaml
manala_files_attributes:
  - path: /tmp/bar.tar.gz
    url:  http://example.com/foo.tar.gz
    unarchive: true
    creates:   /tmp/baz
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
