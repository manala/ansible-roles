<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: Heka

This role will install Heka

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install elao.heka,2.0
```

Using ansible galaxy requirements file:

```yaml
- src:     elao.heka
  version: 2.0
```

### Ansible 1 (no longer maintained)

Using ansible galaxy cli:

```bash
ansible-galaxy install elao.heka,1.0
```

Using ansible galaxy requirements file:

```yaml
- src:     elao.heka
  version: 1.0
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.heka }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
