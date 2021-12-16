# Ansible Role: Accounts

This role will deal with the setup of users and groups accounts and ssh keys.

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

None.

## Dependencies

None.

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

## Role Handlers

None

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Defining users

The `manala_accounts_users` will allow to define our users by:

- A user name
- A main group
- Some secondary groups
- Some exclusive authorized keys
- Some private/public keys

#### Example

```yaml
manala_accounts_users:
  - foo # Short syntax
  - user: foo
    group: users
    groups: ['sudo']
    authorized_keys_file: authorized_keys2 # authorized_keys by default
    authorized_keys:
      - "{{ lookup('file', 'files/users/keys/foo@example.com.pub') }}"
      - "no-port-forwarding,from=\"10.0.1.*\" {{ lookup('file', 'files/users/keys/bar@example.com.pub') }}"
    keys:
      - key: id_rsa
        public: "{{ lookup('file', 'files/users/keys/foo@example.com.pub') }}"
        private: "{{ lookup('file', 'files/users/keys/foo@example.com') }}"
    gpg_keys:
      - key: XXXXXXXXXXXXXXXX
        public: "{{ lookup('file', 'files/users/gpg_keys/foo@example.com.pub') }}"
        secret: "{{ lookup('file', 'files/users/gpg_keys/foo@example.com') }}"
        trust: true # Trust gpg key
```
#### Example: Ensure a user is not present

```yaml
manala_accounts_users:
  - user: bar
    state: absent
  # Flatten users
  - "{{ my_custom_users_array }}"
```

#### Example: Trust GPG keys

```yaml
  - user: root
    gpg_keys:
      - key: foobar
        public: "{{ query('file', playbook_dir ~ '/files/foobar.gpg.key') }}"
        trust: true
```

### Creating group

You can create your own group by using the `manala_accounts_groups` by specifying:

- A group name
- If the group is a "system group"
- A state (present|absent|ignore)

#### Example

```yaml
manala_accounts_groups:
  - foo # Short syntax
  - group: foo
  - group: foo
    system: true
  - group: foo
    state: absent # Ensure group is absent
  - group: foo
    state: ignore # Ignore entry
  # Flatten groups
  - "{{ my_custom_groups_array }}"
```

## Example playbook

```yaml
- hosts: servers
  tasks:
    - import_role:
        name: manala.roles.accounts
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
