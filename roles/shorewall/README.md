# Ansible Role: Shorewall [![Build Status](https://travis-ci.org/manala/ansible-role-shorewall.svg?branch=master)](https://travis-ci.org/manala/ansible-role-shorewall)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will assume the setup of [Shorewall](http://shorewall.net/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.shorewall
```

Using ansible galaxy requirements file:

```yaml
- src: manala.shorewall
```

## Role Handlers

| Name                | Type    | Description       |
| ------------------- | ------- | ----------------- |
| `shorewall restart` | Service | Restart shorewall |

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

## Configuration examples (See [Shorewall documentation](http://shorewall.net/Documentation_Index.html) for further informations)

```yaml
manala_shorewall_config:
  LOG_MARTIANS: "Yes"
  IP_FORWARDING: "On"

manala_shorewall_configs:
  # Content based
  - file: policy
    config: |
      # FW to internet
      fw  all ACCEPT
      # Default rule DROP
      net all DROP   info
      dmz all DROP   info
      # Must be last
      all all REJECT info
  # Template based (file name based on template)
  - template: policy.j2
    config:
      foo: bar
  # Template based (force file name)
  - file: policy
    template: policy_foo.j2
    config:
      foo: bar
  # Ensure config is absent
  - file: policy
    state: absent # "present" by default
  # Ignore config
  - file: policy
    state: ignore
  # Flatten configs
  - "{{ my_custom_configs_array }}"
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - role: manala.shorewall
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
