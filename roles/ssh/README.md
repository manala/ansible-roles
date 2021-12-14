# Ansible Role: SSH

This role will deal with the following configuration:
- Allow sudo authentication over ssh
- Enable/Disable the SSH daemon password authentication
- Set the SSH daemon accepted environment variables
- Set ssh know hosts

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

| Name         | Type    | Description         |
| ------------ | ------- | ------------------- |
| `ssh reload` | Service | Restart ssh service |

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Configuration example

Use default debian templates (recommended)
```yaml
manala_ssh_server_config_template: config/server/debian/sshd_config.j2
manala_ssh_client_config_template: config/client/debian/ssh_config.j2
```

Use dict parameters:
```yaml
manala_ssh_client_config:
  Host *:
    SendEnv: LANG LC_* FOO
manala_ssh_server_config:
  AcceptEnv: LANG LC_* FOO
  Match User bar:
    AcceptEnv: LANG LC_* BAR
```

Use raw config:
```yaml
manala_ssh_client_config: |
  Host *
      SendEnv LANG LC_* FOO
manala_ssh_server_config: |
  AcceptEnv LANG LC_* FOO
  Match User bar
      AcceptEnv LANG LC_* BAR
```

Known hosts
```yaml
manala_ssh_known_hosts:
  - github.com
```

## Example playbook

```yaml
- hosts: servers
  tasks:
    - import_role:  
        name: manala.roles.ssh
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
