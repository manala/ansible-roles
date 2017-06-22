# Ansible Role: Mount

This role will deal with the setup of mount points.

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.mount
```

Using ansible galaxy requirements file:

```yaml
- src: manala.mount
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.mount }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
