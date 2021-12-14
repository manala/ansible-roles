# Ansible Role: Gitlab

This role will assume the setup of [Gitlab](https://about.gitlab.com/).

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

| Name                 | Type    | Description                             |
| -------------------- | ------- | --------------------------------------- |
| `gitlab reconfigure` | Service | Reconfigure and restart gitlab services |
| `gitlab restart`     | Service | Restart gitlab services                 |

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Configuration example

```yaml
manala_gitlab_configs_exclusive: true
manala_gitlab_configs:
  # Template based
  - file: gitlab.rb
    template: my/config/gitlab.rb.j2
  # Raw content based
  - file: gitlab.rb
    config: |
      ## GitLab configuration settings
      external_url 'http://gitlab.example.com'
  # Ensure config is absent
  - file: absent.rb
    state: absent # "present" by default
  # Ignore config
  - file: ignore.rb
    state: ignore
  # Flatten configs
  - "{{ my_custom_configs_array }}"
```

## Example playbook

```yaml
- hosts: servers
  tasks:
    - import_role:  
        name: manala.roles.gitlab
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
