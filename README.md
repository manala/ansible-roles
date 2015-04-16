<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: npm

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Dependencies

None.

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.npm
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.npm }
```

## Role Variables

| Name                | Default | Type  | Description       |
| ------------------- | ------- | ----  | ----------------- |
| `elao_npm_packages` | [ ]     | Array | Npm packages list |

### Configuration example

```yaml
elao_npm_packages:
  - name:     gulp
    version:  3
    global:   true
  - name:     coffee-script
    path:     /app/path
    version:  1.6.1
```

Package configuration directives : http://docs.ansible.com/npm_module.html

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.npm }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
