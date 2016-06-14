# Ansible Role: cron

This role will deal with the setup of __cron__.

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.cron
```

Using ansible galaxy requirements file:

```yaml
- src: manala.cron
```


## Role Handlers

| Name         | Type     | Description           |
| ------------ | -------- | --------------------- |
| cron restart | Service  |  Restart cron service |

## Role Variables

| Name              | Default | Type  | Description |
| ----------------- | ------- | ----- | ----------- |
| manala_cron_files | []      | Array | Cron files  |

### Configuration example

```yaml
manala_cron_files:
  - file: app
    user: foo
    environment:
      - FOO: bar
    jobs:
      # Do foo bar
      - name:   foo-bar
        job:    "php /srv/app/bin/console app:foo:bar"
        minute: 0
        hour:   7
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.cron }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
