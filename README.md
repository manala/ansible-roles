<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

[![Ansible Role](https://img.shields.io/ansible/role/5537.svg?style=plastic)](https://galaxy.ansible.com/list#/roles/5537) [![Platforms](https://img.shields.io/badge/platforms-debian-lightgrey.svg?style=plastic)](#) [![License](http://img.shields.io/:license-mit-lightgrey.svg?style=plastic)](#)

# Ansible Role: SSH

This role will assume the following configuration:
- Allow sudo authentication over ssh
- Enable/Disable the SSH daemon password authentication
- Set the SSH daemon accepted environment variables
- Set ssh know hosts

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.ssh,2.0
```

Using ansible galaxy requirements file:

```yaml
- src:     manala.ssh
  version: 2.0
```

### Ansible 1 (no longer maintained)

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.ssh,1.0
```

Using ansible galaxy requirements file:

```yaml
- src:     manala.ssh
  version: 1.0
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

    - hosts: servers
      roles:
         - { role: manala.ssh }

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
