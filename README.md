<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: ZSH

This role will assume the following configuration:
- Install zsh package
- Setup a default zprofile file
- Setup a zprofile dir for local files definition

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Dependencies

None.

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.zsh
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.zsh }
```

## Role Handlers

None

## Role Variables

|Name|Default|Type|Description|
|----|----|-----------|-------|
`elao_zsh_profile_path`|None|String (Path)|Path to local definitions.
`elao_zsh_zprofile_template`|None|String|Path to custom zprofile template.

### Configuration example

```
---

elao_zsh_profile_path: "/etc/zprofile.d/"
elao_zsh_zprofile_template: "{{ playbook_dir ~ '/templates/zsh/zprofile.j2' }}"
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.zsh }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)