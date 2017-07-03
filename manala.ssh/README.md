# Ansible Role: SSH [![Build Status](https://travis-ci.org/manala/ansible-role-ssh.svg?branch=master)](https://travis-ci.org/manala/ansible-role-ssh)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the following configuration:
- Allow sudo authentication over ssh
- Enable/Disable the SSH daemon password authentication
- Set the SSH daemon accepted environment variables
- Set ssh know hosts

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.ssh
```

Using ansible galaxy requirements file:

```yaml
- src: manala.ssh
```

## Role Handlers

|Name|Action|Description|
|----|----|-----------|-------|
`sudo restart`|Service restarted|Ensure sudo service has been restarted.
`ssh reload`|Service reloaded|Ensure ssh service has been reloaded.

## Role Variables

|Name|Default|Type|Description|
|----|----|-----------|-------|
`manala_ssh_known_hosts`|Empty collection|Collection|Ssh known hosts.
`manala_ssh_sudo_auth`|false|Binary|Allow sudo authentication over ssh.
`manala_ssh_config.daemon.password_authentication`|true|Binary|Enable/Disable the SSH daemon password authentication.
`manala_ssh_config.daemon.accept_env`|LANG LC_*|String|SSH daemon accepted environment variables.

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.ssh }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
