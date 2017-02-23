# Ansible Role: Nginx

This role will deal with the setup and config of nginx

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

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

| Name                              | Default           | Type    | Description                                 |
| --------------------------------- | ----------------- | ------- | ------------------------------------------- |
| `manala_nginx_config_template`    | config/default.j2 | String  | Main config template                        |
| `manala_nginx_config`             | {}                | Array   | Main config                                 |
| `manala_nginx_configs`            | {}                | Array   | Configs                                     |
| `manala_nginx_configs_template`   | configs/empty.j2  | String  | Template to use to define a host            |
| `manala_nginx_configs_exclusive`  | false             | Boolean | Exclusion of existings files                |
| `manala_nginx_configs_dir`        | /etc/nginx/conf.d | String  | Path to the main configuration directory    |
| `manala_nginx_user`               | www-data          | String  | User running nginx                          |
| `manala_nginx_log_dir`            | /var/log/nginx    | String  | Directory where Nginx will store is logs    |


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
  - events:
    - worker_connections: 1024
```

### Exclusivity

`manala_nginx_configs_exclusive` allow you to clean up existing nginx configuration files into directory defined by the `manala_nginx_configs_dir` key. Made to be sure no old or manualy created files will alter current configuration.

```yaml
manala_nginx_configs_exclusive: true
```

### Hosts configuration

The `manala_nginx_configs` key is made to define Nginx host configuration.

```yaml
manala_nginx_config:
  - user: nginx
  - events:
    - worker_connections: 1024
manala_nginx_configs:
  - file: test.conf
    template: configs/server.j2
    config:
      - listen: 8080
      - location /:
        - root:  /srv/foo
  - file: symfony2.conf
    template: configs/server.j2
    config:
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
  - file: wp.conf
    template: configs/server.j2
    config:
      - listen: 80
      - location /:
        - root:  /srv/wordpress/
  - file: pma.conf
    template: configs/server.j2
    config:
      - server_name:          pma.my_domain.com
      - listen:               "{{ ansible_venet0_0.ipv4.address }}:80"
      - root:                 /opt/phpmyadmin
      - include:              conf.d/gzip
      - client_max_body_size: 16M
      - location /:
        - try_files: $uri /index.php$is_args$args
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
