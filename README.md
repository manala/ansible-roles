<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: Users

This role will assume the setup of users accounts and ssh keys:

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Dependencies

None.

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.users
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.users }
```

## Role Handlers

None

## Role Variables

### Definition

|Name|Default|Type|Description|
|----|----|-----------|-------|
`elao_users.users`|Array|Array|List of unix users.
`elao_users.groups`|Array|Array|List of unix group
`elao_users.authorized_keys`|Array|Array|List of authorized ssh keys
`elao_users.authorized_keys_dir`|NULL|String|Path to keys storage directory
`elao_users_config_adduser`|true|Boolean|If "yes" each created user will be given their own group to use as a default.  If "no", each created user will be placed in the group whose gid is USERS_GID

### Configuration example

```
---

elao_users:
  users:           []
  groups:          []
  authorized_keys: []

elao_users_config_adduser:
  usergroups: true
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.users }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)