<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: cron

This role will assume the setup of cron

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install elao.cron,2.0
```

Using ansible galaxy requirements file:

```yaml
- src:     elao.cron
  version: 2.0
```

### Ansible 1 (no longer maintained)

Using ansible galaxy cli:

```bash
ansible-galaxy install elao.cron,1.0
```

Using ansible galaxy requirements file:

```yaml
- src:     elao.cron
  version: 1.0
```

## Role Handlers

| Name         | Type     | Description           |
| ------------ | -------- | --------------------- |
| cron restart | Service  |  Restart cron service |

## Role Variables

| Name            | Default | Type  | Description |
| ----------------| ------- | ----- | ----------- |
| elao_cron_files | []      | Array | Cron files  |

### Configuration example

```yaml
elao_cron_files:
  - file: app
    user: foo
    jobs:
      # Do foo bar
      - name:   foo-bar
        job:    "php /srv/app/bin/console app:foo:bar"
        minute: 0
        hour:   7
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.cron }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
