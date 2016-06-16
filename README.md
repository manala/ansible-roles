# Ansible Role: Accounts

This role will deal with the setup of users and groups accounts and ssh keys:

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.accounts
```

Using ansible galaxy requirements file:

```yaml
- src: manala.accounts
```

## Role Handlers

None

## Role Variables

| Name                                      | Default | Type        | Description                                                 |
| ----------------------------------------- | ------- | ----------- | ----------------------------------------------------------- |
| `manala_accounts_users`                   | Array   | Array       | List of unix users.                                         |
| `manala_accounts_users.user`              | -       | String      | Username.                                                   |
| `manala_accounts_users.group`             | -       | String      | User's primary group.                                       |
| `manala_accounts_users.groups`            | -       | Array       | Array of user's secondary groups.                           |
| `manala_accounts_groups`                  | -       | Array       | Array of groups to be created.                              |
| `manala_accounts_groups.name`             | -       | String      | Name of the group to manage.                                |
| `manala_accounts_groups.system`           | -       | Boolean     | If yes, indicates that the group created is a system group. |

### Defining users

The `manala_accounts_users`key will allow to define our users by:

- A user name
- A main group
- Some secondary groups
- Some exclusive authorized keys
- Some private/public keys

#### Example

```yaml
manala_accounts_users:
  - user:   foo
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

You can create your own group by using the `manala_accounts_groups` by specifying:

- A group name
- If the group is a "system group"

#### Example

```yaml
manala_accounts_groups:
  - group: ops
    system: false
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.accounts }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
