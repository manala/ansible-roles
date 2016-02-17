<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: phantomjs

This role will assume the setup of PhantomJS.

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install elao.phantomjs,2.0
```

Using ansible galaxy requirements file:

```yaml
- src:     elao.phantomjs
  version: 2.0
```

### Ansible 1 (no longer maintained)

Using ansible galaxy cli:

```bash
ansible-galaxy install elao.phantomjs,1.0
```

Using ansible galaxy requirements file:

```yaml
- src:     elao.phantomjs
  version: 1.0
```

## Configuration example

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
