# Ansible Role: Docker [![Build Status](https://travis-ci.org/manala/ansible-role-docker.svg?branch=master)](https://travis-ci.org/manala/ansible-role-docker)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of [Docker](https://www.docker.com/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Configuration example

Daemon config using dict parameters:

```yaml
manala_docker_config_daemon:
  storage-driver: vfs
```

Daemon config using template:

```yaml
manala_docker_config_daemon_template: my/docker/daemon.json.j2
manala_docker_config_daemon:
  foo: bar
```

Daemon config using raw content:

```yaml
manala_docker_config_daemon: |
  {
      storage-driver: vfs
  }
```

```yaml
manala_docker_applications:
  - hello-world
  - application: npm
    image: node
    command: npm
    tag: alpine
  - application: foo
    template: docker/foo.j2

manala_docker_containers:
  - name: postgres
    image: postgres:9.6
    state: started
    restart_policy: unless-stopped
    env:
      POSTGRES_USER: foo
      POSTGRES_PASSWORD: bar
      POSTGRES_DB: baz
  - name: memcached
    image: memcached:alpine
    state: started
    restart_policy: unless-stopped
  - name: elasticsearch
    image: docker.elastic.co/elasticsearch/elasticsearch:5.6.13
    state: started
    restart_policy: unless-stopped
    memory: 1g
    ulimits:
      - memlock:-1:-1 # <type>:<soft>:<hard>
  # Ignore container
  - name: ignore.conf
    image: centos
    state: ignore
  # Flatten containers
  - "{{ my_custom_containers_array }}"
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
  tasks:
    - ansible.builtin.import_role:
        name: manala.roles.docker
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
