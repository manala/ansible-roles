<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: Bind

This role will assume the setup of local nameserver via bind.

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Dependencies

None.

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.bind
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.bind }
```

## Role Handlers

|Name|Type|Description|
|----|-----------|-------|
`bind restart`|Service|Restart bind server

## Role Variables

|Name|Default|Type|Description|
|----|----|-----------|-------|
`elao_bind_config_templates`|Array|Array|List of config files.
`elao_bind_config_templates.named_conf`|-|String (filepath)|Custom path to global config file.
`elao_bind_config_templates.named_conf_local`|-|String (filepath)|Custom path to local config file.
`elao_bind_config_templates.named_conf_options`|-|String (filepath)|Custom path to options config file.

`elao_bind_zones`|Array|Array|List of domain zones.
`elao_bind_zones.domain`|-|String| domain name and TLD (Ex: elao.com).
`elao_bind_zones.network`|-|String (filepath)|Zone network definition (Ex:172.16.1.0/24).
`elao_bind_zones.responsible`|-|String (Email)|Contact mail address.

### Configuration example

#### Bind configuration with custom template files

```
---

elao_bind_config_templates:
    named_conf:             "{{ playbook_dir ~ '/files/bind/named.conf.j2' }}"
    named_conf_local:       "{{ playbook_dir ~ '/files/bind/named.conf.local.j2' }}"
    named_conf_options:     "{{ playbook_dir ~ '/files/bind/named.conf.options.j2' }}"

elao_bind_zones_templates:
    "{{ playbook_dir ~ '/files/bind/zones' }}"
```

#### bind configuration with default template files (provided by the role)

```
elao_bind_zones:
  - domain:         mydomain.local
    responsible:    contact_email@elao.com
    network:        "172.16.0.0/24"

  - domain:         elao.local
    responsible:    contact_email@elao.com
    network:        "172.16.1.0/24"
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.bind }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)