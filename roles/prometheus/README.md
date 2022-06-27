# Ansible Role: Prometheus

This role will deal with the setup of [Prometheus](https://prometheus.io/)

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

None.

## Dependencies

None.

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

## Example

```yaml
- hosts: all
  vars:
    nginx: true
    php: true
    haproxy: true
  tasks:
    - ansible.builtin.import_role:
        name: manala.roles.prometheus
      vars:
        manala_prometheus_service_args:
          - --log.level debug  # Debug mode
        manala_prometheus_config: |
          global:
            scrape_interval: 15s
          scrape_configs:
            - job_name: node
              static_configs:
                - targets:
                    - localhost:9100
                  labels:
                    instance: "{{ inventory_hostname }}"
          {% if nginx %}
            - job_name: nginx
              static_configs:
                - targets:
                    - localhost:9113
                  labels:
                    instance: "{{ inventory_hostname }}"
          {% endif %}
          {% if php %}
            - job_name: php-fpm
              static_configs:
                - targets:
                    - localhost:9253
                  labels:
                    instance: "{{ inventory_hostname }}"
          {% endif %}
          {% if haproxy %}
            - job_name: haproxy
              static_configs:
                - targets:
                    - localhost:8888
                  labels:
                    instance: "{{ inventory_hostname }}"
          {% endif %}
        # Node Exporter
        manala_prometheus_node_exporter: true
        manala_prometheus_node_exporter_service_args:
          - --collector.systemd
          - --collector.processes
          - --web.listen-address localhost:9100
          - --web.disable-exporter-metrics
          - --web.max-requests 0
          - --log.level debug # Debug mode
        # Nginx Exporter
        manala_prometheus_nginx_exporter: "{{ nginx }}"
        manala_prometheus_nginx_exporter_service_args:
          - -web.listen-address localhost:9113
          - -nginx.scrape-uri http://localhost:8080/stub_status
        # Php Fpm Exporter
        manala_prometheus_php_fpm_exporter: "{{ php }}"
        manala_prometheus_php_fpm_exporter_service_args:
          - --web.listen-address localhost:9253
          - --phpfpm.fix-process-count
          - --phpfpm.scrape-uri "unix:///run/php.sock;/status"
          - --log.level debug # Debug mode

```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
