# Ansible Role: Ansible Galaxy

This role will deal with the setup of __Ansible Galaxy__.

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.ansible-galaxy
```

Using ansible galaxy requirements file:

```yaml
- src: manala.ansible-galaxy
```

## Role Variables

| Name                         | Default| Type  | Description  |
|----------------------------- |------- |------ |------------- |
| manala_ansible_galaxy_roles  | []     | Array | Roles        |

### Roles

`manala_ansible_galaxy_roles` allow you to install ansible galaxy roles.

```yaml
manala_ansible_galaxy_roles:
  - manala.app
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.ansible-galaxy }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
