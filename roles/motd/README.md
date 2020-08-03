# Ansible Role: Message Of The Day [![Build Status](https://travis-ci.org/manala/ansible-role-motd.svg?branch=master)](https://travis-ci.org/manala/ansible-role-motd)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of Message Of The Day.

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.motd
```

Using ansible galaxy requirements file:

```yaml
- src: manala.motd
```

## Role Handlers

None

## Role Variables

| Name                            | Default                | Type    | Description                |
| ------------------------------- | ---------------------- | ------- | -------------------------- |
| `manala_motd_scripts_exclusive` | false                  | Boolean | Scripts exclusivity        |
| `manala_motd_scripts_dir`       | '/etc/update-motd.d'   | String  | Scripts dir path           |
| `manala_motd_scripts_defaults`  | {}                     | Array   | Default scripts parameters |
| `manala_motd_scripts`           | []                     | Array   | Scripts                    |
| `manala_motd_template`          | 'template/_default.j2' | String  | Template path              |
| `manala_motd_message`           | ~                      | String  | Message                    |

### Configuration example

Use scripts (recommended)

```yaml
manala_motd_scripts_exclusive: true # Keep only defined scripts
manala_motd_scripts:
  - file: 10-uname
    template: scripts/uname.j2
  - file: 10-message
    message: Hello world! # Simple custom message
  - file: 30-template
    template: scripts/cow.j2 # Predefined template (cow|dragon|stegosaurus|turkey|yoda)
    message: Hjartað hamast # Icelandic custom message
  - file: 40-raw
    # Raw script
    script: |
      #!/bin/sh
      printf "Hello world!\n"
```

Static template (deprecated)

```yaml
manala_motd_template: template/turkey.j2 # Predefined template (cow|dragon|stegosaurus|turkey|yoda)
manala_motd_message: My awesome message # Custom message
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - role: manala.motd
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
