# Ansible Role: Nginx

This role will deal with the setup and config of [Nginx](https://nginx.org/en/).

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

This role is made to work with the official __nginx__ debian packages, available on the __nginx__ debian repository. Please use the [**manala.roles.apt**](../apt/) role to handle it properly.

```yaml
manala_apt_preferences:
  - nginx@nginx
```

## Dependencies

None.

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Nginx configuration

The `manala_nginx_config_template` key will allow you to use main configuration templates. The role is shipped with default upstream template:
```yaml
manala_nginx_config_template: config/nginx/nginx.conf.j2
```

But you can feel free to use your owns:
```yaml
manala_nginx_config_template: my/nginx.conf.j2
```

The `manala_nginx_config` key is made to allow you to alter main Nginx configuration template.

#### Examples:

Use dict:
```yaml
manala_nginx_config:
  user: nginx
  worker_processes: 1
```

Use raw content:
```yaml
manala_nginx_config: |
  user nginx;
  worker_processes 1;
```

### Exclusivity

`manala_nginx_configs_exclusive` allow you to clean up existing nginx configuration files into directory defined by the `manala_nginx_configs_dir` key. Made to be sure no old or manually created files will alter current configuration.

```yaml
manala_nginx_configs_exclusive: true
```

### Configurations

The `manala_nginx_configs` key is made to define Nginx configurations.

A state (present|absent|ignore) can be provided.

```yaml
manala_nginx_configs:
  # Template based
  - file: template.conf
    template: my/template.conf.j2
  # Dict based
  - file: dict.conf
    config:
      listen: 80 default_server
      server_name: example.com www.example.com
  # Raw content based
  - file: content.conf
    config: |
      server {
          listen 80 default_server;
          listen [::]:80 default_server;
          server_name example.com www.example.com;
          root /var/www/example.com;
          index index.html;
          try_files $uri /index.html;
      }
  # Ensure config is absent
  - file: absent.conf
    state: absent # "present" by default
  # Ignore config
  - file: ignore.conf
    state: ignore
  # Flatten configs
  - "{{ my_custom_configs_array }}"
```

## Example playbook

```yaml
- hosts: servers
  tasks:
    - ansible.builtin.import_role:  
        name: manala.roles.nginx
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
