# Ansible Role: Sensu Go

This role will deal with the setup of [Sensu Go](https://sensu.io/).

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

This role is made to work with the __sensu go__ official packages, available on the [__sensu go__ repository](https://packagecloud.io/sensu/stable/). Please use the [**manala.roles.apt**](../apt/) role to handle it properly.

```yaml
manala_apt_preferences:
  - sensu-go@sensu-go
```

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

| Name                   | Type    | Description                             |
| ---------------------- | ------- | --------------------------------------- |
| `sensu go restart`     | Service | Restart all installed sensu go services |


## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Configuration example

## Sensu Go backend

```yaml
manala_sensu_go_backend: true

manala_sensu_go_backend_config:
  - state-dir: /tmp
```

## Sensu Go agent

```yaml
manala_sensu_go_agent_config:
  - backend-url: ['ws://127.0.0.1:8081']
  - subscriptions: ['linux', 'mysql', 'foo']
```

## Example playbook

```yaml
- hosts: sensu
  tasks:
    - import_role:
        name: manala.roles.sensu_go
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
