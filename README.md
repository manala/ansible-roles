<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: logrotate

This role will assume the setup of logrotate

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Dependencies

None.

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.logrotate
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.logrotate }
```

## Role Handlers

None

## Role Variables

| Name                             | Default                | Type   | Description          |
| -------------------------------- | ---------------------- | ------ | -------------------- |
| `elao_logrotate_config_template` | config/default.conf.j2 | String | Main config template |
| `elao_logrotate_config`          | {}                     | Array  | Main config          |
| `elao_logrotate_configs_path`    | /etc/logrotate.d       | String | Configs path         |
| `elao_logrotate_configs`         | []                     | Array  | Configs              |

### Configuration examples

```yaml
elao_logrotate_config:
  daily: true
  create: 0640 www-data adm
  ifempty: true
  rotate: 5
  prerotate: |
    if [ -d /etc/logrotate.d/httpd-prerotate ]; then \
      run-parts /etc/logrotate.d/httpd-prerotate; \
    fi; \
```

```yaml
elao_logrotate_configs:
  - name:      nginx
    template:  configs/nginx.j2
    config:
      size:    100M
```

```yaml
elao_logrotate_configs:
  - name: nginx_example
    config:
      ? |
        /var/log/nginx/example/access.log
        /var/log/nginx/example/error.log
      :
        size:           200M
        missingok:      true
        rotate:         0
        compress:       true
        delaycompress:  true
        notifempty:     true
        create:         0640 www-data adm
        sharedscripts:  true
        prerotate: |
          if [ -d /etc/logrotate.d/httpd-prerotate ]; then \
            run-parts /etc/logrotate.d/httpd-prerotate; \
          fi \
        postrotate: |
          [ -s /run/nginx.pid ] && kill -USR1 `cat /run/nginx.pid`
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.logrotate }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
