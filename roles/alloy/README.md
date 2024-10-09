# Ansible Role: Alloy

This role will deal with the configuration of [Alloy](https://grafana.com/docs/alloy/latest/).

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

This role is made to work with the __Alloy__ official debian packages, available on the [__grafana__ debian repository](https://grafana.com/docs/agent/latest/set-up/install-agent-linux/#install-on-debian-or-ubuntu). Please use the [**manala.roles.apt**](../apt/) role to handle it properly.

```yaml
manala_apt_preferences:
  - alloy@grafana
```

## Dependencies

None.

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/main/README.md)

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yaml](./defaults/main.yaml) file

### Configuration example

See : https://grafana.com/docs/alloy/latest/configure/


```
manala_alloy_config: |
  # Sample config for Alloy
  # For a full configuration reference, see: https://grafana.com/docs/alloy/latest/get-started/configuration-syntax/.
  
  // Collection: mount a local directory with a certain path spec
  local.file_match "applogs" {
      path_targets = [{"__path__" = "/tmp/app-logs/app.log"}]
  }

  // Collection: Take the file match as input, and scrape those mounted log files
  loki.source.file "local_files" {
      targets    = local.file_match.applogs.targets

      // This specifies which component should process the logs next, the "link in the chain"
      forward_to = [loki.process.add_new_label.receiver]
  }

  // Transformation: pull some data out of the log message, and turn it into a label
  loki.process "add_new_label" {
      stage.logfmt {
          mapping = {
              "extracted_level" = "level",
          }
      }

      // Add the value of "extracted_level" from the extracted map as a "level" label
      stage.labels {
          values = {
              "level" = "extracted_level",
          }
      }

      // The next link in the chain is the local_loki "receiver" (receives the telemetry)
      forward_to = [loki.write.local_loki.receiver]
  }

  // Anything that comes into this component gets written to the loki remote API
  loki.write "local_loki" {
      endpoint {
          url = "http://loki:3100/loki/api/v1/push"
      }
  }
```

## Example playbook

```yaml
- hosts: foo
  tasks:
    - ansible.builtin.import_role:  
        name: manala.roles.alloy
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
