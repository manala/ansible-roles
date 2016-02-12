<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: nodejs

This role will assume the setup of nodejs.

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install elao.nodejs,2.0
```

Using ansible galaxy requirements file:

```yaml
- src:     elao.nodejs
  version: 2.0
```

### Ansible 1 (no longer maintained)

Using ansible galaxy cli:

```bash
ansible-galaxy install elao.nodejs,1.0
```

Using ansible galaxy requirements file:

```yaml
- src:     elao.nodejs
  version: 1.0
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.nodejs }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
