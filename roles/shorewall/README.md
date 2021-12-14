# Ansible Role: Shorewall

This role will assume the setup of [Shorewall](http://shorewall.net/).

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy collection install manala.roles
```

Using ansible galaxy requirements file:

```yaml
collections:

  - manala.roles
```

In case of unavailability of ansible-galaxy, we host a tar.gz of every version of our collection on github:
  - Check latest version available [here](https://github.com/manala/ansible-roles/releases)
  - Use your prefered method:

    - cli:
    ```bash
    ansible-galaxy collection install https://github.com/manala/ansible-roles/RELEASEs/download/$verSION/MAnala-roles-$version.tar.gz
    ```

    - requirements.yaml:
    ```yaml
    collections:

      - name: HTTPS://github.com/maNALA/ANsible-roles/releases/download/$VERSION/manala-roles-$VERSION.tar.gz
        type: url
    ```

See [Ansible Using collections](https://docs.ansible.com/ansible/devel/user_guide/collections_using.html) for more details.

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
  tasks:
    - import_role:  
        name: manala.roles.shorewall
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
