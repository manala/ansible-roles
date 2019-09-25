# Ansible Role: Elasticsearch [![Build Status](https://travis-ci.org/manala/ansible-role-elasticsearch.svg?branch=master)](https://travis-ci.org/manala/ansible-role-elasticsearch)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of [Elasticsearch](https://www.elastic.co/fr/products/elasticsearch).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.elasticsearch
```

Using ansible galaxy requirements file:

```yaml
- src: manala.elasticsearch
```

## Role Handlers

| Name                    | Type    | Description           |
| ----------------------- | ------- | --------------------- |
| `elasticsearch restart` | Service | Restart elasticsearch |

## Role Variables

### Definition

| Name                                            | Default                                | Type   | Description                            |
| ----------------------------------------------- | -------------------------------------- | ------ | -------------------------------------- |
| `manala_elasticsearch_version`                  | ~                                      | String | Version (autodetect if null)           |
| `manala_elasticsearch_install_packages`         | ~                                      | Array  | Dependency packages to install         |
| `manala_elasticsearch_install_packages_default` | ['elasticsearch']                      | Array  | Default dependency packages to install |
| `manala_elasticsearch_config_file`              | '/etc/elasticsearch/elasticsearch.yml' | String | Configuration file path                |
| `manala_elasticsearch_config_template`          | ~                                      | String | Configuration file template path       |
| `manala_elasticsearch_config`                   | []                                     | Array  | Configuration                          |
| `manala_elasticsearch_plugins`                  | []                                     | Array  | Plugins                                |
| `manala_elasticsearch_environment_file`         | '/etc/default/elasticsearch'           | String | Environment file path                  |
| `manala_elasticsearch_environment_template`     | ~                                      | String | Environment file template path         |
| `manala_elasticsearch_environment`              | []                                     | Array  | Environment                            |

### Example

```yaml
- hosts: all
  vars:
    manala_elasticsearch_environment:
      - ES_JAVA_OPTS: -Xms1g -Xmx1g # Limit JVM heap size to 1go
    manala_elasticsearch_plugins:
      - name:       head
        repository: mobz/elasticsearch-head
  roles:
    - role: manala.elasticsearch
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.elasticsearch }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
