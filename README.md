<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: Supervisor

This role will assume the setup of Supervisor

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install elao.supervisor,2.0
```

Using ansible galaxy requirements file:

```yaml
- src:     elao.supervisor
  version: 2.0
```

### Ansible 1 (no longer maintained)

Using ansible galaxy cli:

```bash
ansible-galaxy install elao.supervisor,1.0
```

Using ansible galaxy requirements file:

```yaml
- src:     elao.supervisor
  version: 1.0
```

## Role Handlers

|Name|Type|Description|
|----|----|-----------|
|supervisor restart|Service|Restart supervisor service

## Role Variables

|Name|Default|Type|Description|
|----|-------|----|-----------|
|elao_supervisor_config|{}|Array|Config
|elao_supervisor_configs|[]|Array|Configs

### Configuration example

```yaml
elao_supervisor_config:
  loglevel: info
```

Enable http server

```yaml
elao_supervisor_configs:
  - file:     inet_http_server.conf
    template: configs/inet_http_server_default.conf.j2
    config:
      port:     "*:9001"
```

Program

```yaml
elao_supervisor_configs:
  - file:     foo.conf
    template: configs/program_default.conf.j2
    config:
      name: foo
      command: "bar"
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.supervisor }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
