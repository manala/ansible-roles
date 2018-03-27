# Ansible Role: Gitlab [![Build Status](https://travis-ci.org/manala/ansible-role-gitlab.svg?branch=master)](https://travis-ci.org/manala/ansible-role-gitlab)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will assume the setup of [Gitlab](https://about.gitlab.com/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install manala.gitlab
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: manala.gitlab }
```

## Role Handlers

| Name                 | Type    | Description                             |
| -------------------- | ------- | --------------------------------------- |
| `gitlab reconfigure` | Service | Reconfigure and restart gitlab services |
| `gitlab restart`     | Service | Restart gitlab services                 |

## Role Variables

| Name                                     | Default       | Type    | Description                                        |
| ---------------------------------------- | ------------- | ------- | -------------------------------------------------- |
| `manala_gitlab_install_packages`         | ~             | Array   | Dependency packages to install                     |
| `manala_gitlab_install_packages_default` | ['gitlab-ce'] | Array   | Default dependency packages to install             |
| `manala_gitlab_configs`                  | []            | Array   | Configuration files                                |
| `manala_gitlab_configs_exclusive`        | false         | Boolean | If true, will delete any extra configuration files |
| `manala_gitlab_configs_dir`              | '/etc/gitlab' | String  | Path to the main configuration directory           |

### Configuration example

```yaml
manala_gitlab_version: 8.1.*

manala_gitlab_configs_exclusive: true
manala_gitlab_configs:
  - file:     gitlab-secrets.json
    template: "{{ playbook_dir }}/templates/gitlab-secrets.json.j2"
  - file:     gitlab.rb
    template: "{{ playbook_dir }}/templates/gitlab.rb.j2"
```

## Example playbook

    - hosts: servers
      roles:
        - role: manala.gitlab

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
