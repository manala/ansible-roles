<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: composer

This role will assume the setup of [composer](https://getcomposer.org)

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Dependencies

This role requires php-cli >=5.3.2. You can use [elao.php](https://github.com/ElaoInfra/ansible-role-php) role.

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.composer
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.composer }
```

## Role Handlers

None.

## Role Variables

### Configuration paths

| Name                                        | Default                        | Type        | Description            |
| ------------------------------------------- | ------------------------------ | ----------- | ---------------------- |
| `elao_composer_bin`                         | /usr/local/bin/composer        | String      | Composer bin path.     |
| `elao_composer_home`                        | ~/.composer                    | String      | Composer home path.    |
| `elao_composer_config_auth`                 | { }                            | Array       | Composer auth config.  |

### Configuration definitions

| Name                        | Default         | Type        | Description                            |
| --------------------------- | --------------- | ----------- | -------------------------------------- |
| `elao_composer_config.auth` | Emptycollection | Collection  | Definition of composer authentication. |

### Configuration example

#### Composer configuration with github token

```
elao_composer_config:
  auth:
    github-oauth:
      github.com: <your-github-token>
```

#### Composer configuration with global packages

```
elao_composer_home: /home/vagrant/.composer
elao_composer_packages:
  - name:     phpunit/phpunit
    version:  '@stable'
    bin_dir:  /usr/local/bin
  - name:     squizlabs/php_codesniffer
    version:  '@stable'
    bin_dir:  /usr/local/bin
```

## Example playbook

    - hosts: servers
      roles:
        - { role: elao.composer }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
