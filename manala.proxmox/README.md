# Ansible Role: Proxmox [![Build Status](https://travis-ci.org/manala/ansible-role-proxmox.svg?branch=master)](https://travis-ci.org/manala/ansible-role-proxmox)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of [Proxmox](https://www.proxmox.com/en/).

Handles:
- Templates download
- Storage management

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

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

| Name                                  | Default                    | Type    | Description                                            |
| ------------------------------------- | -------------------------- | ------- | ------------------------------------------------------ |
| `manala_proxmox_templates_exclusive`  | false                      | Boolean | Exclusion of existings templates                       |
| `manala_proxmox_templates_dir`        | /var/lib/vz/template/cache | String  | Path to the templates directory                        |
| `manala_proxmox_templates`            | []                         | Array   | Collection of templates                                |
| `manala_proxmox_isos_exclusive`       | false                      | Boolean | Exclusion of existings isos                            |
| `manala_proxmox_isos_dir`             | /var/lib/vz/template/iso   | String  | Path to the isos directory                             |
| `manala_proxmox_isos`                 | []                         | Array   | Collection of isos                                     |
| `manala_proxmox_storages`             | []                         | Array   | Collection of storage points                           |
| `manala_proxmox_instances`            | []                         | Array   | Proxmove instances to manage                           |
| `manala_proxmox_instances_defaults`   | {}                         | Array   | Defaults parameters used by `manala_proxmox_instances` |

### Configuration example

#### Proxmox templates

```
manala_proxmox_templates_exclusive: true
manala_proxmox_templates:
  - http://download.manala.io/proxmox/templates/debian-7.0-manala_2.0.0_amd64.tar.gz
  - url: http://download.manala.io/proxmox/templates/debian-8.0-manala_2.0.0_amd64.tar.gz
    file: debian-8.0.tar.gz
  - url: http://download.manala.io/proxmox/templates/debian-9.0-manala_2.0.0_amd64.tar.gz
    state: absent
```

#### Proxmox isos

```
manala_proxmox_isos_exclusive: true
manala_proxmox_isos:
  - https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-9.4.0-amd64-netinst.iso
  - url: https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-9.4.0-amd64-netinst.iso
    file: debian-9.4.tar.gz
  - url: https://cdimage.debian.org/debian-cd/9.4.0/arm64/iso-cd/debian-9.4.0-arm64-netinst.iso
    state: absent
```

#### Proxmox storages

```yaml
manala_proxmox_storages:
  - id:       storage_point_identifier
    type:     nfs
    server:   servername
    export:   /export/ftpbackup/my_storage_point_name
    maxfiles: 3
    content:  backup
    nodes:    hypervisor-1
```

#### Proxmox instances

```yaml
manala_proxmox_instances_defaults:
  api_user: root@pam
  api_password: proxmox-api-password
  api_host: hv-1
  node: hv-1
  password: root-password

# See http://docs.ansible.com/ansible/latest/proxmox_module.html#options for available options
manala_proxmox_instances:
  - vmid: 101
    hostname: mysql-1.local
    cpus: 2
    memory: 6144
    swap: 512
    disk: 30
    netif: '{
      "net0": "name=eth0,ip=192.168.0.1/24,gw=192.168.0.254,bridge=vmbr1"
    }'
    pool: db
    ostemplate: local:vztmpl/debian-8.0-manala_2.0.0_amd64.tar.gz
```

## Example playbook

```yaml
- hosts: hypervisors
  roles:
    - { role: manala.proxmox }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io) is proudly supported by [**ELAO**](https://www.elao.com/)
