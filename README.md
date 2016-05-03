# Ansible Role: Mongo Express

This role will deal with the setup and install of __Mongo Express__.

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

This role is made to work with the __manala__ node-mongo-express debian package, available on the __manala__ debian repository. Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

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
ansible-galaxy install manala.mongo-express,2.0
```

Using ansible galaxy requirements file:

```yaml
- src: manala.mongo-express
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.mongo-express }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
