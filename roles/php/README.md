# Ansible Role: Php

This role will deal with the setup and config of PHP.

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

This role is made to work with the [__sury__](https://deb.sury.org/) php debian repositories. Please use the [**manala.roles.apt**](../apt/) role to handle it properly.

```yaml
manala_apt_preferences:
  - php@sury_php
```

## Dependencies

None.

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Configuration example

#### Version

```yaml
manala_php_version: 7.4
```

#### Sapis

```yaml
manala_php_sapis_exclusive: true # Ensure other sapis are automatically absents
manala_php_sapis:
  - cli
  - fpm
  # Ensure sapi is absent
  - sapi: cgi
    state: absent
  # Ignore sapi
  - sapi: phpdbg
    state: ignore
```

#### Extensions

```yaml
manala_php_extensions_exclusive: true # Ensure other extensions are automatically absents
manala_php_extensions:
  - intl
  - gd
  - extension: xdebug
    enabled: false # Ensure extension will be installed *but* disabled
  # Ensure extension is absent
  - extension: gd
    state: absent
  # Ignore extension
  - extension: xml
    state: ignore
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
  # Config based
  - file: foo.ini
    config:
      date.timezone: UTC
  # Raw content based
  - file: foo_content.ini
    config: |
      memory_limit = 512M
  # Ensure config is absent
  - file: absent.ini
    state: absent # "present" by default
  # Ignore config
  - file: ignore.ini
    state: ignore
  # Flatten configs
  - "{{ my_custom_configs_array }}"
```

Sapis specific
```yaml
# Fpm
manala_php_fpm_configs:
  - file: app.ini
    config:
      max_input_time: 60
      output_buffering: 4096
      expose_php: true
      memory_limit: 512M

# Cli
manala_php_cli_configs:
  - file: app.ini
    config:
      max_input_time: -1
      output_buffering: 4096
      expose_php: false
      memory_limit: 2G
```

#### Fpm pools

```yaml
manala_php_fpm_pools:
  - file: www.conf
    config:
      www:
        pm.max_children: 5
        pm.start_servers: 2
        pm.min_spare_servers: 1
        pm.max_spare_servers: 3
        env:
          FOO: bar
          APP_ENV: prod
        php_flag:
          display_errors: true
  # Content based
  - file: content.conf
    config: |
      [www]
      user = foo
      group = foo
  # Ensure pool is absent
  - file: absent.conf
    state: absent # "present" by default
  # Ignore pool
  - file: ignore.conf
    state: ignore
  # Flatten configs
  - "{{ my_custom_pools_array }}"
```

#### Applications:

Installation of specific php applications

```yaml
manala_php_applications:
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
  server-id: your-server-id
  server-token: your-token-id

manala_php_blackfire_client_config:
  client-id: your-client-id
  client-token: your-client-token
```

## Example playbook

```yaml
- hosts: servers
  tasks:
    - ansible.builtin.import_role:  
        name: manala.roles.php
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
