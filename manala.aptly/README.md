# Ansible Role: Aptly

This role will add third party sources to the package manager by:
- Adding source URL as new repository
- Adding secure key specified
- Managing packages preferences files (aka. pinning)
- Installing packages

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.aptly
```

Using ansible galaxy requirements file:

```yaml
- src: manala.aptly
```

## Role Handlers

None.

## Role Variables

### Definition

| Name                           | Default         | Type   | Description                |
| ------------------------------ | --------------- | ------ | -------------------------- |
| `manala_aptly_user`            | ~               | String | Update                     |
| `manala_aptly_config_file`     | /etc/aptly.conf | String | Upgrade                    |
| `manala_aptly_config_template` | ~               | String | Collection of components   |
| `manala_aptly_config`          | []              | Array  | Config                     |
| `manala_aptly_repositories`    | []              | Array  | Collection of repositories |

### Example

```yaml
- hosts: all
  vars:
    manala_aptly_user: aptly
    manala_aptly_config:
      - rootDir: /srv/aptly
      - architectures:
        - amd64
    manala_aptly_repositories:
      - name:         wheezy
        comment:      Wheezy
        component:    main
        distribution: wheezy
        origin:       Foo
        label:        Bar
      - name:         jessie
        comment:      Jessie
        component:    main
        distribution: jessie
        origin:       Foo
        label:        Bar
  roles:
    - role: manala.aptly
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
