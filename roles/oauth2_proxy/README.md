#######################################################################################################

# :exclamation: DEPRECATION :exclamation:

## This repository and the role associated are deprecated.

### You can find our other roles in the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles). You will find informations on its usage on the [collection repository](https://github.com/manala/ansible-roles)

#######################################################################################################

# Ansible Role: OAuth2 Proxy [![Build Status](https://travis-ci.org/manala/ansible-role-oauth2_proxy.svg?branch=master)](https://travis-ci.org/manala/ansible-role-oauth2_proxy)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup and config of [OAuth2 Proxy](https://github.com/bitly/oauth2_proxy).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

This role is made to work with the __manala__ oauth2-proxy debian package, available on the __manala__ debian repository. Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

```yaml
manala_apt_preferences:
  - oauth2-proxy@manala
```

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.oauth2_proxy
```

Using ansible galaxy requirements file:

```yaml
- src: manala.oauth2_proxy
```

## Role Handlers

| Name                   | Type    | Description          |
| ---------------------- | ------- | -------------------- |
| `oauth2 proxy restart` | Service | Restart oauth2 proxy |

## Role Variables

| Name                                          | Default                         | Type   | Description                            |
| ---------------------------------------------- | ------------------------------ | ------ | -------------------------------------- |
| `manala_oauth2_proxy_install_packages`         | ~                              | String | Dependency packages to install         |
| `manala_oauth2_proxy_install_packages_default` | ['oauth2-proxy']               | String | Default dependency packages to install |
| `manala_oauth2_proxy_config_file`              | '/etc/oauth2-proxy/config.cfg' | String | Configuration file path                |
| `manala_oauth2_proxy_config_template`          | ~                              | String | Configuration template path            |
| `manala_oauth2_proxy_config`                   | []                             | Array  | Configuration                          |

### Configuration example

```yaml
manala_oauth2_proxy_config:
  - http_address: 0.0.0.0:80
  - request_logging: true
  - upstreams:
    - http://127.0.0.1:8080/
  - email_domains:
    - manalas.com
  - client_id: oauth2_client_id
  - client_secret: oauth2_client_secret
  - cookie_name: _oauth2_proxy
  - cookie_secret: cookie_secret
  - cookie_domain: .manalas.com
  - cookie_expire: 168h
  - cookie_refresh: 1h
  - cookie_secure: true
  - cookie_httponly: true
  - skip_auth_regex:
    - /foo
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.oauth2_proxy }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
