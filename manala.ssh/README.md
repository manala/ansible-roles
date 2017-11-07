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

| Name          | Type    | Description          |
| ------------- | ------- | -------------------- |
| ssh reload    | Service | Restart ssh service  |

## Role Variables

| Name                              | Default                                 | Type          | Description                         |
| --------------------------------- | --------------------------------------- | ------------- | ----------------------------------- |
| `manala_ssh_config_file`          | /etc/ssh/ssh_config                     | String (path) | Configuration file path             |
| `manala_ssh_config_template`      | config/[distribution]_[release].j2      | String (path) | Default configuration template      |
| `manala_ssh_config`               | [ ]                                     | Array         | Configuration                       |
| `manala_ssh_config_sshd_file`     | /etc/ssh/sshd_config                    | String (path) | Sshd configuration file path        |
| `manala_ssh_config_sshd_template` | config/sshd/[distribution]_[release].j2 | String (path) | Sshd default configuration template |
| `manala_ssh_config_sshd`          | [ ]                                     | Array         | Sshd configuration                  |
| `manala_ssh_known_hosts`          | [ ]                                     | Array         | Known hosts                         |

### Configuration example

```yaml
# Use default custom templates
manala_ssh_config_template: config/default.[env].j2
manala_ssh_config_sshd_template: config/sshd/default.[env].j2

manala_ssh_config:
  - Host *:
    - SendEnv: LANG LC_* FOO

manala_ssh_config_sshd:
  - AcceptEnv: LANG LC_* FOO
  - Match User bar:
    - AcceptEnv: LANG LC_* BAR

manala_ssh_known_hosts:
  - github.com
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.ssh }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
