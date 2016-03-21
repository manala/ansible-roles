# Ansible Role: Php

This role will deal with the setup and config of PHP.

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.php,2.0
```

Using ansible galaxy requirements file:

```yaml
- src:     manala.php
  version: 2.0
```

## Role Handlers

| Name              | Type    | Description     |
| ----------------- | ------- | --------------- |
| `php fpm restart` | Service | Restart php-fpm |

## Role Variables

| Name                             | Default                   | Type    | Description                                            |
| -------------------------------- | --------------------      | ------  | ------------------------------------------------------ |
| `manala_php_sapis`               | [cli, fpm]                | Array   | A list of the PHP SAPIs to install.                    |
| `manala_php_extensions`          | [ ]                       | Array   | A list of the php extensions to install.               |
| `manala_php_configs_dir_base`    | /etc/php5                 | String  | Configs directory path.                                |
| `manala_php_configs_template`    | configs/default.ini.j2    | String  | Default configuration template.                        |
| `manala_php_configs_exclusive`   | false                     | Boolean | Whether to remove all other non-specified config files |
| `manala_php_configs`             | [ ]                       | Array   | Shared configurations.                                 |
| `manala_php_fpm_configs`         | [ ]                       | Array   | PHP fpm additional configurations.                     |
| `manala_php_cli_configs`         | [ ]                       | Array   | PHP cli additional configurations.                     |
| `manala_php_fpm_pools_dir`       | /etc/php5/fpm/pool.d      | String  | PHP fpm pools directory path.                          |
| `manala_php_fpm_pools_template`  | fpm_pools/default.conf.j2 | String  | Default pool template.                                 |
| `manala_php_fpm_pools_exclusive` | false                     | Boolean | Whether to remove all other non-specified pool files   |
| `manala_php_fpm_pools`           | [ {name: www.conf} ]      | Array   | PHP fpm pools configurations.                          |

### Configuration example

#### PHP client only

```yaml
manala_php_sapis: ['cli']

manala_php_extensions:
  - curl
  - mysqlnd

manala_php_configs:
  # Load PHP extensions.
  - file:             10-extensions.ini
    template:         configs/extensions.ini.j2
  - file:             default.ini
    config:
      date.timezone:  UTC
```

#### PHP client and fpm basic setup

```yaml
manala_php_sapis: ['cli', 'fpm']

manala_php_extensions:
  - curl
  - mysqlnd
  - intl

manala_php_configs:
  - file:      10-extensions.ini
    template:  configs/extensions.ini.j2
  - file: default.ini
    config:
      date.timezone: UTC

manala_php_fpm_configs:
  - file: env_dev.ini
    # A development environment template with some preconfigured directives.
    template: configs/config_dev.ini.j2
    config:
      # default parameters
      display_errors :                   'On'
      display_startup_errors :           'On'
      error_reporting :                  E_ALL
      html_errors :                      'On'
      log_errors :                       'On'
      max_input_time :                   60
      output_buffering :                 4096
      register_argc_argv :               'Off'
      request_order :                    GP
      short_open_tag :                   'Off'
      track_errors :                     'On'
      variables_order :                  GPCS
      expose_php :                       'On'
      memory_limit :                     512M
      session.gc_divisor :               1000
      session.hash_bits_per_character :  5
      url_rewriter.tags :                a=href,area=href,frame=src,input=src,form=fakeentry
      # And add extra parameters.
      session.name:                      sid
      php_post_max_size:                 32M
  - file: env_prod.ini
    # A production environment template with some preconfigured directives.
    template: configs/config_prod.ini.j2
    config:
      # default parameters
      display_errors :                   'Off'
      display_startup_errors :           'Off'
      error_reporting :                  E_ALL & ~E_DEPRECATED & ~E_STRICT
      html_errors :                      'On'
      log_errors :                       'On'
      max_input_time :                   60
      output_buffering :                 4096
      register_argc_argv :               'Off'
      request_order :                    GP
      short_open_tag :                   'Off'
      track_errors :                     'Off'
      variables_order :                  GPCS
      expose_php :                       'Off'
      memory_limit :                     512M
      session.gc_divisor :               1000
      session.hash_bits_per_character :  5
      url_rewriter.tags :                a=href,area=href,frame=src,input=src,form=fakeentry
      # And add extra parameters.
      session.name:                      sid
      php_post_max_size:                 32M
```

#### PHP fpm pools

```yaml
manala_php_sapis: ['cli', 'fpm']

manala_php_fpm_pools:
  - file:      www.conf
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
      php_flag[display_errors]:  'true'
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.php }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
