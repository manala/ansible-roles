# Ansible Role: Php [![Build Status](https://travis-ci.org/manala/ansible-role-php.svg?branch=master)](https://travis-ci.org/manala/ansible-role-php)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup and config of PHP.

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

This role is made to work with the [__dotdeb__](https://www.dotdeb.org/) or [__sury__](https://deb.sury.org/) php debian repositories. Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle them properly.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.php
```

Using ansible galaxy requirements file:

```yaml
- src: manala.php
```

## Role Handlers

| Name                          | Type    | Description                                           |
| ----------------------------- | ------- | ----------------------------------------------------- |
| `php fpm restart`             | Service | Check php fpm configuration and restart service if ok |
| `php blackfire agent restart` | Service | Restart php blackfire agent service                   |

## Role Variables

| Name                                          | Default                       | Type                 | Description                                             |
| --------------------------------------------- | ----------------------------- | -------------------- | ------------------------------------------------------- |
| `manala_php_version`                          | ~                             | String,Integer,Float | Php version                                             |
| `manala_php_sapis_exclusive`                  | false                         | Boolean              | Should the SAPIs list be exclusive ?                    |
| `manala_php_sapis`                            | ~                             | Array                | A list of PHP SAPIs                                     |
| `manala_php_sapis_default`                    | ['cli', 'fpm']                | Array                | Default list of PHP SAPIs                               |
| `manala_php_extensions_exclusive`             | false                         | Boolean              | Should the extensions list be exclusive ?               |
| `manala_php_extensions`                       | []                            | Array                | A list of PHP extensions                                |
| `manala_php_configs_template`                 | 'configs/empty.j2'            | String               | Configs base template path                              |
| `manala_php_configs_exclusive:`               | false                         | Boolean              | Should configs files be exclusive ?                     |
| `manala_php_configs`                          | []                            | Array                | Configs files                                           |
| `manala_php_cli_configs`                      | []                            | Array                | Configs files (cli SAPI only)                           |
| `manala_php_fpm_configs`                      | []                            | Array                | Configs files (fpm SAPI only)                           |
| `manala_php_cgi_configs`                      | []                            | Array                | Configs files (cgi SAPI only)                           |
| `manala_php_phpdbg_configs`                   | []                            | Array                | Configs files (phpdbg SAPI only)                        |
| `manala_php_fpm_pools_template`               | 'fpm_pools/empty.j2'          | String               | Fpm pools base template path                            |
| `manala_php_fpm_pools_exclusive`              | false                         | Boolean              | Should fpm pools files be exclusive ?                   |
| `manala_php_fpm_pools`                        | []                            | Array                | Fpm pools files                                         |
| `manala_php_blackfire`                        | false                         | Boolean              | Install blackfire                                       |
| `manala_php_blackfire_agent_config_file`      | '/etc/blackfire/agent'        | String               | Blackfire agent config file path                        |
| `manala_php_blackfire_agent_config_template`  | 'blackfire/agent/default.j2'  | String               | Blackfire agent config base template path               |
| `manala_php_blackfire_agent_config`           | []                            | Array                | Blackfire agent config                                  |
| `manala_php_blackfire_client_config_file`     | '~/.blackfire.ini'            | String               | Blackfire client config file path                       |
| `manala_php_blackfire_client_config_template` | 'blackfire/client/default.j2' | String               | Blackfire client config base template path              |
| `manala_php_blackfire_client_config`          | []                            | Array                | Blackfire client config                                 |
| `manala_php_applications_dir`                 | '/usr/local/bin'              | String               | Applications directory path                             |
| `manala_php_applications`                     | []                            | Array                | A list of php applications                              |

### Configuration example

#### Version matrix

| Version | Distribution | Repository | *manala_apt_preferences* | *manala_php_version* | *manala_php_extensions_pecl_versioned* |
| :---    | :---:        | :---:      | ---:                     | ---:                 | ---:                                   |
| **5.6** | Jessie       | Sury       | `php@sury_php`           | `5.6`                |                                        |
| **5.6** | Stretch      | Sury       | `php@sury_php`           | `5.6`                |                                        |
| **5.6** | Buster       | Sury       | `php@sury_php`           | `5.6`                |                                        |
| **7.0** | Jessie       | Dotdeb     | `php@dotdeb`             | `7.0`                | `true`                                 |
| **7.0** | Jessie       | Sury       | `php@sury_php`           | `7.0`                |                                        |
| **7.0** | Stretch      | Sury       | `php@sury_php`           | `7.0`                |                                        |
| **7.0** | Buster       | Sury       | `php@sury_php`           | `7.0`                |                                        |
| **7.1** | Jessie       | Sury       | `php@sury_php`           | `7.1`                |                                        |
| **7.1** | Stretch      | Sury       | `php@sury_php`           | `7.1`                |                                        |
| **7.1** | Buster       | Sury       | `php@sury_php`           | `7.1`                |                                        |
| **7.2** | Jessie       | Sury       | `php@sury_php`           | `7.2`                |                                        |
| **7.2** | Stretch      | Sury       | `php@sury_php`           | `7.2`                |                                        |
| **7.2** | Buster       | Sury       | `php@sury_php`           | `7.2`                |                                        |
| **7.3** | Jessie       | Sury       | `php@sury_php`           | `7.3`                |                                        |
| **7.3** | Stretch      | Sury       | `php@sury_php`           | `7.3`                |                                        |
| **7.3** | Buster       | Sury       | `php@sury_php`           | `7.3`                |                                        |
| **7.4** | Jessie       | Sury       | `php@sury_php`           | `7.4`                |                                        |
| **7.4** | Stretch      | Sury       | `php@sury_php`           | `7.4`                |                                        |
| **7.4** | Buster       | Sury       | `php@sury_php`           | `7.4`                |                                        |

#### Sapis

```yaml
manala_php_sapis_exclusive: true # Ensure other sapis are automatically absents
manala_php_sapis:
  - cli
  - fpm
  - sapi:  cgi
    state: absent
```

#### Extensions

```yaml
manala_php_extensions_exclusive: true # Ensure other extensions are automatically absents
manala_php_extensions:
  - intl
  - gd
  - extension: gd
    state:     absent
  - extension: xdebug
    enabled:   false # Ensure extension will be installed *but* disabled
```

#### Configs

A state (present|absent) can be provided.

All sapis
```yaml
manala_php_configs_exclusive: true # Ensure other configs are automatically absents
manala_php_configs:
  # Template based
  - file: foo_template.ini
    template: configs/default.dev.j2
  # Config based, empty template by default
  - file: foo.ini
    config:
      - date.timezone: UTC
  # Raw content based
  - file: foo_content.ini
    content: |
      memory_limit = 512M
    state: absent
```

Sapis specific
```yaml
# Fpm
manala_php_fpm_configs:
  - file: app.ini
    # A development environment template with some preconfigured directives.
    template: configs/default.dev.j2
    config:
      - max_input_time:   60
      - output_buffering: 4096
      - expose_php:       true
      - memory_limit:     512M

# Cli
manala_php_cli_configs:
  - file: app.ini
    # A development environment template with some preconfigured directives.
    template: configs/default.staging.j2
    config:
      - max_input_time:   -1
      - output_buffering: 4096
      - expose_php:       false
      - memory_limit:     2G
```

#### Fpm pools

```yaml
manala_php_fpm_pools:
  - file: www.conf
    config:
      - www:
        - pm.max_children:          5
        - pm.start_servers:         2
        - pm.min_spare_servers:     1
        - pm.max_spare_servers:     3
        - env:
            FOO:     bar
            APP_ENV: prod
        - php_flag[display_errors]: true
```

#### Applications:

Installation of specific php applications

```
  php_applications:
    - drush@8.1.18
```

##### List of available applications:

- phpcs
- phpcbf
- openl10n
- phpunit
- php-cs-fixer
- couscous
- security-checker
- deptrac
- wp-cli
- drush

#### Blackfire

```yaml
manala_php_blackfire: true

manala_php_blackfire_agent_config:
  - server-id: your-server-id
  - server-token: your-token-id

manala_php_blackfire_client_config:
  - client-id: your-client-id
  - client-token: your-client-token
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
