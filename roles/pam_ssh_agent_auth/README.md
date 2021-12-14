# Ansible Role: Pam ssh agent auth [![Build Status](https://travis-ci.org/manala/ansible-role-pam_ssh_agent_auth.svg?branch=master)](https://travis-ci.org/manala/ansible-role-pam_ssh_agent_auth)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup and config of [Pam ssh agent auth](http://pamsshagentauth.sourceforge.net/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

This role is made to work with the __manala__ libpam-ssh-agent-auth debian package, available on the __manala__ debian repository. Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

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
ansible-galaxy install manala.pam_ssh_agent_auth
```

Using ansible galaxy requirements file:

```yaml
- src: manala.pam_ssh_agent_auth
```

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

## Example playbook

```yaml
- hosts: servers
  roles:
    - role: manala.pam_ssh_agent_auth
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
