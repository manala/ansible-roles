# Ansible Role: Phantomjs

This role will deal with the setup of PhantomJS.

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.phantomjs,2.0
```

Using ansible galaxy requirements file:

```yaml
- src:     manala.phantomjs
  version: 2.0
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
