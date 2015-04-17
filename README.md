<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: Alternatives

This role will assume the setup of alternatives

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.alternatives
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.alternatives }
```

## Role Variables

|Name|Default|Type|Description|
|----|-------|----|-----------|
|elao_alternatives|[]|Array|Alternatives

### Configuration example

```yaml
elao_alternatives:
  - name: editor
    path: /usr/bin/vim.basic
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.alternatives }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
