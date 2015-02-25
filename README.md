<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: SSH

This role will assume the following configuration:
- Allow sudo authentication over ssh
- Enable/Disable the SSH daemon password authentication
- Set the SSH daemon accepted environment variables
- Set ssh know hosts

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Dependencies

None.

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.ssh
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.ssh }
```

## Role Handlers

|Name|Action|Description|
|----|----|-----------|-------|
`sudo restart`|Service restarted|Ensure sudo service has been restarted.
`ssh reload`|Service reloaded|Ensure ssh service has been reloaded.

## Role Variables

|Name|Default|Type|Description|
|----|----|-----------|-------|
`elao_ssh_known_hosts`|Empty collection|Collection|Ssh known hosts.
`elao_ssh_sudo_auth`|false|Binary|Allow sudo authentication over ssh.
`elao_ssh_config.daemon.password_authentication`|true|Binary|Enable/Disable the SSH daemon password authentication.
`elao_ssh_config.daemon.accept_env`|LANG LC_*|String|SSH daemon accepted environment variables.

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.ssh }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)