# Ansible Role: HAProxy [![Build Status](https://travis-ci.org/manala/ansible-role-haproxy.svg?branch=master)](https://travis-ci.org/manala/ansible-role-haproxy)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of [HAProxy](http://www.haproxy.org/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

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
|haproxy reload|Service|Reload haproxy service

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
