# Ansible Role: Composer

This role will deal with the setup of [composer](https://getcomposer.org)

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

This role requires php-cli >=5.3.2. You can use [manala.php](https://github.com/manala/ansible-role-php) role.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.composer,2.0
```

Using ansible galaxy requirements file:

```yaml
- src:     manala.composer
  version: 2.0
```

## Role Handlers

None.

## Role Variables

### Configuration paths

| Name                                          | Default                        | Type        | Description            |
| --------------------------------------------- | ------------------------------ | ----------- | ---------------------- |
| `manala_composer_bin`                         | /usr/local/bin/composer        | String      | Composer bin path.     |
| `manala_composer_home`                        | ~/.composer                    | String      | Composer home path.    |
| `manala_composer_config_auth`                 | { }                            | Array       | Composer auth config.  |

### Configuration definitions

| Name                          | Default         | Type        | Description                            |
| ----------------------------- | --------------- | ----------- | -------------------------------------- |
| `manala_composer_config.auth` | Emptycollection | Collection  | Definition of composer authentication. |

### Configuration example

#### Composer configuration with github token

```yaml
manala_composer_config:
  auth:
    github-oauth:
      github.com: <your-github-token>
```

#### Composer configuration with global packages

```yaml
manala_composer_home: /home/vagrant/.composer
manala_composer_packages:
  - name:     phpunit/phpunit
    version:  '@stable'
    bin_dir:  /usr/local/bin
  - name:     squizlabs/php_codesniffer
    version:  '@stable'
    bin_dir:  /usr/local/bin
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.composer }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
