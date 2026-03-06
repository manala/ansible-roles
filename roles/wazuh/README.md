# Ansible Role: Wazuh

This role will deal with the setup of [Wazuh](https://documentation.wazuh.com/current/index.html) components.

It currently supports the **agent** mode. Manager mode may be added in the future.

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

The Wazuh APT repository must be configured before using this role (e.g. via `manala.roles.apt`).

## Dependencies

None.

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/main/README.md)

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yaml](./defaults/main.yaml) file

### Mode

| Variable | Default | Description |
|---|---|---|
| `manala_wazuh_agent` | `true` | Enable agent mode |

### Agent

| Variable | Default | Description |
|---|---|---|
| `manala_wazuh_agent_server` | `~` | Wazuh manager address (used for enrollment via `WAZUH_MANAGER`) |
| `manala_wazuh_agent_authd_password` | `~` | Enrollment password (written to `/var/ossec/etc/authd.pass`) |
| `manala_wazuh_agent_groups` | `[]` | Agent groups for enrollment (joined with `,` via `WAZUH_AGENT_GROUP`) |
| `manala_wazuh_agent_force_enrollment` | `false` | Force re-enrollment via `agent-auth` (useful for manager migration) |

### Install

| Variable | Default | Description |
|---|---|---|
| `manala_wazuh_install_packages` | `~` | Override package list (default: `wazuh-agent`) |

The agent name is automatically set to `inventory_hostname` via `WAZUH_AGENT_NAME`.

### Enrollment

Enrollment happens **at package installation time** via environment variables passed to the Wazuh post-install script. If the package is already installed, `apt` won't re-run the post-install and enrollment is skipped.

To force re-enrollment (e.g. after a manager migration), set `manala_wazuh_agent_force_enrollment: true`. This calls `/var/ossec/bin/agent-auth` explicitly and restarts the agent.

### Configuration

Agent configuration (`ossec.conf`) is **managed by the Wazuh manager** via centralized configuration (`agent.conf`). This role does not manage `ossec.conf` beyond the initial enrollment.

## Example playbook

```yaml
- hosts: all

  vars:
    manala_wazuh_agent_server: wazuh.example.com
    manala_wazuh_agent_authd_password: "{{ lookup('manala_vault', 'infra', 'wazuh/authd')['password'] }}"
    manala_wazuh_agent_groups:
      - linux
      - production

  tasks:
    - ansible.builtin.import_role:
        name: manala.roles.wazuh
```

### Force re-enrollment (manager migration)

```yaml
- hosts: all

  vars:
    manala_wazuh_agent_server: new-wazuh.example.com
    manala_wazuh_agent_authd_password: "{{ lookup('manala_vault', 'infra', 'wazuh/authd')['password'] }}"
    manala_wazuh_agent_force_enrollment: true

  tasks:
    - ansible.builtin.import_role:
        name: manala.roles.wazuh
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
