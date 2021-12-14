# Ansible Role: Cron [![Build Status](https://travis-ci.org/manala/ansible-role-cron.svg?branch=master)](https://travis-ci.org/manala/ansible-role-cron)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of __Cron__.

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

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

| Name          | Type    | Description          |
| ------------- | ------- | -------------------- |
| `cron restart | Service | Restart cron service |

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Configuration example

```yaml
manala_cron_files_defaults:
  user: foo # Override default "root" user
```

```yaml
manala_cron_files:
  - file: app
    user: foo # Default jobs user
    env:
      FOO: foo
    jobs:
      # ⚠️ In this example, you must **explicitly** set the minute option to `0` to have the job run at a specific hour,
      # otherwise the default value `*` will run it _every minute_ for an hour.
      - command: php /srv/app/bin/console app:foo:bar
        minute: 0
        hour: 7
      - command: php /srv/app/bin/console app:foo:bar
        user: bar # Override default jobs user
        minute: 0
        hour: 7
  # Template based
  - file: template
    template: my/cron.j2
  # Raw content based
  - file: content
    config: |
      0 7 * * * root cd /srv/app && bin/console app:bar:bar
  # Ensure file is absent
  - file: absent
    state: absent # "present" by default
  # Ignore file
  - file: ignore
    state: ignore
  # Flatten files
  - "{{ my_custom_files_array }}"
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - role: manala.cron
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
