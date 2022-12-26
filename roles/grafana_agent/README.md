# Ansible Role: Grafana Agent

This role will deal with the configuration of [Grafana Agent](https://grafana.com/docs/agent/latest/).

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

This role is made to work with the __grafana agent__ official debian packages, available on the [__grafana__ debian repository](https://grafana.com/docs/agent/latest/set-up/install-agent-linux/#install-on-debian-or-ubuntu). Please use the [**manala.roles.apt**](../apt/) role to handle it properly.

```yaml
manala_apt_preferences:
  - grafana-agent@grafana
```

## Dependencies

None.

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Configuration example

See : https://grafana.com/docs/agent/latest/configuration/

```yaml
manala_grafana_agent_config: |
  # Sample config for Grafana Agent
  # For a full configuration reference, see: https://grafana.com/docs/agent/latest/configuration/.
  server:
    log_level: warn

  metrics:
    global:
      scrape_interval: 1m
    wal_directory: '/var/lib/grafana-agent'
    configs:
      # Example Prometheus scrape configuration to scrape the agent itself for metrics.
      # This is not needed if the agent integration is enabled.
      # - name: agent
      #   host_filter: false
      #   scrape_configs:
      #     - job_name: agent
      #       static_configs:
      #         - targets: ['127.0.0.1:9090']

  integrations:
    agent:
      enabled: true
    node_exporter:
      enabled: true
      include_exporter_metrics: true
      disable_collectors:
        - "mdadm"
```

## Example playbook

```yaml
- hosts: foo
  tasks:
    - ansible.builtin.import_role:  
        name: manala.roles.grafana_agent
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
