# Ansible Role: Phantomjs [![Build Status](https://travis-ci.org/manala/ansible-role-phantomjs.svg?branch=master)](https://travis-ci.org/manala/ansible-role-phantomjs)

This role will deal with the setup of PhantomJS.

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

This role is made to work with the __manala__ phantomjs debian package, available on the __manala__ debian repository. Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

```yaml
manala_apt_repositories:
 - manala
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
