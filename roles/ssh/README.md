# Ansible Role: SSH [![Build Status](https://travis-ci.org/manala/ansible-role-ssh.svg?branch=master)](https://travis-ci.org/manala/ansible-role-ssh)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the following configuration:
- Allow sudo authentication over ssh
- Enable/Disable the SSH daemon password authentication
- Set the SSH daemon accepted environment variables
- Set ssh know hosts

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.ssh
```

Using ansible galaxy requirements file:

```yaml
- src: manala.ssh
```

## Role Handlers

| Name         | Type    | Description         |
| ------------ | ------- | ------------------- |
| `ssh reload` | Service | Restart ssh service |

## Role Variables

| Name                                  | Default                                     | Type         | Description                                |
| ------------------------------------- | ------------------------------------------- | ------------ | ------------------------------------------ |
| `manala_ssh_install_packages`         | ~                                           | Array        | Dependency packages to install             |
| `manala_ssh_install_packages_default` | ['openssh-server']                          | Array        | Default dependency packages to install     |
| `manala_ssh_server`                   | true                                        | Boolean      | Enable server                              |
| `manala_ssh_server_config_file`       | '/etc/ssh/sshd_config'                      | String       | Server configuration file path             |
| `manala_ssh_server_config_template`   | 'config/server/[distribution]_[release].j2' | String       | Server default configuration template path |
| `manala_ssh_server_config`            | ~                                           | Array/String | Server configuration directives            |
| `manala_ssh_client_config_file`       | '/etc/ssh/ssh_config'                       | String       | Client configuration file path             |
| `manala_ssh_client_config_template`   | 'config/client/[distribution]_[release].j2' | String       | Client default configuration template path |
| `manala_ssh_client_config`            | ~                                           | Array/String | Client configuration directives            |
| `manala_ssh_known_hosts`              | []                                          | Array        | Known hosts                                |

### Configuration example

Use default debian templates (recommended)
```yaml
manala_ssh_server_config_template: config/server/debian/sshd_config.j2
manala_ssh_client_config_template: config/client/debian/ssh_config.j2
```

Use dict parameters:
```yaml
manala_ssh_client_config:
  Host *:
    SendEnv: LANG LC_* FOO
manala_ssh_server_config:
  AcceptEnv: LANG LC_* FOO
  Match User bar:
    AcceptEnv: LANG LC_* BAR
```

Use raw config:
```yaml
manala_ssh_client_config: |
  Host *
      SendEnv LANG LC_* FOO
manala_ssh_server_config: |
  AcceptEnv LANG LC_* FOO
  Match User bar
      AcceptEnv LANG LC_* BAR
```

Known hosts
```yaml
manala_ssh_known_hosts:
  - github.com
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - role: manala.ssh
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
