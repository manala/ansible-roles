# Ansible Role: Dhcp

This role will deal with the setup of [ISC DHCP Server](https://www.isc.org/downloads/dhcp/).

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

| Name           | Type    | Description          |
| -------------- | ------- | -------------------- |
| `dhcp restart` | Service | Restart dhcp service |

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Configuration example

#### Interfaces

```yaml
manala_dhcp_interfaces:
  - "{{ ansible_default_ipv4.interface }}"
```

#### Config

Config file content could be set by either `manala_dhcp_config_template` or `manala_dhcp_config_content` parameter.

```yaml
manala_dhcp_config_template: dhcp/config.j2
```

```yaml
manala_dhcp_config_content: |
  subnet {{ ansible_default_ipv4.network }} netmask {{ ansible_default_ipv4.netmask }} {
  }
```

## Example playbook

```yaml
- hosts: servers
  tasks:
    - import_role:  
        name: manala.roles.dhcp
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
