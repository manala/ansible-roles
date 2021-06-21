# Ansible Role: PhantomJS [![Build Status](https://travis-ci.org/manala/ansible-role-phantomjs.svg?branch=master)](https://travis-ci.org/manala/ansible-role-phantomjs)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of [PhantomJS](http://phantomjs.org/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

This role is made to work with the __manala__ phantomjs debian package, available on the __manala__ debian repository. Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

```yaml
manala_apt_preferences:
  - phantomjs@manala
```

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.phantomjs
```

Using ansible galaxy requirements file:

```yaml
- src: manala.phantomjs
```

## Role Variables

### Definition

| Name                                        | Default       | Type   | Description                            |
| ------------------------------------------- | ------------- | ------ | -------------------------------------- |
| `manala_phantomjs_install_packages`         | ~             | Array  | Dependency packages to install         |
| `manala_phantomjs_install_packages_default` | ['phantomjs'] | Array  | Default dependency packages to install |
| `manala_phantomjs_config_template`          | ~             | String | Configuration template path            |
| `manala_phantomjs_config`                   | []            | Array  | Configuration                          |

## Configuration example

```yaml
manala_phantomjs_config:
  - webdriver:          4444
  - webdriver-logfile:  /var/log/phantomjs.log
  - webdriver-loglevel: DEBUG
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.phantomjs }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
