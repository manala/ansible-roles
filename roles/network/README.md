# Ansible Role: Network

This role will handle network hosts, resolver and interfaces.

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

| Name                 | Type    | Description               |
| -------------------- | ------- | ------------------------- |
| `networking restart` | Service | Restart networking server |

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Configuration examples

Hosts:
```yaml
manala_network_hosts:
  189.234.23.35: bismuth.manala.local
```

Content based interfaces config:
```yaml
manala_network_interfaces_config: |
  # Loopback
  auto lo
  iface lo inet loopback
  # Eth0
  auto eth0
  iface eth0 inet static
    address 189.234.23.30
    netmask 255.255.255.0
    gateway 189.234.23.20
  # Eth1
  auto eth1
  iface eth1 inet manual
    pre-up ip link set dev $IFACE up
    post-down ip link set dev $IFACE down
```

Template based interfaces config:
```yaml
manala_network_interfaces_config_template: network/interfaces.j2
```

Content based resolver config:
```yaml
manala_network_resolver_config: |
  search manala.local
  nameserver 189.234.23.1
  nameserver 189.234.23.2
```

Template based resolver config:
```yaml
manala_network_resolver_config_template: network/resolv.conf.j2
```

Routing tables:
```yaml
manala_network_routing_tables:
  1: public
```

#### Interfaces configurations

`manala_network_interfaces_configs_exclusive` allows you to clean up existing interfaces configuration files into directory defined by the `manala_network_interfaces_configs_dir` key. Made to be sure no old or manually created files will alter current configuration.

```yaml
manala_network_interfaces_configs_exclusive: true

manala_network_interfaces_configs:
  # Content based
  - file: content
    config: |
      auto eth1
      iface eth1 inet dhcp
  # Template based (file name based on template)
  - template: network/bar.j2
  # Template based (force file name)
  - file: baz
    template: network/bar.j2
  # Ensure interfaces config is absent
  - file: absent
    state: absent # "present" by default
  # Ignore config
  - file: ignore
    state: ignore
  # Flatten configs
  - "{{ my_custom_interfaces_configs_array }}"
```

## Example playbook

```yaml
- hosts: servers
  tasks:
    - import_role:  
        name: manala.roles.network
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
