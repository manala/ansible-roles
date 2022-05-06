# Ansible Role: Aptly Api

This role will deal with the setup of [Aptly Api](https://www.aptly.info/doc/api/).

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

Use template:

```yaml
manala_aptly_api_config_template: my/aptly.conf.j2
manala_aptly_api_config:
  foo: bar
```

Use dict parameters:
```yaml
manala_aptly_api_config:
  rootDir: /tmp/aptly
  architectures:
    - amd64
```

Use raw config:
```yaml
manala_aptly_api_config: |
  {
      "rootDir": "/tmp/aptly",
      "architectures": [
          "amd64"
      ]
  }
```

## Example playbook

 ```yaml
 - hosts: servers
   tasks:
     - import_role:  
        name: manala.roles.aptly_api
 ```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
