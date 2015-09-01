<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: elao.oauth2-proxy

This role will assume the setup of [oauth2-proxy](https://github.com/bitly/oauth2_proxy).

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.9.0+

## Dependencies

None.

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.oauth2-proxy
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.oauth2-proxy }
```

## Role Handlers

| Name                   | Type    | Description          |
| ---------------------- | ------- | -------------------- |
| `oauth2-proxy restart` | Service | Restart oauth2 proxy |

## Role Variables

| Name                                | Default                      | Type   | Description          |
| ----------------------------------- | ---------------------------- | ------ | -------------------- |
| `elao_oauth2_proxy_config_file`     | /etc/oauth2-proxy/config.cfg | String | Config file          |
| `elao_oauth2_proxy_config_template` | config/base.cfg.j2           | String | Config template      |
| `elao_oauth2_proxy_config`          | []                           | Array  | Config               |

### Configuration example

```yaml
elao_oauth2_proxy_config:
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
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.oauth2-proxy }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
