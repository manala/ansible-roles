<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: npm

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install elao.npm,2.0
```

Using ansible galaxy requirements file:

```yaml
- src:     elao.npm
  version: 2.0
```

### Ansible 1 (no longer maintained)

Using ansible galaxy cli:

```bash
ansible-galaxy install elao.npm,1.0
```

Using ansible galaxy requirements file:

```yaml
- src:     elao.npm
  version: 1.0
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
