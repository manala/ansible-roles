# Ansible Role: systemd

This role will deal with the configuration of __systemd__.

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.systemd
```

Using ansible galaxy requirements file:

```yaml
- src: manala.systemd
```

## Role Variables

| Name                                        | Default                 | Type    | Description                                 |
| ------------------------------------------- | ----------------------- | ------- | ------------------------------------------- |
| `manala_systemd_system_configs`             | {}                      | Array   | System configs                              |
| `manala_systemd_system_configs_template`    | system_configs/empty.j2 | String  |                                             |
| `manala_systemd_system_configs_exclusive`   | false                   | Boolean | Exclusion of existings files                |
| `manala_systemd_system_configs_dir`         | /etc/systemd/system     | String  | Path to the system configuration directory  |
| `manala_systemd_tmpfiles_configs_exclusive` | false                   | Boolean | Exclusion of existings files                |
| `manala_systemd_tmpfiles_configs_dir`       | /etc/tmpfiles.d         | String  | Path to the system configuration directory  |
| `manala_systemd_tmpfiles_configs_template`  | ~                       | String  |                                             |
| `manala_systemd_tmpfiles_configs`           | []                      | Array   | System configs                              |

### Configuration example

```yaml

manala_systemd_system_configs_exclusive: true

manala_systemd_system_configs:
  - file: redis-server.service.d/proxmox-lxc.conf
    template: system_configs/proxmox-lxc.j2

# Mask redis service
manala_systemd_services:
  - name: redis-server
    masked: true
```

### Configuration example (tmpfiles.d)

```yaml

manala_systemd_tmpfiles_configs_exclusive: true

manala_systemd_tmpfiles_configs:
  - file:   mysql.conf
    config:
      - d: /var/run/mysqld 0755 mysql mysql -
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.systemd }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
