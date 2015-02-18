<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: Shorewall

This role will assume the setup of [shorewall] (http://shorewall.net/)

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Dependencies

None.

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.shorewall
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.shorewall }
```

## Role Handlers

|Name|Type|Description|
|----|-----------|-------|
`shorewall restart`|Service|Restart shorewall

## Role Variables (See [Shorewall documentation](http://shorewall.net/Documentation_Index.html) for further informations)

### Custom configuration definition

|Name|Default|Type|Description|
|----|----|-----------|-------|
`elao_shorewall_files.zones`|Null|String (filepath)|Custom path to zones file.
`elao_shorewall_files.interfaces`|Null|String (filepath)|Custom path to interfaces file.
`elao_shorewall_files.rules`|Null|String (filepath)|Custom path to rules file.
`elao_shorewall_files.masq`|Null|String (filepath)|Custom path to masq file.
`elao_shorewall_files.policy`|Null|String (filepath)|Custom path to policy file.

### Default configuration definition (provided by the role)

|Name|Default|Type|Description|
|----|----|-----------|-------|
`elao_shorewall_config.zones`|Empty collection|Collection|Definition of shorwall zones.
`elao_shorewall_config.rules`|Empty collection|Collection|Definition of firewall rules.
`elao_shorewall_config.masq`|Empty collection|Collection|Definition of shorewall masqs.
`elao_shorewall_config.policy`|Empty collection|Collection|Definition of policy.

### Configuration example

#### Shorewall configuration with custom template files

```
---

elao_shorewall_files:
    zones:       "{{ playbook_dir ~ '/files/shorewall/zones.j2' }}"
    interfaces:  "{{ playbook_dir ~ '/files/shorewall/interfaces.j2' }}"
    rules:       "{{ playbook_dir ~ '/files/shorewall/rules.j2' }}"
    masq:        "{{ playbook_dir ~ '/files/shorewall/masq.j2' }}"
    policy:      "{{ playbook_dir ~ '/files/shorewall/policy.j2' }}"

```

#### Shorewall configuration with default template files (provided by the role)
```
elao_shorewall_config:
  zones:
    fw:
      type:         firewall
    net:
      type:         ipv4
      interface:
        name:       vmbr0
        broadcast:  detect
        options:    "blacklist,routeback,bridge,nosmurfs"
    dmz:
      type:         ipv4
      interface:
        name:       venet0
        broadcast:  detect
        options:    routeback
    vrack:
      type:         ipv4
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

    - hosts: servers
      roles:
         - { role: elao.shorewall }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)