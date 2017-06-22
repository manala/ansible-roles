# Ansible Role: pam-ssh-agent-auth

This role will deal with the setup and config of [pam-ssh-agent-auth](http://pamsshagentauth.sourceforge.net/).

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

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
