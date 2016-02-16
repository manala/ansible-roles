<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

[![Ansible Role](https://img.shields.io/ansible/role/5559.svg?style=plastic)](https://galaxy.ansible.com/list#/roles/5559) [![Platforms](https://img.shields.io/badge/platforms-debian-lightgrey.svg?style=plastic)](#) [![License](http://img.shields.io/:license-mit-lightgrey.svg?style=plastic)](#)

# Ansible Role: Nginx

This role will assume the setup and config of nginx

It's part of the ELAO <a href="http://www.manalas.com" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

- Ansible 1.9.0+

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install elao.nginx,2.0
```

Using ansible galaxy requirements file:

```yaml
- src:     elao.nginx
  version: 2.0
```

### Ansible 1 (no longer maintained)

Using ansible galaxy cli:

```bash
ansible-galaxy install elao.nginx,1.0
```

Using ansible galaxy requirements file:

```yaml
- src:     elao.nginx
  version: 1.0
```

## Role Handlers

| Name            | Type    | Description          |
| --------------- | ------- | -------------------- |
| `nginx restart` | Service | Restart nginx server |

## Role Variables

| Name                            | Default                     | Type    | Description                                 |
| ------------------------------- | --------------------------- | ------- | ------------------------------------------- |
| `elao_nginx_config_template`    | config/http_default.conf.j2 | String  | Main config template                        |
| `elao_nginx_config`             | {}                          | Array   | Main config                                 |
| `elao_nginx_configs`            | {}                          | Array   | Configs                                     |
| `elao_nginx_configs_template`   | configs/empty.conf.j2       | String  | Template to use to define a host            |
| `elao_nginx_configs_exclusive`  | false                       | Boolean | Exclusion of existings files                |
| `elao_nginx_configs_dir`        | /etc/nginx/conf.d           | String  | Path to the main configuration directory    |
| `elao_nginx_user`               | www-data                    | String  | User running nginx                          |
| `elao_nginx_log_dir`            | /var/log/nginx              | String  | Directory where Nginx will store is logs    |


### Nginx configuration

The `elao_nginx_config_template` key will allow you to use differents main configuration templates. The role is shipped with basic templates :

- base (Simple template with no default configuration)
- dev (This configuration will keep serving NGINX informations like server tokens and provide directives for Vagrant VM)
- test
- prod (For production purpose. Cleaning all sensible server informations)

#### Example:
```yaml
elao_nginx_config_template: config/http_dev.conf.j2
```

The `elao_nginx_config` key is made to allow you to alter main Nginx configuration templates.

#### Example:

```yaml
elao_nginx_config:
  user: nginx
  events:
    worker_connections: 1024
```

### Exclusivity

`elao_nginx_configs_exclusive` allow you to clean up existing nginx configuration files into directory defined by the `elao_nginx_configs_dir` key. Made to be sure no old or manualy created files will alter current configuration.

```yaml
elao_nginx_configs_exclusive: true
```

### Hosts configuration

The `elao_nginx_configs` key is made to define Nginx host configuration.

```yaml
elao_nginx_config:
  user: nginx
  events:
    worker_connections: 1024
elao_nginx_configs:
  - file: test.conf
    template: configs/server_default.conf.j2
    config:
      - listen: 8080
      - location /:
        - root:  /srv/foo
  - file: symfony2.conf
    template: configs/server_symfony2.conf.j2
    config:
      - server_name: symfony2.dev
      - root: /srv/symfony2/web
      - access_log:  "{{ elao_nginx_log_dir }}/app.access.log"
      - error_log:   "{{ elao_nginx_log_dir }}/app.error.log"
      - client_max_body_size: 8G
      - include:     conf.d/gzip
      - location ^~ /sf/:
        - alias: "/usr/share/symfony/symfony-1.4/data/web/sf/"
      - location /:
        - try_files: $uri /index.php$is_args$args
      - location ~ ^/(index|frontend_dev)\.php(/|$):
        - include: conf.d/php_fpm_params
  - file: wp.conf
    template: configs/server_wordpress.conf.j2
    config:
      - listen: 80
      - location /:
        - root:  /srv/wordpress/
  - file: pma.conf
    template: configs/server_php.conf.j2
    config:
      - server_name:          pma.my_domain.com
      - listen:               "{{ ansible_venet0_0.ipv4.address }}:80"
      - root:                 /opt/phpmyadmin
      - include:              conf.d/gzip
      - client_max_body_size: 16M
      - location /:
        - try_files: $uri /index.php$is_args$args
```

### Logs rotation

Assuming you want to rotate your logs 3 templates are provided:

- Empty:  You want to handle yourself your logrotate strategy
- Base:   Most distro basic configuration with a daily rotation
- Weekly: Configuration with a weekly rotation

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.nginx }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
