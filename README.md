# Ansible Role: Telegraf

This role will deal with the setup and the config of influxdata Telegraf.

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.telegraf
```

Using ansible galaxy requirements file:

```yaml
- src: manala.telegraf
```

## Role Handlers

| Name               | Type    | Description            |
| ------------------ | ------- | ---------------------- |
| `telegraf restart` | Service | Restart telegraf agent |

## Role Variables

### Example

## Playbook

```yaml
- hosts: all
  roles:
    - role: manala.telegraf
```

## Group/host vars

```yaml
  manala_telegraf_config:
    - agent:
      - hostname: "{{ ansible_fqdn }}"
      - quiet: true

  manala_telegraf_configs_exclusive: true
  manala_telegraf_configs:
    - file:     output_influxdb.conf
      template: configs/output_influxdb.conf.j2
      config:
        - urls: ["udp://127.0.0.1:8090"]
        - database: telegraf
        - username: telegraf
        - password: password

    - file:     input_system.conf
      template: configs/input_system.conf.j2

    - file:     input_cpu.conf
      template: configs/input_cpu.conf.j2

    - file:     input_custom.conf
      template: "{{ playbook_dir }}/templates/telegraf/input_custom.conf.j2"
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)