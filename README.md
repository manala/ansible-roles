# Ansible Role: Rtail

This role will deal with the setup and install of __Rtail__.

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.rtail,2.0
```

Using ansible galaxy requirements file:

```yaml
- src:     manala.rtail
  version: 2.0
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.rtail }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
