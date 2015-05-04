<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: files

This role will assume the configuration of files.

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Dependencies

None.

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.files
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.files }
```

## Role Variables

| Name         | Default | Type  | Description      |
| ------------ | ------- | ----  | ---------------- |
| `elao_files` | {}      | Array | Files attributes |

### Configuration example

```yaml
elao_files:
  - path: /var/log/symfony
    state: directory
  - path: /var/cache/symfony
    state: directory
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.files }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
