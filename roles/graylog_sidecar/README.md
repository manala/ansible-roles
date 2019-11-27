# Ansible Role: Graylog_sidecar [![Build Status](https://travis-ci.org/manala/ansible-role-graylog_sidecar.svg?branch=master)](https://travis-ci.org/manala/ansible-role-graylog_sidecar)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the configuration of [Graylog_sidecar](https://github.com/Graylog2/collector-sidecar).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

This role is made to work with the __graylog_sidecar__ official packages, available on the [__graylog_sidecar__ github](https://github.com/Graylog2/collector-sidecar/releases). Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.graylog_sidecar
```

Using ansible galaxy requirements file:

```yaml
- src: manala.graylog_sidecar
```

## Role Variables

| Name                                              | Default                    		| Type    | Description                            |
| --------------------------------------------------| -------------------------- 		| ------- | -------------------------------------- |
| `manala_graylog_sidecar_version`          		| ~                          		| String  | Version to install (mandatory)   	   |
| `manala_graylog_sidecar_install_packages`         | ['https://github.com/Graylog2/collector-sidecar/releases/download/{{ manala_graylog_sidecar_version }}/graylog-sidecar_{{ manala_graylog_sidecar_version }}-1_amd64.deb']           | Array   | Default dependency packages to install |
| `manala_graylog_sidecar_config_file` 				| /etc/graylog/sidecar/sidecar.yml  | String  | Configuration file path         	   |
| `manala_graylog_sidecar_config_template`			| ~  								| String  | Configuration base template path 	   |
| `manala_graylog_sidecar_config` 					| [] 								| Array   | Configuration directives	           |

### Configuration example

## Config

`server_api_token` is required to have a value for graylog-sidecar to start

```yaml
manala_graylog_sidecar_version: 1.0.2
manala_graylog_sidecar_config:
  server_url: http://foo.bar:9000/api
  server_api_token: foo-bar-baz-bar-foo
  node_name: foo.bar.baz.hostname
  ```
# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
