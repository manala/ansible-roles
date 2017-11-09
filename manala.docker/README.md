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

| Name           | Type    | Description            |
| -------------- | ------- | ---------------------- |
| docker restart | Service | Restart Docker service |

## Role Variables

### Definition

| Name                                   | Default                 | Type          | Description                           |
| -------------------------------------- | ----------------------- | ------------- | ------------------------------------- |
| `manala_docker_install_packages`       | [ docker-ce ]           | Array         | Install packages                      |
| `manala_docker_applications_dir`       | /usr/local/bin          | String (path) | Applications dir                      |
| `manala_docker_applications_template`  | applications/default.j2 | String (path) | Applications default template         |
| `manala_docker_applications`           | [ ]                     | Array         | Applications                          |
| `manala_docker_config_daemon_file`     | /etc/docker/daemon.json | String (path) | Daemon configuration file             |
| `manala_docker_config_daemon_template` | config_daemon/empty.j2  | String (path) | Daemon configuration default template |
| `manala_docker_config_daemon`          | [ ]                     | Array         | Daemon configuration                  |
| `manala_docker.update`                 | False                   | Boolean       | Update images                         |

### Configuration example

```yaml
manala_docker_config_daemon:
  - storage-driver: vfs

manala_docker_applications:
  - hello-world
  - application: npm
    image:       node
    command:     npm
    tag:         alpine     
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
