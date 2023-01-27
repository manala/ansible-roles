# Ansible Role: Elasticsearch

This role will deal with the setup of [Elasticsearch](https://www.elastic.co/fr/products/elasticsearch).

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

None.

## Dependencies

None.

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

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
  tasks:
    - ansible.builtin.import_role:  
        name: manala.roles.elasticsearch
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
