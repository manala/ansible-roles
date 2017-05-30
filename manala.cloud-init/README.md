# Ansible Role: Cloud-init [![Build Status](https://travis-ci.org/manala/ansible-role-cloud-init.svg?branch=master)](https://travis-ci.org/manala/ansible-role-cloud-init)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the configuration of [Cloud-init](https://cloud-init.io/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.cloud-init
```

Using ansible galaxy requirements file:

```yaml
- src: manala.cloud-init
```

## Role Variables

| Name                                    | Default                | Type   | Description                 |
| --------------------------------------- | ---------------------- | -------| --------------------------- |
| `manala_cloud_init_configs_exclusive`   | false                  | String |                             |
| `manala_cloud_init_configs_dir`         | /etc/cloud/cloud.cfg.d | String |                             |
| `manala_cloud_init_configs_template`    | configs/empty.j2       | Array  | Cloud-init configs template |
| `manala_cloud_init_configs`             | []                     | Array  | Cloud-init configs          |

### Configuration example

```
manala_cloud_init_configs:
  - file: 99_hostname.cfg
    config:
      - fqdn: delicious.manala.io
      - hostname: delicious
```

## Example playbook

```yaml
- hosts: all
  roles:
    - { role: manala.cloud-init }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
