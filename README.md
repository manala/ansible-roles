# Ansible Role: Maxscale [![Build Status](https://travis-ci.org/manala/ansible-role-maxscale.svg?branch=master)](https://travis-ci.org/manala/ansible-role-maxscale)

This role will deal with the setup and configuration of MaxScale the Mysql/MariaDB proxy.

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

This role is made to work with the __mariadb maxscale__ debian packages, available on the [__mariadb__ repository](https://downloads.mariadb.com/MaxScale/).
Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

## Dependencies

None.

## Installation

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.maxscale
```

Using ansible galaxy requirements file:

```yaml
- src: manala.maxscale

```
## Role Handlers

| Name             | Type    | Description              |
| ---------------- | ------- | ------------------------ |
| maxscale restart | Service | Restart Maxscale service |

## Role Variables

| Name                                | Default           | Type   | Description                                            |
| ----------------------------------- | ----------------- | -------| ------------------------------------------------------ |
| `manala_maxscale_config_file`       | /etc/maxscale.cnf | String | Configuration file                                     |
| `manala_maxscale_config_template`   | config/empty.j2   | String | Default configuration template                         |
| `manala_maxscale_config`            | []                | Array  | Maxscale configuration options                         |

### Configuration example (Galera cluster configuration)

```yaml
# Using a custom template
manala_maxscale_config_template: "{{ playbook_dir ~ '/templates/maxscale/custom_template.j2' }}"

manala_maxscale_config:
  - maxscale:
    - threads: auto #Dedicated container
  - Splitter Service:
    - type:    service
    - router:  readwritesplit
    - servers: mariadb-1, mariadb-2, mariadb-3
    - user:    maxscale
    - passwd:  XXXXXXXXXXXXXX
  - Splitter Listener:
    - type:     listener
    - address:  "{{ ansible_eth0.ipv4.address }}" # Ip of the host, can be omit default is listen all interfaces
    - port:     3306
    - socket:   /tmp/ClusterMaster
    - service:  Splitter Service
    - protocol: MySQLClient
  - mysql-1.elao:
    - type:     server
    - address:  172.16.X.XX
    - port:     3306
    - protocol: MySQLBackend
  - mysql-2.elao:
    - type:     server
    - address:  172.16.X.XX
    - port:     3306
    - protocol: MySQLBackend
  - mysql-3.elao:
    - type:     server
    - address:  172.16.X.XX
    - port:     3306
    - protocol: MySQLBackend
  - Galera Monitor:
    - type:     monitor
    - module:   galeramon
    - servers:  mariadb-1, mariadb-1, mariadb-1
    - user:     maxscale
    - passwd:   XXXXXXXXXXX
  - CLI:
    - type:     service
    - router:   cli
  - CLI Listener:
    - type:     listener
    - service:  CLI
    - protocol: maxscaled
    - address:  localhost
    - port:     6603
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.maxscale }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
