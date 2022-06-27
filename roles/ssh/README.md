# Ansible Role: SSH

This role will deal with the following configuration:
- Allow sudo authentication over ssh
- Enable/Disable the SSH daemon password authentication
- Set the SSH daemon accepted environment variables
- Set ssh know hosts

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

None.

## Dependencies

None.

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Configuration example

Install client only
```yaml
manala_ssh_server: false  # Default true
```

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
  tasks:
    - ansible.builtin.import_role:  
        name: manala.roles.ssh
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
