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

General:
```yaml
manala_files_attributes:
  # Ignore attribute
  - path: /tmp/foo
    state: ignore
  # Flatten attributes
  - "{{ my_custom_files_attributes_array }}"
```

File:
```yaml
manala_files_attributes:
  - path: /tmp/foo # Required. An empty file is created on path if not present
  - path: /tmp/bar
    user: foo
    group: bar
    mode: "0644"
  - path: /tmp/baz
    state: absent
  - path: /tmp/qux
    parents: true # Recursively create file's directories
    force: true # Force path to be a file
```

Directory:
```yaml
manala_files_attributes:
  - path: /tmp/foo # Required
    state: directory
  - path: /tmp/bar
    state: directory
    user: foo
    group: bar
    mode: "0755"
  - path: /tmp/baz
    state: absent
  - path: /tmp/qux
    state: directory
    force: true # Force path to be a directory
```

Link:
```yaml
manala_files_attributes:
  - path: /tmp/foo # Required
    src: /tmp/bar
  - path: /tmp/qux
    src: /tmp/bar
    force: true # Force path to be a link
```

Template:
```yaml
manala_files_attributes:
  - path: /tmp/foo # Required
    template: foo.j2
  - path: /tmp/bar
    template: foo.j2
    user: foo
    group: bar
    mode: "0755"
  - path: /tmp/baz
    template: foo.j2
    state: absent
  - path: /tmp/qux
    template: foo.j2
    parents: true # Recursively create template file's directories
```

Content:
```yaml
manala_files_attributes:
  - path: /tmp/foo/bar # Required
    content: |
      Hello world!
  - path: /tmp/bar
    content: |
      Hello world!
    user: foo
    group: bar
    mode: "0755"
  - path: /tmp/baz
    content: |
      Hello world!
    state: absent
  - path: /tmp/qux
    content: |
      Hello world!
    parents: true # Recursively create content file's directories
```

Copy:
```yaml
manala_files_attributes:
  - path: /tmp/foo # Required
    copy: /tmp/bar
```

Symbolic link to directory:
```yaml
manala_files_attributes:
  - path: /path/to/link # Required
    src: /path/to/directory # Required
    state: link_directory
    #force: true # Force both `path` to be a link and `src` to be a directory
    #parents: true # Recursively create both link's directories
```

Symbolic link to file:
```yaml
manala_files_attributes:
  - path: /path/to/link # Required
    src: /path/to/file # Required
    state: link_file
    #force: true # Force both `path` to be a link and `src` to be a file
    #parents: true # Recursively create both file and link's directories
```

Get url:
```yaml
manala_files_attributes:
  - path: /tmp/bar # Required
    url: http://example.com/foo
```

Get url and unarchive:
```yaml
manala_files_attributes:
  - path: /tmp/bar.tar.gz
    url: http://example.com/foo.tar.gz
    unarchive: true
    creates: /tmp/baz
```

Defaults:
```yaml
manala_files_attributes_defaults:
  # Will be applied to *all* files attributes
  - user: nobody
    parents: true
  # Will be applied to files attributes path beginning by "/etc"
  - path: ^/etc
    user: root
    group: root
```

## Example playbook

```yaml
- hosts: all
  roles:
    - role: manala.files
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
