# Ansible Role: Files

This role will deal with the attributes of files.

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

None.

## Dependencies

None.

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

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
  tasks:
    - ansible.builtin.import_role:  
        name: manala.roles.files
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
