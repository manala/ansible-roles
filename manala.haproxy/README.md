# Ansible Role: HAProxy

This role will assume the setup of HAProxy

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.haproxy
```

Using ansible galaxy requirements file:

```yaml
- src: manala.haproxy
```

## Role Handlers
|Name|Type|Description|
|----|----|-----------|
|haproxy restart|Command|Test config and notify "do haproxy restart" handler
|do haproxy restart|Service|Restart haproxy service

## Role Variables

|Name|Default|Type|Description|
|----|-------|----|-----------|
|manala_haproxy_errorfiles_path|/etc/haproxy/errors|String|Errorfiles path
|manala_haproxy_errorfiles|Array|Array|Errorfiles templates
|manala_haproxy_config_path|/etc/haproxy/haproxy.cfg|String|Config path
|manala_haproxy_config_template|config/http_default.cfg.j2|String|Config template
|manala_haproxy_config|Array|Array|Config

### Configuration example

Handle errorfiles

```yaml
manala_haproxy_errorfiles:
  - name: 400.http
    template: errorfiles/400.http.j2
  - name: maintenance.http
    template: "{{ playbook_dir ~ '/templates/haproxy/errorfiles/maintenance.http.j2' }}"
```

Use default config template, and set/add custom parameters

```yaml
manala_haproxy_config:
  defaults:
    timeout:
      - connect 3000
      - client  30000
      - server  30000
  userlist test:
    user:
      - test insecure-password test
  frontend web:
    bind: 127.0.0.1:80
    acl:
      - test hdr_sub(host) -i test.com
    use_backend:
      - test if test
  backend test:
    mode: http
    server: test test.local:80
    acl:
      - auth http_auth(test)
    http-request: auth realm Customer if !auth
```

Use custom config template

```yaml
manala_haproxy_config_template: "{{ playbook_dir ~ '/templates/haproxy/haproxy.cfg.j2' }}"
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.haproxy }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
