# Ansible Role: GlusterFS [![Build Status](https://travis-ci.org/manala/ansible-role-glusterfs.svg?branch=master)](https://travis-ci.org/manala/ansible-role-glusterfs)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the configuration of [GlusterFS](https://www.gluster.org/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

This role is made to work with the __glusterfs__ official packages, available on the [__glusterfs__ repository](https://download.gluster.org/pub/gluster/glusterfs). Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.glusterfs
```

Using ansible galaxy requirements file:

```yaml
- src: manala.glusterfs
```

## Role Variables

| Name                                        | Default                    | Type    | Description                            |
| -----------------------------------------   | -------------------------- | ------- | -------------------------------------- |
| `manala_glusterfs_install_packages`         | ~                          | Array   | Dependency packages to install         |
| `manala_glusterfs_install_packages_default` | ['glusterfs-server']       | Array   | Default dependency packages to install |
| `manala_glusterfs_volumes`                  | []                         | Array   | Volumes settings                       |


### Configuration example

## Volumes

```yaml
manala_glusterfs_volumes:
  - name: volume_test
    cluster:
      - foo
      - bar
    bricks: /mnt/foo, /mnt/bar
    replicas: 2
    options:
      nfs.disable: "off"
      storage.owner-gid: "1234"
      storage.owner-uid: "1234"
  # Ignore volume
  - name: volume_ignore
    state: ignore
  # Flatten volumes
  - "{{ my_custom_volumes_array }}"
```

- "Options" are expecting strings only. Quotes are required.
- To add bricks, use the same syntax on existent volume.

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
