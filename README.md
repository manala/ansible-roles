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
ansible-galaxy install manala.env
```

Using ansible galaxy requirements file:

```yaml
- src: manala.env
```

## Role Variables

| Name                   | Default | Type  | Description            |
| ---------------------- | ------- | ----- | ---------------------- |
| `manala_env_variables` | []      | Array |  Environment variables |

### Configuration example

```yaml
manala_env_variables:
  - FOO: bar
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
