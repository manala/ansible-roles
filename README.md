# Ansible Role: Bind

This role will assume the setup of local nameserver via bind.

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.bind
```

Using ansible galaxy requirements file:

```yaml
- src: manala.bind
```

## Role Handlers

|Name|Type|Description|
|----|-----------|-------|
`bind reload`|Service|Reload bind server configuration

## Role Variables

|Name|Default|Type|Description|
|----|----|-----------|-------|
`manala_bind_config_templates`|Array|Array|List of config files.
`manala_bind_config_templates.named_conf`|-|String (filepath)|Custom path to global config file.
`manala_bind_config_templates.named_conf_local`|-|String (filepath)|Custom path to local config file.
`manala_bind_config_templates.named_conf_options`|-|String (filepath)|Custom path to options config file.
`manala_bind_zones`|Array|Array|List of domain zones.
`manala_bind_zones.domain`|-|String| domain name and TLD (Ex: manala.com).
`manala_bind_zones.network`|-|String (filepath)|Zone network definition (Ex:172.16.1.0/24).
`manala_bind_zones.responsible`|-|String (Email)|Contact mail address.

### Configuration example

#### Bind configuration with custom template files

```
---

manala_bind_config_templates:
    named_conf:             "{{ playbook_dir ~ '/files/bind/named.conf.j2' }}"
    named_conf_local:       "{{ playbook_dir ~ '/files/bind/named.conf.local.j2' }}"
    named_conf_options:     "{{ playbook_dir ~ '/files/bind/named.conf.options.j2' }}"

manala_bind_zones_templates:
    "{{ playbook_dir ~ '/files/bind/zones' }}"
```

#### Bind custom files example:

```
#db.mydomain.local

$TTL    86400
@       IN      SOA     ns-1.{{ item.domain }}. {{ item.responsible }}. (
                        2014060203         ; Serial
                            604800         ; Refresh
                             86400         ; Retry
                           2419200         ; Expire
                             86400 )       ; Negative Cache TTL


@               IN      NS      ns-1.{{ item.domain }}.
@               IN      NS      ns-2.{{ item.domain }}.
```

```
#rev.mydomain.local

@ IN SOA ns-1.{{ item.domain }}. {{ item.responsible }}. (
                        2015020501;
                        28800;
                        604800;
                        604800;
                        86400
)

{{ item.network|regex_replace('^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})/([0-9]{1,2})$', '\\3.\\2.\\1') }}.in-addr.arpa.  IN    NS     ns-1.{{ item.domain }}.
{{ item.network|regex_replace('^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})/([0-9]{1,2})$', '\\3.\\2.\\1') }}.in-addr.arpa.  IN    NS     ns-2.{{ item.domain }}.

172.16.0.1              IN    PTR    ouranos.{{ item.domain }}.
172.16.0.11             IN    PTR    ns-1.{{ item.domain }}.
```

#### Bind zones configuration:

```
manala_bind_zones:
  - domain:         mydomain.local
    responsible:    contact_email@manala.io
    network:        "172.16.0.0/24"

  - domain:         manala.local
    responsible:    contact_email@manala.io
    network:        "172.16.1.0/24"
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.bind }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
