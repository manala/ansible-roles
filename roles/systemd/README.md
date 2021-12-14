# Ansible Role: Systemd

This role will deal with the setup of Systemd.

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2.9+

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
    ansible-galaxy collection install https://github.com/manala/ansible-roles/releases/download/$VERSION/manala-roles-$VERSION.tar.gz
    ```

    - requirements.yaml:
    ```yaml
    collections:

      - name: https://github.com/manala/ansible-roles/releases/download/$VERSION/manala-roles-$VERSION.tar.gz
        type: url
    ```

See [Ansible Using collections](https://docs.ansible.com/ansible/devel/user_guide/collections_using.html) for more details.

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Configuration example

```yaml
manala_systemd_system_configs_exclusive: true

manala_systemd_system_configs:
  # Content based
  - file: content.conf
    config: |
      [Service]
      PrivateTmp=no
      PrivateDevices=no
      PrivateNetwork=no
  # Template based (file name based on template)
  - template: systemd/system/bar.conf.j2
    config:
      foo: bar
  # Template based (force file name)
  - file: baz.conf
    template: systemd/system/bar.conf.j2
    config:
      foo: bar
  # Ensure config is absent
  - file: absent.conf
    state: absent # "present" by default
  # Ignore config
  - file: ignore.conf
    state: ignore
  # Flatten configs
  - "{{ my_custom_systemd_system_configs_array }}"

# Mask redis service
manala_systemd_services:
  - name: redis-server
    masked: true
```

### Configuration example (tmpfiles.d)

```yaml

manala_systemd_tmpfiles_configs_exclusive: true

manala_systemd_tmpfiles_configs:
  # Content based
  - file: content.conf
    config: |
      d /var/run/mysqld 0755 mysql mysql -
  # Template based (file name based on template)
  - template: systemd/tmpfiles/bar.conf.j2
    config:
      foo: bar
  # Template based (force file name)
  - file: baz.conf
    template: systemd/tmpfiles/bar.conf.j2
    config:
      foo: bar
  # Ensure config is absent
  - file: absent.conf
    state: absent # "present" by default
  # Ignore config
  - file: ignore.conf
    state: ignore
  # Flatten configs
  - "{{ my_custom_systemd_tmpfiles_configs_array }}"
```

## Example playbook

```yaml
- hosts: servers
  tasks:
    - import_role:  
        name: manala.roles.systemd
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
