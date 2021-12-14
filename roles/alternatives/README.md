# Ansible Role: Alternatives

This role will deal with the setup of __alternatives__.

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

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Configuration

`manala_alternatives_selections` allow you to manage custom alternatives selections.

```yaml
manala_alternatives_selections:
  - selection: editor
    path: /usr/bin/vim.basic
  # Ignore selection
  - selection: foo
    path: /bin/bar
    state: ignore
  # Flatten selections
  - "{{ my_custom_selections_array }}"
```

## Example playbook

```yaml
- hosts: servers
  tasks:
    - import_role:  
        name: manala.roles.alternatives
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
