# Ansible Role: Environment

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
ansible-galaxy install manala.environment
```

Using ansible galaxy requirements file:

```yaml
- src: manala.environment
```

## Role Variables

| Name                           | Default | Type    | Description            |
| ------------------------------ | ------- | ------- | ---------------------- |
| `manala_environment_variables` | []      | Array   |  Environment variables |

### Configuration example

```yaml
manala_environment_variables:
  - FOO: bar
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.environment }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
