# Ansible Role: Shorewall

This role will assume the setup of [shorewall](http://shorewall.net/)

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.shorewall
```

Using ansible galaxy requirements file:

```yaml
- src: manala.shorewall
```

## Role Handlers

|Name|Type|Description|
|----|-----------|-------|
`shorewall restart`|Service|Restart shorewall

## Role Variables (See [Shorewall documentation](http://shorewall.net/Documentation_Index.html) for further informations)

### Configuration templates

|Name|Default|Type|Description|
|----|----|-----------|-------|
`manala_shorewall_config_templates.policy`|policy.j2|String (path)|Path to policy template.
`manala_shorewall_config_templates.masq`|masq.j2|String (path)|Path to masq template.
`manala_shorewall_config_templates.interfaces`|interfaces.j2|String (path)|Path to interfaces template.
`manala_shorewall_config_templates.zones`|zones.j2|String (path)|Path to zones template.
`manala_shorewall_config_templates.rules`|rules.j2|String (path)|Path to rules template.


### Configuration definitions

|Name|Default|Type|Description|
|----|----|-----------|-------|
`manala_shorewall_config.zones`|Empty collection|Collection|Definition of shorwall zones.
`manala_shorewall_config.rules`|Empty collection|Collection|Definition of firewall rules.
`manala_shorewall_config.masq`|Empty collection|Collection|Definition of shorewall masqs.
`manala_shorewall_config.policy`|Empty collection|Collection|Definition of policy.

### Configuration example

#### Shorewall configuration with custom templates

```
---

manala_shorewall_config_templates:
    policy:      "{{ playbook_dir ~ '/templates/shorewall/policy.j2' }}"
    masq:        "{{ playbook_dir ~ '/templates/shorewall/masq.j2' }}"
    interfaces:  "{{ playbook_dir ~ '/templates/shorewall/interfaces.j2' }}"
    zones:       "{{ playbook_dir ~ '/templates/shorewall/zones.j2' }}"
    rules:       "{{ playbook_dir ~ '/templates/shorewall/rules.j2' }}"
```

#### Shorewall configuration with default templates
```
manala_shorewall_config:
  zones:
    - name: fw
      type: firewall
    - name: net
      type: ipv4
      interface:
        name:       vmbr0
        broadcast:  detect
        options:    "blacklist,routeback,bridge,nosmurfs"
    - name: dmz
      type: ipv4
      interface:
        name:       venet0
        broadcast:  detect
        options:    routeback
    - name: vrack
      type: ipv4
      interface:
        name:       vmbr1
        broadcast:  detect
        options:    "blacklist,routeback,bridge,nosmurfs"

  rules:
    - Permit access to SSH
    - { action: SSH/ACCEPT,  source: net, dest: fw }
    - Access to LB
    - { action: ACCEPT,      source: net, dest: "dmz:XXX.XXX.XXX.XXX", proto: tcp, dest_port: "80,443" }
    - Permit access to Proxmox Manager and Console
    - { action: ACCEPT,      source: net, dest: fw,                  proto: tcp, dest_port: "443,8006" }
    - PING Rules
    - { action: Ping/ACCEPT, source: all, dest: all }

  masq:
    - { interface: vmbr0, source: 172.16.0.0/24 }

  policy:
    - From Firewall
    - { source: fw,    dest: fw,    policy: ACCEPT }
    - { source: fw,    dest: net,   policy: ACCEPT }
    - { source: fw,    dest: vrack, policy: ACCEPT }
    - { source: fw,    dest: dmz,   policy: ACCEPT }
    - From DMZ
    - { source: dmz,   dest: dmz,   policy: ACCEPT }
    - { source: dmz,   dest: net,   policy: ACCEPT }
    - { source: dmz,   dest: vrack, policy: ACCEPT }
    - { source: dmz,   dest: fw,    policy: DROP,   log: info }
    - VRACK
    - { source: vrack, dest: dmz,   policy: ACCEPT }
    - { source: vrack, dest: fw,    policy: ACCEPT }
    - Public Bridge (read the policy warnings!)
    - { source: net,   dest: net,   policy: DROP }
    - { source: net,   dest: fw,    policy: DROP,   log: info }
    - { source: net,   dest: dmz,   policy: DROP,   log: info }
    - THE FOLLOWING POLICY MUST BE LAST
    - { source: all,   dest: all,   policy: REJECT, log: info }
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.shorewall }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
