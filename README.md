# Ansible Role: Mailhog

This role will deal with the setup and the config of mailhog

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

This role is made to work with the __manala__ mailhog debian package, available on the __manala__ debian repository. Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

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
    manala_mailhog_config_template: config/default.dev.j2
    manala_mailhog_config:
      - ui-bind-addr: 0.0.0.0:8080
  roles:
    - role: manala.mailhog
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
