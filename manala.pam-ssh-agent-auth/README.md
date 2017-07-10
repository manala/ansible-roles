# Ansible Role: Pam ssh agent auth [![Build Status](https://travis-ci.org/manala/ansible-role-pam-ssh-agent-auth.svg?branch=master)](https://travis-ci.org/manala/ansible-role-pam-ssh-agent-auth)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup and config of [Pam ssh agent auth](http://pamsshagentauth.sourceforge.net/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

This role is made to work with the __manala__ pam-ssh-agent-auth debian package, available on the __manala__ debian repository. Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

```yaml
manala_apt_preferences:
 - pam-ssh-agent-auth@manala
```

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.pam-ssh-agent-auth
```

Using ansible galaxy requirements file:

```yaml
- src: manala.pam-ssh-agent-auth
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.pam-ssh-agent-auth }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
