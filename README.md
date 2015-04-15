<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: PHP

This role will assume the setup and config of PHP.

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Dependencies

None.

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.php
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.php }
```

## Role Handlers

|Name|Type|Description|
|----|----|-----------|
|`php fpm restart`|Service|Restart php-fpm

## Role Variables

| Name                      | Default              | Type   | Description                              |
| ------------------------- | -------------------- | ------ | ---------------------------------------- |
| `elao_php_sapis`          | [cli, fpm]           | Array  | A list of the PHP SAPIs to install.      |
| `elao_php_extensions`     | [ ]                  | Array  | A list of the php extensions to install. |
| `elao_php_configs_path`   | /etc/php5            | String | Configs base path.                       |
| `elao_php_configs`        | [ ]                  | Array  | Shared configurations.                   |
| `elao_php_fpm_configs`    | [ ]                  | Array  | PHP fpm additional configurations.       |
| `elao_php_cli_configs`    | [ ]                  | Array  | PHP cli additional configurations.       |
| `elao_php_fpm_pools_path` | /etc/php5/fpm/pool.d | String | PHP fpm pools base path.                 |
| `elao_php_fpm_pools`      | [ {name: www.conf} ] | Array  | PHP fpm pools base path.                 |


### Configuration example

#### PHP client only

```yaml
elao_php_sapis: ['cli']

elao_php_extensions:
  - curl
  - mysqlnd

elao_php_configs:
  # Load PHP extensions.
  - name:             10-extensions.ini
    template:         configs/extensions.ini.j2
  - name:             default.ini
    config:
      date.timezone:  UTC
```

#### PHP client and fpm basic setup

```yaml
elao_php_sapis: ['cli', 'fpm']

elao_php_extensions:
  - curl
  - mysqlnd
  - intl

elao_php_configs:
  - name:      10-extensions.ini
    template:  configs/extensions.ini.j2
  - name: default.ini
    config:
      date.timezone: UTC

elao_php_cli_configs:
  - name:     default-cli.ini
    # A development environment template with some preconfigured directives.
    template: configs/config_dev.ini.j2
    config:
      # We override the default memory limit.
      memory_limit:      1024M
      # And add extra parameters.
      session.name:      sid
      php_post_max_size: 32M
```

#### PHP fpm pools

```yaml
elao_php_sapis: ['cli', 'fpm']

elao_php_fpm_pools:
  - name:      www.conf
    # default template
    template: fpm_pools/default.conf.j2
    config:
      # default parameters
      name:                      www
      user:                      www-data
      group:                     www-data
      listen:                    127.0.0.1:  9000
      listen.backlog:            128
      listen.owner:              www-data
      listen.group:              www-data
      pm:                        dynamic
      pm.max_children:           5
      pm.start_servers:          2
      pm.min_spare_servers:      1
      pm.max_spare_servers:      3
      # add extra parameters
      request_slowlog_timeout:   30s
      env[HOSTNAME]:             $HOSTNAME
      php_flag[display_errors]:  true
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.php }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
