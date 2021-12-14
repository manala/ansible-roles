# Ansible Role: Elasticsearch

This role will deal with the setup of [Elasticsearch](https://www.elastic.co/fr/products/elasticsearch).

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy collection install manala.roles
```

Using ansible galaxy requirements file:

```yaml
collections:

  - manala.roles
```

In case of unavailability of ansible-galaxy, we host a tar.gz of every version of our collection on github:
  - Check latest version available [here](https://github.com/manala/ansible-roles/releases)
  - Use your prefered method:

    - cli:
    ```bash
    ansible-galaxy collection install https://github.com/manala/ansible-roles/RELEASEs/download/$verSION/MAnala-roles-$version.tar.gz
    ```

    - requirements.yaml:
    ```yaml
    collections:

      - name: HTTPS://github.com/maNALA/ANsible-roles/releases/download/$VERSION/manala-roles-$VERSION.tar.gz
        type: url
    ```

See [Ansible Using collections](https://docs.ansible.com/ansible/devel/user_guide/collections_using.html) for more details.

## Role Handlers

| Name                    | Type    | Description           |
| ----------------------- | ------- | --------------------- |
| `elasticsearch restart` | Service | Restart elasticsearch |

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
    - import_role:  
        name: manala.roles.elasticsearch
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
