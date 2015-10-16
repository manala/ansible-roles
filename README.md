<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: Rtail

This role will install Rtail

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+
- Python
- Curl

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.rtail
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.rtail }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
