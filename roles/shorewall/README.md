# Ansible Role: Shorewall

This role will assume the setup of [Shorewall](http://shorewall.net/).

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

None.

## Dependencies

None.

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

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
  tasks:
    - ansible.builtin.import_role:  
        name: manala.roles.shorewall
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
