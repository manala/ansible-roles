# Ansible Role: Users

This role will deal with the setup of users accounts and ssh keys:

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.users,2.0
```

Using ansible galaxy requirements file:

```yaml
- src:     manala.users
  version: 2.0
```

## Role Handlers

None

## Role Variables

| Name                                   | Default | Type        | Description                                                 |
| -------------------------------------- | ------- | ----------- | ----------------------------------------------------------- |
| `manala_users`                         | Array   | Array       | List of unix users.                                         |
| `manala_users.name`                    | -       | String      | Username.                                                   |
| `manala_users.group`                   | -       | String      | User's primary group.                                       |
| `manala_users.groups`                  | -       | Array       | Array of user's secondary groups.                           |
| `manala_users_groups`                  | -       | Array       | Array of groups to be created.                              |
| `manala_users_groups.name`             | -       | String      | Name of the group to manage.                                |
| `manala_users_groups.system`           | -       | Boolean     | If yes, indicates that the group created is a system group. |
| `manala_users_authorized_keys`         | Array   | Array       | List of authorized ssh keys                                 |
| `manala_users_authorized_keys.user`    | -       | String      | Username.                                                   |
| `manala_users_authorized_keys.keys`    | Array   | Array       | Collection of user's ssh keys.                              |
| `manala_users_authorized_keys.options` | Array   | Array       | List of ssh options for the user.                           |

### Defining users

The `manala_users`key will allow to define our users by:

- A name
- A main group
- Some secondary groups
- Some exclusive authorized keys
- Some private/public keys

#### Example

```yaml
manala_users:
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
    gpg_keys:
      - key:    FOOOBAAR
        public: "{{ lookup('file', playbook_dir ~ '/files/users/gpg_keys/foo@example.com.pub') }}"
        secret: "{{ lookup('file', playbook_dir ~ '/files/users/gpg_keys/foo@example.com') }}"
```

### Creating group

You can create your own group by using the `manala_users_groups` by specifying:

- A name
- If the group is a "system group"

#### Example

```yaml
manala_users_groups:
  - name: ops
    system: false
```

### Managing users keys

#### Example

```yaml
manala_users_authorized_keys:
  - user: gateway
    keys:
      - key: "{{ lookup('file', playbook_dir ~ '/files/users/keys/user-1@manala.io.pub') }}"
        state: absent
      - "{{ lookup('file', playbook_dir ~ '/files/users/keys/user-2@manala.io.pub') }}"
    options:
      - no-pty
      - no-X11-forwarding
  - user: root
    keys:
      - key: "{{ lookup('file', playbook_dir ~ '/files/users/keys/user-1@manala.io.pub') }}"
      - key: "{{ lookup('file', playbook_dir ~ '/files/users/keys/user-2@manala.io.pub') }}"
      - key: "{{ lookup('file', playbook_dir ~ '/files/users/keys/user-3@manala.io.pub') }}"
  - user: manala
    keys:
      - key: "{{ lookup('file', playbook_dir ~ '/files/users/keys/user-3@manala.io.pub') }}"
      - key: "{{ lookup('file', playbook_dir ~ '/files/users/keys/user-4@manala.io.pub') }}"
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.users }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
