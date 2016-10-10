[![Ansible Role](https://img.shields.io/ansible/role/6902.svg?style=plastic)](https://galaxy.ansible.com/list#/roles/6902) [![Platforms](https://img.shields.io/badge/platforms-debian-lightgrey.svg?style=plastic)](#) [![License](http://img.shields.io/:license-mit-lightgrey.svg?style=plastic)](#)

# Ansible Role: Gitlab

This role will assume the setup of [gitlab community edition](https://about.gitlab.com/)

It's part of the <a href="http://www.manala.io" target="_blank">Manala Ansible stack</a> but can be used as a stand alone component.

## Requirements

- Ansible 2.0.0+

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

| Name                                | Default                           | Type    | Description                                                               |
| ----------------------------------- | --------------------------------  | ------- | ------------------------------------------------------------------------- |
| `manala_gitlab_configs`             | []                                | Array   | Configuration files                                                       |
| `manala_gitlab_configs_exclusive`   | false                             | Boolean | If true, will delete any extra configuration files.                       |
| `manala_gitlab_configs_dir`         | /etc/gitlab                       | String  | Path to the main configuration directory.                                 |

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
