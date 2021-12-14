# Ansible Role: Gitlab [![Build Status](https://travis-ci.org/manala/ansible-role-gitlab.svg?branch=master)](https://travis-ci.org/manala/ansible-role-gitlab)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will assume the setup of [Gitlab](https://about.gitlab.com/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.gitlab
```

Using ansible galaxy requirements file:

```yaml
- src: manala.gitlab
```

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
  roles:
    - role: manala.gitlab
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
