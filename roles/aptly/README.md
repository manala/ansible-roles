# Ansible Role: Aptly

This role will deal with the setup of [Aptly](https://www.aptly.info/).

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

None.

## Dependencies

None.

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Configuration example

User:

```yaml
manala_aptly_user: aptly
```

Use template:

```yaml
manala_aptly_config_template: my/aptly.conf.j2
manala_aptly_config:
  foo: bar
```

Use dict parameters:
```yaml
manala_aptly_config:
  rootDir: /tmp/aptly
  architectures:
    - amd64
```

Use raw config:
```yaml
manala_aptly_config: |
  {
      "rootDir": "/tmp/aptly",
      "architectures": [
          "amd64"
      ]
  }
```

Repositories:

```yaml
manala_aptly_repositories:
  - name: buster
    comment: Buster
    component: main
    distribution: buster
    origin: Foo
    label: Bar
    architectures: amd64,arm64
  - name: bullseye
    comment: Bullseye
    component: main
    distribution: bullseye
    origin: Foo
    label: Bar
    architectures: amd64
  # Ignore repository
  - name: ignore
    state: ignore
  # Flatten repositories
  - "{{ my_custom_repositories_array }}"
```

## Example playbook

 ```yaml
 - hosts: servers
   tasks:
     - ansible.builtin.import_role:  
        name: manala.roles.aptly
 ```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
