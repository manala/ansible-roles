<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: Heka

This role will install Heka

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+
- Python
- Curl

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.heka
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.heka }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
