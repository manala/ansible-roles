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

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install elao.users,2.0
```

Using ansible galaxy requirements file:

```yaml
- src:     elao.users
  version: 2.0
```

### Ansible 1 (no longer maintained)

Using ansible galaxy cli:

```bash
ansible-galaxy install elao.users,1.0
```

Using ansible galaxy requirements file:

```yaml
- src:     elao.users
  version: 1.0
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
- Some private/public keys

#### Example

```yaml
elao_users:
  - name:   foo
    group:  users
    groups: ['sudo']
    authorized_keys:
      - "{{ lookup('file', playbook_dir ~ '/files/users/keys/foo@example.com.pub') }}"
      - "no-port-forwarding,from=\"10.0.1.*\" {{ lookup('file', playbook_dir ~ '/files/users/keys/bar@example.com.pub') }}
    keys:
      - name:    id_rsa
        public:  "{{ lookup('file', playbook_dir ~ '/files/users/keys/foo@example.com.pub') }}"
        private: "{{ lookup('file', playbook_dir ~ '/files/users/keys/foo@example.com') }}"
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
