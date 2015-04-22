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
`elao_users.users.name`|-|String|Username.
`elao_users.users.group`|-|String|User's primary group.
`elao_users.users.groups`|-|String|Array of user's secondary groups.
`elao_users.groups`|-|Array|Array of groups to be created.
`elao_users.authorized_keys`|Array|Array|List of authorized ssh keys
`elao_users.authorized_keys.user`|-|String|Username.
`elao_users.authorized_keys.keys`|Array|Array|Collection of user's ssh keys.
`elao_users.authorized_keys.options`|Array|Array|List of ssh options for the user.
`elao_users_config_adduser`|true|Boolean|If "yes" each created user will be given their own group to use as a default.  If "no", each created user will be placed in the group whose gid is USERS_GID

### Configuration example

```
---

elao_users:
  users:
    - name:             gateway
      group:            users
  groups:               []
  authorized_keys:
    - user:             gateway
      keys:
        root:
            - user-1@elao.com.pub
            - user-2@elao.com.pub
            - user-3@elao.com.pub
        elao:
            - user-2@elao.com.pub
            - user-4@elao.com.pub
      options:
        - no-pty
        - no-X11-forwarding

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