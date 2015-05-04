<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: Nginx

This role will assume the setup and config of nginx

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Dependencies

None.

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.nginx
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.nginx }
```

## Role Handlers

| Name            | Type    | Description          |
| --------------- | ------- | -------------------- |
| `nginx restart` | Service | Restart nginx server |

## Role Variables

| Name                         | Default                     | Type   | Description          |
| ---------------------------- | --------------------------- | ------ | -------------------- |
| `elao_nginx_config_template` | config/http_default.conf.j2 | String | Main config template |
| `elao_nginx_config`          | {}                          | Array  | Main config          |
| `elao_nginx_configs`         | {}                          | Array  | Configs              |

### Configuration example

```yaml
elao_nginx_config:
  user: nginx
  events:
    worker_connections: 1024
elao_nginx_configs:
  - file: test.conf
    template: configs/server_default.conf.j2
    config:
      listen: 8080
      location /:
        root:  /srv/foo
  - file: symfony2.conf
    template: configs/server_symfony2.conf.j2
    config:
      server_name: symfony2.dev
      root: /srv/symfony2/web
      indexes:
        - app
        - app_dev
        - app_test
      client_max_body_size: 8G
  - file: wp.conf
    template: configs/server_wordpress.conf.j2
    config:
      listen: 80
      location /:
        root:  /srv/wordpress/
  - file: pma.conf
    template: configs/server_php.conf.j2
    config:
      server_name:    pma.my_domain.com
      listen:         "{{ ansible_venet0_0.ipv4.address }}:80"
      root:           /opt/phpmyadmin
      fastcgi_index:  index.php
      indexes:
        - index
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.nginx }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
