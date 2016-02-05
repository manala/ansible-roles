<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: Message Of The Day

This role is far simple, functionally useless and because of this, essential. It will setup your Message Of The Day on your linux boxes.

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install elao.motd,2.0
```

Using ansible galaxy requirements file:

```yaml
- src:     elao.motd
  version: 2.0
```

### Ansible 1 (no longer maintained)

Using ansible galaxy cli:

```bash
ansible-galaxy install elao.motd,1.0
```

Using ansible galaxy requirements file:

```yaml
- src:     elao.motd
  version: 1.0
```

## Role Handlers

None

## Role Variables

|Name|Default|Type|Description|
|----|----|-----------|-------|
`elao_motd_template`|template/elao.j2|String (path)|Path to custom motd.
`elao_motd`|California 1993|String|A custom message

### Configuration example

Use predefined type (elao|cow|turkey|stegosaurus) with custom message:

```
---

elao_motd_template: template/turkey.j2
elao_motd:          "My awesome message"
```

Use custom template:

```
---

elao_motd_template:  "{{ playbook_dir ~ '/templates/motd.j2' }}"
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.motd }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
