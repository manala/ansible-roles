<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: phantomjs

This role will assume the setup of PhantomJS.

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Dependencies

None.

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.phantomjs
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.phantomjs }
```
### Configuration example

```yaml
elao_phantomjs_config:
  webdriver: 4444
  'webdriver-logfile': /var/log/phantomjs.log
  'webdriver-loglevel': DEBUG
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.phantomjs }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
