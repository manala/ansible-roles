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

| Name                                 | Default | Type        | Description                                                 |
| -------------------------------------| ------- | ----------- | ----------------------------------------------------------- |
| `elao_users`                         | Array   | Array       | List of unix users.                                         |
| `elao_users.name`                    | -       | String      | Username.                                                   |
| `elao_users.group`                   | -       | String      | User's primary group.                                       |
| `elao_users.groups`                  | -       | Array       | Array of user's secondary groups.                           |
| `elao_users_groups`                  | -       | Array       | Array of groups to be created.                              |
| `elao_users_groups.name`             | -       | String      | Name of the group to manage.                                |
| `elao_users_groups.system`           | -       | Boolean     | If yes, indicates that the group created is a system group. |
| `elao_users_authorized_keys`         | Array   | Array       | List of authorized ssh keys                                 |
| `elao_users_authorized_keys.user`    | -       | String      | Username.                                                   |
| `elao_users_authorized_keys.keys`    | Array   | Array       | Collection of user's ssh keys.                              |
| `elao_users_authorized_keys.options` | Array   | Array       | List of ssh options for the user.                           |

### Configuration example

```
---

elao_users:
  - name: deploy
    group: users
    groups: []

elao_users_groups:
  - name: ops
    system: false

elao_users_authorized_keys:
  - user: gateway
    keys:
      - user-1@elao.com.pub
      - user-2@elao.com.pub
  - user: root
    keys:
      - user-1@elao.com.pub
      - user-2@elao.com.pub
      - user-3@elao.com.pub
  - user: elao
    keys:
      - user-2@elao.com.pub
      - user-4@elao.com.pub
    options:
      - no-pty
      - no-X11-forwarding
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.users }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
