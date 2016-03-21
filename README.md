# Ansible Role: Supervisor

This role will deal with the setup of Supervisor

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.supervisor,2.0
```

Using ansible galaxy requirements file:

```yaml
- src:     manala.supervisor
  version: 2.0
```

## Role Handlers

|Name|Type|Description|
|----|----|-----------|
|supervisor restart|Service|Restart supervisor service

## Role Variables

|Name|Default|Type|Description|
|----|-------|----|-----------|
|manala_supervisor_config|{}|Array|Config
|manala_supervisor_configs|[]|Array|Configs

### Configuration example

```yaml
manala_supervisor_config:
  loglevel: info
```

Enable http server

```yaml
manala_supervisor_configs:
  - file:     inet_http_server.conf
    template: configs/inet_http_server_default.conf.j2
    config:
      port:     "*:9001"
```

Program

```yaml
manala_supervisor_configs:
  - file:     foo.conf
    template: configs/program_default.conf.j2
    config:
      name: foo
      command: "bar"
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.supervisor }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
