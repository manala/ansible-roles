# Ansible Role: Heka

This role will deal with the install and setup of __Heka__.

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

This role is made to work with the __manala__ heka debian package, available on the __manala__ debian repository. Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

```yaml
manala_apt_repositories:
 - manala
```

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.heka
```

Using ansible galaxy requirements file:

```yaml
- src: manala.heka
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.heka }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
