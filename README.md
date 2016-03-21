# Ansible Role: Npm

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.npm
```

Using ansible galaxy requirements file:

```yaml
- src: manala.npm
```

## Role Variables

| Name                  | Default | Type  | Description       |
| --------------------- | ------- | ----  | ----------------- |
| `manala_npm_packages` | [ ]     | Array | Npm packages list |

### Configuration example

```yaml
manala_npm_packages:
  - name:     gulp
    version:  3
    global:   true
  - name:     coffee-script
    path:     /app/path
    version:  1.6.1
```

Package configuration directives : http://docs.ansible.com/npm_module.html

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.npm }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
