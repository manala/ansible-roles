# Ansible Role: Env

This role will deal with the setup of environment variables

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.env,2.0
```

Using ansible galaxy requirements file:

```yaml
- src:     manala.env
  version: 2.0
```

## Role Variables

| Name                | Default | Type  | Description            |
| ------------------- | ------- | ----- | ---------------------- |
| `manala_env_config` | {}      | Array |  Environment variables |

### Configuration example

```yaml
manala_env_config:
  foo: bar
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.env }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
