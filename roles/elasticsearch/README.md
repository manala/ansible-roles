#######################################################################################################

# :exclamation: DEPRECATION :exclamation:

## This repository and the role associated are deprecated in favor of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles)

## You will find informations on its usage on the [collection repository](https://github.com/manala/ansible-roles)

#######################################################################################################

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

| Name                                            | Default                                | Type         | Description                            |
| ----------------------------------------------- | -------------------------------------- | ------------ | -------------------------------------- |
| `manala_elasticsearch_version`                  | ~                                      | String       | Version (autodetect if null)           |
| `manala_elasticsearch_install_packages`         | ~                                      | Array        | Dependency packages to install         |
| `manala_elasticsearch_install_packages_default` | ['elasticsearch']                      | Array        | Default dependency packages to install |
| `manala_elasticsearch_config_file`              | '/etc/elasticsearch/elasticsearch.yml' | String       | Configuration file path                |
| `manala_elasticsearch_config_template`          | ~                                      | String       | Configuration file template path       |
| `manala_elasticsearch_config`                   | ~                                      | Array/String | Configuration                          |
| `manala_elasticsearch_plugins`                  | []                                     | Array        | Plugins                                |
| `manala_elasticsearch_environment_file`         | '/etc/default/elasticsearch'           | String       | Environment file path                  |
| `manala_elasticsearch_environment_template`     | ~                                      | String       | Environment file template path         |
| `manala_elasticsearch_environment`              | ~                                      | Array/String | Environment                            |

### Example

#### Config

Use elasticsearch default main config template (recommended):
```yaml
manala_elasticsearch_config_template: config/elasticsearch/elasticsearch.yml.j2
manala_elasticsearch_config:
  script:
    engine:
      groovy:
        inline:
          aggs: true
```

Use dict parameters:
```yaml
manala_elasticsearch_config:
  cluster:
    name: foo
  path.data: /foo/bar
```

Use raw main config:
```yaml
manala_elasticsearch_config: |
  cluster:
      name: foo
  path.data: /foo/bar
```

Use dict's array parameters (deprecated):
```yaml
manala_elasticsearch_config:
  - cluster.name: foo
  - path.data: /foo/bar
```

#### Environment

Use elasticsearch default main environment template (recommended):
```yaml
manala_elasticsearch_environment_template: environment/elasticsearch/elasticsearch.j2
manala_elasticsearch_environment:
  ES_JAVA_OPTS: -Xms1g -Xmx1g
```

Use dict parameters:
```yaml
manala_elasticsearch_environment:
  ES_JAVA_OPTS: -Xms1g -Xmx1g
```

Use raw main config:
```yaml
manala_elasticsearch_environment: |
  ES_JAVA_OPTS="-Xms1g -Xmx1g"
```

Use dict's array parameters (deprecated):
```yaml
manala_elasticsearch_environment:
  - ES_JAVA_OPTS: -Xms1g -Xmx1g
```

#### Plugins

```yaml
manala_elasticsearch_plugins:
  # Short sytax
  - mobz/elasticsearch-head
  # Verbose syntax
  - name: head
    repository: mobz/elasticsearch-head
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - role: manala.elasticsearch
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
