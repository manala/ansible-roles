# Ansible Role: Backup Manager

This role will deal with the setup of [backup-manager](https://github.com/sukria/Backup-Manager).

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.


## Requirements

This role is made to work with the __manala__ backup-manager debian package, available on the __manala__ debian repository. Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

```yaml
manala_apt_preferences:
 - backup-manager@manala
```

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.backup-manager
```

Using ansible galaxy requirements file:

```yaml
- src: manala.backup-manager
```

## Role Variables

| Name                                | Default                      | Type   | Description          |
| ----------------------------------- | ---------------------------- | ------ | -------------------- |


### Configuration example

```yaml
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.backup-manager }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
