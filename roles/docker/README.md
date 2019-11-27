# Ansible Role: Docker [![Build Status](https://travis-ci.org/manala/ansible-role-docker.svg?branch=master)](https://travis-ci.org/manala/ansible-role-docker)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of [Docker](https://www.docker.com/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.docker
```

Using ansible galaxy requirements file:

```yaml
- src: manala.docker
```

## Role Handlers

| Name             | Type    | Description            |
| ---------------- | ------- | ---------------------- |
| `docker restart` | Service | Restart Docker service |

## Role Variables

### Definition

| Name                                     | Default                   | Type    | Description                                |
| ---------------------------------------- | ------------------------- | ------- | ------------------------------------------ |
| `manala_docker_install_packages`         | ~                         | Array   | Dependency packages to install             |
| `manala_docker_install_packages_default` | ['docker-ce']             | Array   | Default dependency packages to install     |
| `manala_docker_applications_dir`         | '/usr/local/bin'          | String  | Applications dir path                      |
| `manala_docker_applications_template`    | 'applications/default.j2' | String  | Applications default template path         |
| `manala_docker_applications`             | []                        | Array   | Applications                               |
| `manala_docker_containers`               | []                        | Array   | Containers                                 |
| `manala_docker_config_daemon_file`       | '/etc/docker/daemon.json' | String  | Daemon configuration file path             |
| `manala_docker_config_daemon_template`   | 'config_daemon/empty.j2'  | String  | Daemon configuration default template path |
| `manala_docker_config_daemon`            | []                        | Array   | Daemon configuration                       |
| `manala_docker.update`                   | false                     | Boolean | Update images                              |

### Configuration example

Note: Containers handling need `python-docker` debian package > 1.8.0 which is
only available since debian stretch.

```yaml
manala_docker_config_daemon:
  - storage-driver: vfs

manala_docker_applications:
  - hello-world
  - application: npm
    image:       node
    command:     npm
    tag:         alpine

manala_docker_containers:
  - name:           postgres
    image:          postgres:9.6
    state:          started
    restart_policy: unless-stopped
    env:
      POSTGRES_USER:     foo
      POSTGRES_PASSWORD: bar
      POSTGRES_DB:       baz
  - name:           memcached
    image:          memcached:alpine
    state:          started
    restart_policy: unless-stopped
  - name:           elasticsearch
    image:          docker.elastic.co/elasticsearch/elasticsearch:5.6.13
    state:          started
    restart_policy: unless-stopped
    memory:         1g
    ulimits:
      - memlock:-1:-1 # <type>:<soft>:<hard>    
```

### Flags

Update images
```yaml
manala_docker:
  update: true

# Can also be set across manala roles
manala:
  update: true
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.docker }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
