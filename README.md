# Ansible Role: Beanstalkd

This role will deal with the setup of [beanstalkd](http://kr.github.io/beanstalkd/)

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.beanstalkd
```

Using ansible galaxy requirements file:

```yaml
- src: manala.beanstalkd
```

## Role Handlers

None.

## Role Variables

### Definition

| Name                             | Default  | Type   | Description     |
| -------------------------------- | -------- | ------ | --------------- |

### Example

```yaml
- hosts: all
  roles:
    - role: manala.beanstalkd
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
