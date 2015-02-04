<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: Fail2Ban

This role will assume the basic setup of fail2ban, enhancements will soon appended.

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Dependencies

None.

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.fail2ban
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.fail2ban }
```

## Role Handlers

None

## Role Variables

None 

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.fail2ban }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)