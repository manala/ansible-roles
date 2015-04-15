<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: nodejs

This role will assume the setup of nodejs.

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Dependencies

None.

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.nodejs
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.nodejs }
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.nodejs }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
