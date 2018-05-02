# Ansible Role: Message Of The Day [![Build Status](https://travis-ci.org/manala/ansible-role-motd.svg?branch=master)](https://travis-ci.org/manala/ansible-role-motd)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of Message Of The Day.

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.motd
```

Using ansible galaxy requirements file:

```yaml
- src: manala.motd
```

## Role Handlers

None

## Role Variables

| Name                   | Default           | Type   | Description   |
| ---------------------- | ----------------- | ------ | ------------- |
| `manala_motd_template` | template/empty.j2 | String | Template path |
| `manala_motd_message`  | ~                 | String | Message       |

### Configuration example

Use predefined type (manala|cow|turkey|stegosaurus) with custom message:

```yaml
---

manala_motd_template: template/turkey.j2
manala_motd_message:  My awesome message
```

Use custom template:

```yaml
---

manala_motd_template: motd/motd.j2
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.motd }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
