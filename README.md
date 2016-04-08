# Ansible Role: Proxmox

This role will handle:
- Templates download
- Storage management

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.proxmox
```

Using ansible galaxy requirements file:

```yaml
- src: manala.proxmox
```

## Role Handlers

None.

## Role Variables

### Definition

| Name                                  | Default                    | Type    | Description                    |
| ------------------------------------- | -------------------------- | ------- | ------------------------------ |
| `manala_proxmox_templates_exclusive`  | false                      | Boolean | Exclusion of existings files   |
| `manala_proxmox_templates_dir`        | /var/lib/vz/template/cache | String  | Path to the template directory |
| `manala_proxmox_templates`            | []                         | Array   | Collection of templates        |
| `manala_proxmox_storages`             | []                         | Array   | Collection of storage points   |

### Example

```yaml
- hosts: all
  vars:
    manala_proxmox_storages:
      - id:       storage_point_identifier
        type:     nfs
        server:   servername
        export:   /export/ftpbackup/my_storage_point_name
        maxfiles: 3
        content:  backup
        nodes:    hypervisor-1

    manala_proxmox_templates_exclusive: false
    manala_proxmox_templates_dir:       /var/lib/vz/template/cache
    manala_proxmox_templates:           []
  roles:
    - role: manala.proxmox
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io) is proudly supported by [**ELAO**](https://www.elao.com/)
