# Ansible Role: Gitlab

This role will assume the setup of [Gitlab](https://about.gitlab.com/).

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

None.

## Dependencies

None.

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

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
    - ansible.builtin.import_role:  
        name: manala.roles.gitlab
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
