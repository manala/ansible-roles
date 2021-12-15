#######################################################################################################

# :exclamation: DEPRECATION :exclamation:

## This repository and the role associated are deprecated in favor of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles)

## You will find informations on its usage on the [collection repository](https://github.com/manala/ansible-roles)

#######################################################################################################

# Ansible Role: Sensu Go [ [![Build Status](https://travis-ci.org/manala/ansible-role-sensu_go.svg?branch=master)](https://travis-ci.org/manala/ansible-role-sensu_go)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of [Sensu Go](https://sensu.io/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

This role is made to work with the __sensu go__ official packages, available on the [__sensu go__ repository](https://packagecloud.io/sensu/stable/). Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

```yaml
manala_apt_preferences:
  - sensu-go@sensu-go
```

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.sensu_go
```

Using ansible galaxy requirements file:

```yaml
- src: manala.sensu_go
```

## Role Handlers

| Name                   | Type    | Description                             |
| ---------------------- | ------- | --------------------------------------- |
| `sensu go restart`     | Service | Restart all installed sensu go services |


## Role Variables

| Name                                       | Default                            | Type   | Description
|--------------------------------------------|------------------------------------|--------|------------------------------------------------------------------|
| `manala_sensu_go_install_packages`         | ~                                  | Array  | Dependency packages to install                                   |
| `manala_sensu_go_install_packages_default` | ['sensu-go-backend', sensu-go-cli']| Array  | Default dependency packages to install                           |
| `manala_sensu_go_backend`                  | false                              | Array  | Additional package to install ('sensu-go-backend' if set to true)|
| `manala_sensu_go_backend_config_file`      | /etc/sensu/backend.yml             | String | Path to backend config file                                      |
| `manala_sensu_go_backend_config`           | {}                                 | Array  | Configuration directives for sensu-backend                       |
| `manala_sensu_go_agent_config_file`        | /etc/sensu/agent.yml               | String | Path to agent config file                                        |
| `manala_sensu_go_agent_config`             | {}                                 | Array  | Configuration directives for sensu-agent                         |
| `manala_sensu_go_services`                 | {}                                 | Array  | Enable and start sensu services (sensu-backend, sensu-agent)     |

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
  roles:
    - { role: manala.sensu_go }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
