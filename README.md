# Ansible Role: Mailhog

This role will deal with the setup and the config of mailhog

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

A debian repository with mailhog package (such as manala one).

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.mailhog
```

Using ansible galaxy requirements file:

```yaml
- src: manala.mailhog
```

## Role Handlers

None.

## Role Variables

### Definition

| Name                             | Default  | Type   | Description     |
| -------------------------------- | -------- | ------ | --------------- |
| `manala_mailhog_config_template` | ~        | String | Config template |
| `manala_mailhog_config`          | []       | Array  | Config          |

### Example

```yaml
- hosts: all
  vars:
    manala_mailhog_config_template: config/dev.j2
    manala_mailhog_config:
      - ui-bind-addr: 0.0.0.0:8080
  roles:
    - role: manala.mailhog
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)