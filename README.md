<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: HAProxy

This role will assume the setup of HAProxy

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.haproxy
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.haproxy }
```

## Role Handlers

|Name|Type|Description|
|----|----|-----------|
|haproxy restart|Command|Test config and notify "do haproxy restart" handler
|do haproxy restart|Service|Restart haproxy service

## Role Variables

|Name|Default|Type|Description|
|----|-------|----|-----------|
|elao_haproxy_errorfiles_path|/etc/haproxy/errors|String|Errorfiles path
|elao_haproxy_errorfiles|Array|Array|Errorfiles templates
|elao_haproxy_config_path|/etc/haproxy/haproxy.cfg|String|Config path
|elao_haproxy_config_template|config/http_default.cfg.j2|String|Config template
|elao_haproxy_config|Array|Array|Config

### Configuration example

Handle errorfiles

```yaml
elao_haproxy_errorfiles:
  - name: 400.http
    template: errorfiles/400.http.j2
  - name: maintenance.http
    template: "{{ playbook_dir ~ '/templates/haproxy/errorfiles/maintenance.http.j2' }}"
```

Use default config template, and set/add custom parameters

```yaml
elao_haproxy_config:
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
elao_haproxy_config_template: "{{ playbook_dir ~ '/templates/haproxy/haproxy.cfg.j2' }}"
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.haproxy }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
