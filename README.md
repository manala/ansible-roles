<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: env

This role will assume the setup of environment variables

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Dependencies

None.

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.env
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.env }
```

## Role Variables

| Name              | Default | Type  | Description            |
| ----------------- | ------- | ----- | ---------------------- |
| `elao_env_config` | {}      | Array |  Environment variables |

### Configuration example

```yaml
elao_env_config:
  foo: bar
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.env }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
