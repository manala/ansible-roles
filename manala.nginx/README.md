# Ansible Role: Nginx [![Build Status](https://travis-ci.org/manala/ansible-role-nginx.svg?branch=master)](https://travis-ci.org/manala/ansible-role-nginx)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup and config of [Nginx](https://nginx.org/en/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

This role is made to work with the official __nginx__ debian packages, available on the __nginx__ debian repository. Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

```yaml
manala_apt_preferences:
 - nginx@nginx
```

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.nginx
```

Using ansible galaxy requirements file:

```yaml
- src: manala.nginx
```

## Role Handlers

| Name            | Type    | Description          |
| --------------- | ------- | -------------------- |
| `nginx restart` | Service | Restart nginx server |

## Role Variables

| Name                                    | Default             | Type    | Description                                    |
| --------------------------------------- | ------------------- | ------- | ---------------------------------------------- |
| `manala_nginx_install_packages`         | 'config/default.j2' | String  | Dependency packages to install                 |
| `manala_nginx_install_packages_default` | 'config/default.j2' | String  | Default dependency packages to install         |
| `manala_nginx_config_template`          | 'config/default.j2' | String  | Main configuration template path               |
| `manala_nginx_config`                   | []                  | Array   | Main configuration                             |
| `manala_nginx_configs`                  | []                  | Array   | Configurations                                 |
| `manala_nginx_configs_template`         | 'configs/empty.j2'  | String  | Configurations template path                   |
| `manala_nginx_configs_exclusive`        | false               | Boolean | Exclusion of existings files                   |
| `manala_nginx_configs_dir`              | '/etc/nginx/conf.d' | String  | Configurations directory path                  |
| `manala_nginx_user`                     | 'www-data'          | String  | User running nginx                             |
| `manala_nginx_log_dir`                  | '/var/log/nginx'    | String  | Directory path where Nginx will store its logs |


### Nginx configuration

The `manala_nginx_config_template` key will allow you to use differents main configuration templates. The role is shipped with basic templates :

- base (Simple template with no default configuration)
- dev (This configuration will keep serving NGINX informations like server tokens and provide directives for Vagrant VM)
- test
- prod (For production purpose. Cleaning all sensible server informations)

#### Example:
```yaml
manala_nginx_config_template: config/http.dev.j2
```

The `manala_nginx_config` key is made to allow you to alter main Nginx configuration templates.

#### Example:

```yaml
manala_nginx_config:
  - user: nginx
  - load_module: modules/ngx_http_geoip_module.so
  - load_module: modules/ngx_stream_geoip_module.so
  - events:
    - worker_connections: 1024
```

### Exclusivity

`manala_nginx_configs_exclusive` allow you to clean up existing nginx configuration files into directory defined by the `manala_nginx_configs_dir` key. Made to be sure no old or manually created files will alter current configuration.

```yaml
manala_nginx_configs_exclusive: true
```

### Hosts configuration

The `manala_nginx_configs` key is made to define Nginx host configuration.

A state (present|absent) can be provided.

```yaml
manala_nginx_configs:
  # Template based
  - file: foo_template.conf
    template: configs/app_magento_2_defaults.j2
  # Config based, empty template by default
  - file: foo.conf
    config:
      - server:
        - listen: 8080
        - location /:
          - root:  /srv/foo
  # Raw content based
  - file: foo_content.conf
    content: |
      server {
          listen         80 default_server;
          listen         [::]:80 default_server;
          server_name    example.com www.example.com;
          root           /var/www/example.com;
          index          index.html;
          try_files $uri /index.html;
      }
    state: absent
  - file: symfony2.conf
    config:
      - server:
        - server_name: symfony2.dev
        - root: /srv/symfony2/web
        - access_log:  "{{ manala_nginx_log_dir }}/app.access.log"
        - error_log:   "{{ manala_nginx_log_dir }}/app.error.log"
        - client_max_body_size: 8G
        - include:     conf.d/gzip
        - location ^~ /sf/:
          - alias: "/usr/share/symfony/symfony-1.4/data/web/sf/"
        - location /:
          - try_files: $uri /index.php$is_args$args
        - location ~ ^/(index|frontend_dev)\.php(/|$):
          - include: conf.d/php_fpm_params
  - file: wordpress.conf
    config:
      - server:
        - listen: 80
        - location /:
          - root:  /srv/wordpress/
  - file: pma.conf
    config:
      - server:
        - server_name:          pma.my_domain.com
        - listen:               "{{ ansible_venet0_0.ipv4.address }}:80"
        - root:                 /opt/phpmyadmin
        - include:              conf.d/gzip
        - client_max_body_size: 16M
        - location /:
          - try_files: $uri /index.php$is_args$args
  # Enables HTTPS offloading support based on a self-signed certificate
  - file: app_ssl.conf
    template: configs/app_ssl_offloading.dev.j2
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.nginx }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
