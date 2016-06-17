# Ansible Role: Fail2Ban

This role will assume the setup of fail2ban

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.fail2ban
```

Using ansible galaxy requirements file:

```yaml
- src: manala.fail2ban
```

## Role Handlers

None

## Role Variables

None

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.fail2ban }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
