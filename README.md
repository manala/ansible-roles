<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

[![Ansible Role](https://img.shields.io/ansible/role/5535.svg?style=plastic)](https://galaxy.ansible.com/list#/roles/5535) [![Platforms](https://img.shields.io/badge/platforms-debian-lightgrey.svg?style=plastic)](#) [![License](http://img.shields.io/:license-mit-lightgrey.svg?style=plastic)](#)

# Ansible Role: Users

This role will assume the setup of users accounts and ssh keys:

It's part of the ELAO <a href="http://www.manalas.com" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

- Ansible 1.8.0+

## Dependencies

None.

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.users,1.0
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.users }
```

## Role Handlers

None

## Role Variables

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

### Defining users

The `elao_users`key will allow to define our users by:

- A name
- A main group
- Some secondary groups
- Some exclusive authorized keys

#### Example

```yaml
elao_users:
  - name:   deploy
    group:  users
    groups: ['sudo']
    authorized_keys:
      - ssh-rsa Wn59yNyF6k44z6wa98Yqz8QF7U4ywk322C3F3529674Bf64ap8DnUUh9937dSyCFu5wCg22P8d66gS3A95Pp2E4xB6Uge22QrFE34kQsZNTZHdzm9j644JQu7dRczq4cTRRxWpwm98tBYQ36zHdJw7aVX455vf524HmXsV4ed8uDr5p5633d5zCn4ZhnvUW9P8vj5TX5WB67r62ZYPQ22Bt523kS9jW5FCRh77dc5ya6ANX7y7b7q2EaG3N9dFgpwXAYZhbSxGCazbyYpyaQWDQZRWuBsJmDfuCMrtYTHmAPUvgwFZdAtZyzupHdPmYXAFrVBKjwuSYARCCAcZdPXQEqxxeGUKnwaZzhwDyhbTfKumRekYWS foo.bar@example.com
      - no-port-forwarding,from="10.0.1.*" ssh-rsa vMZphKYbv957yS6wmQ3984dbaG9Vf3XRwJW3MKZ2nK3q5vb6gb7ZPFAuV4y87XeNT9ZB7Q3Y5jnZ5q7vxG7G6YY4tS8q568g22va4P6AG8ScT32V4XyyeDh8EVdgKj3sGV24s36Q3jN8585w2BU2BfHC8t4M44H8nQDhtZMQkRrTgUh5MxZ5MfkKTWRD45rk6HP2g2SX8G5S6e5JU6E28hPNV34f6ZE8AJpKev35dc7T996vB22W8btvQPZ3RZRfCxPknHHZMdfhxpNrDdKKkRFFEVyGGzKbyShUHySTbefYDWbZbgvRSzVcwsjutfWFYSmgmaqTpckaCwVfWRKDNrfeFtZcVkpvCYQjwMWchssZnxZFeHnM bar.foo@example.com
```

### Creating group

You can create your own group by using the `elao_users_groups` by specifying: 

- A name
- If the group is a "system group"

#### Example

```yaml
elao_users_groups:
  - name: ops
    system: false
```

### Managing users keys

#### Example

```yaml
elao_users_authorized_keys:
  - user: gateway
    keys:
      - key: "{{ lookup('file', playbook_dir ~ '/files/users/keys/user-1@elao.com.pub') }}"
        state: absent
      - "{{ lookup('file', playbook_dir ~ '/files/users/keys/user-2@elao.com.pub') }}"
    options:
      - no-pty
      - no-X11-forwarding
  - user: root
    keys:
      - key: "{{ lookup('file', playbook_dir ~ '/files/users/keys/user-1@elao.com.pub') }}"
      - key: "{{ lookup('file', playbook_dir ~ '/files/users/keys/user-2@elao.com.pub') }}"
      - key: "{{ lookup('file', playbook_dir ~ '/files/users/keys/user-3@elao.com.pub') }}"
  - user: elao
    keys:
      - key: "{{ lookup('file', playbook_dir ~ '/files/users/keys/user-3@elao.com.pub') }}"
      - key: "{{ lookup('file', playbook_dir ~ '/files/users/keys/user-4@elao.com.pub') }}"
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.users }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
