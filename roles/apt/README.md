# Ansible Role: Apt [![Build Status](https://travis-ci.org/manala/ansible-role-apt.svg?branch=master)](https://travis-ci.org/manala/ansible-role-apt)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will add third party sources to the package manager by:
- Adding source URL as new repository
- Adding secure key specified
- Managing packages preferences files (aka. pinning)
- Installing packages

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.apt
```

Using ansible galaxy requirements file:

```yaml
- src: manala.apt
```

## Role Handlers

None

## Role Variables

### Definition

| Name                                  | Default                                               | Type    | Description                            |
| ------------------------------------- | ----------------------------------------------------- | ------- | -------------------------------------- |
| `manala_apt_configs_exclusive`        | false                                                 | Boolean | Configurations exclusivity             |
| `manala_apt_configs_dir`              | '/etc/apt/apt.conf.d'                                 | String  | Configurations dir path                |
| `manala_apt_configs_defaults`         | {}                                                    | Array   | Configurations defaults                |
| `manala_apt_configs`                  | []                                                    | Array   | Configurations                         |
| `manala_apt_install_packages`         | ~                                                     | Array   | Dependency packages to install         |
| `manala_apt_install_packages_default` | ['apt-transport-https', 'openssl', 'ca-certificates'] | Array   | Default dependency packages to install |
| `manala_apt_components`               | ['main']                                              | Array   | Collection of components               |
| `manala_apt_sources_list`             | []                                                    | Array   | Collection of sources                  |
| `manala_apt_repositories_exclusive`   | false                                                 | Boolean | Repositories exclusivity               |
| `manala_apt_repositories`             | []                                                    | Array   | Repositories                           |
| `manala_apt_preferences_exclusive`    | false                                                 | Boolean | Preferences exclusivity                |
| `manala_apt_preferences_dir`          | '/etc/apt/preferences.d'                              | String  | Preferences dir path                   |
| `manala_apt_preferences_defaults`     | {}                                                    | Array   | Preferences defaults                   |
| `manala_apt_preferences`              | []                                                    | Array   | Preferences                            |
| `manala_apt_holds_exclusive`          | false                                                 | Array   | Holds exclusivity                      |
| `manala_apt_holds`                    | []                                                    | Array   | Collection of holds                    |
| `manala_apt_packages`                 | []                                                    | Array   | Collection of packages                 |
| `manala_apt_cache_valid_time`         | 3600                                                  | Integer | Permitted age of apt cache, in seconds |
| `manala_apt.update`                   | false                                                 | Boolean | Update packages                        |

### Example

```yaml
- hosts: all
  vars:
    manala_apt_repositories:
      - contrib
    manala_apt_preferences:
      - git@backports
      - dotdeb:100
      - php@dotdeb_php56:300
      - nginx@nginx
    manala_apt_packages:
      - xfonts-75dpi
      - http://download.gna.org/wkhtmltopdf/0.12/0.12.2.1/wkhtmltox-0.12.2.1_linux-{{ ansible_distribution_release }}-amd64.deb
  roles:
    - role: manala.apt
```

### Configs

`manala_apt_configs` allows you to define apt configuration files using template and config, or raw content.

A state (present|absent|ignore) can be provided.

```yaml
manala_apt_configs:
  # Template based (file name based on template)
  - template: configs/check_valid_until_false.j2
  # Template based (force file name)
  - file: check
    template: configs/check_valid_until_false.j2
  # Content based
  - file: foo_content
    config: |
      APT::Install-Recommends "false";
  # Dicts array config based (deprecated)
  - file: foo
    config:
      - Acquire::Check-Valid-Until: true
  # Ensure config is absent
  - file: absent
    state: absent # "present" by default
  # Ignore config
  - file: ignore
    state: ignore
  # Flatten configs
  - "{{ my_custom_configs_array }}"
```

`manala_apt_configs_exclusive` allow you to clean up existing apt configuration files into directory defined by the `manala_apt_configs_dir` key. Made to be sure no old or manually created files will alter current configuration.

```yaml
manala_apt_configs_exclusive: true
```

### Components

Specify apt components

```yaml
manala_apt_components:
  - main
  - contrib
  - non-free
  # Flatten components
  - "{{ my_custom_components_array }}"
```

### Sources list

Define manually each sources

```yaml
manala_apt_sources_list:
  - deb: http://deb.debian.org/debian stretch main
  - deb http://deb.debian.org/debian stretch contrib
```

Or use predefined templates

```yaml
manala_apt_sources_list_template: sources_list/default.j2
```

Or combine both

```yaml
manala_apt_sources_list_template: sources_list/default_src.j2
manala_apt_sources_list:
  - deb-src: http://deb.debian.org/debian stretch main
  - deb-src http://deb.debian.org/debian stretch contrib
```

### Repositories

Concise, pattern based

```yaml
manala_apt_repositories:
  - security
  - updates
  - partner
  - backports
  - backports_sloppy
  - dotdeb
  - nginx
  - bearstech
  - nodesource_0_10
  - nodesource_0_12
  - nodesource_4
  - nodesource_5
  - nodesource_6
  - nodesource_7
  - nodesource_8
  - nodesource_10
  - nodesource_12
  - nodesource_14
  - postgresql
  - maxscale_2_2
  - mongodb_3_0
  - mongodb_3_2
  - mongodb_3_4
  - mongodb_3_6
  - mongodb_4_0
  - mongodb_4_2
  - varnish_4_0
  - jenkins
  - sensu
  - rabbitmq
  - proxmox
  - proxmox_enterprise
  - logentries
  - galera_3
  - grafana
  - elasticsearch_1_5
  - elasticsearch_1_6
  - elasticsearch_1_7
  - elasticsearch_2
  - elasticsearch_5
  - elasticsearch_6
  - elasticsearch_7
  - ppa_ansible
  - blackfire
  - sury_php
```

Verbose, pattern based

```yaml
manala_apt_repositories:
  - pattern: backports
    state: absent
```

Verbose

```yaml
manala_apt_repositories:
  - source: deb http://pkg.jenkins-ci.org/debian binary/
    key:
      url: http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key
      id:  D50582E6
  - source: deb https://enterprise.proxmox.com/debian {{ ansible_distribution_release }} pve-enterprise
    state: absent
  # Ignore repository
  - source: deb https://example.com foo
    state: ignore
  # Flatten repositories
  - "{{ my_custom_repositories_array }}"
```

Exclusivity (all repositories non defined by role will be deleted)

```yaml
manala_apt_repositories_exclusive: true
```

### Preferences

Concise, pattern based

Format: [preference pattern]@[repository pattern]:[pin priority]

Note that referenced repositories will automatically be include as present using "manala_apt_repositories" process.

```yaml
manala_apt_preferences:
  - git@backports         # "git*"" from debian backports repository, high priority
  - dotdeb:100            # "*" from dotdeb repository, low priority
  - php@dotdeb            # "php*" from dotdeb repository, high priority
  - redis@dotdeb          # "redis*" from dotdeb repository, high priority
  - libssl1.0.0@backports # "libssl1.0.0" from debian backports repository, high priority (in this case "libssl1.0.0" is not a pre-defined preference pattern; as a matter of consequence the package is directly used)
  # Pattern syntax
  - preference: ansible@ansible
    file: foo
```

Verbose

```yaml
manala_apt_preferences:
  - package:  '*'
    pin:      release o=Debian,a=stable
    priority: 600
    file:     dotdeb
  - package:  'php-*'
    pin:      release o=Debian,a=stable
    priority: 900
    file:     php
    state:    absent
  # Ignore preference
  - file: foo
    state: ignore
  # Flatten preferences
  - "{{ my_custom_preferences_array }}"
```

### Holds

Handle your holded packages (the ones you don't want to upgrade) using:

```yaml
manala_apt_holds:
  - foo # Ensure "foo" package won't be upgraded
  - package: bar # The same with "bar" package, using verbose syntax
    state: present
  - package: baz # Ensure "baz" package *will* be upgraded
    state: absent
  # Ignore hold
  - package: qux
    state: ignore
  # Deprecated
  - package: quux
    hold: true # or false :)
  # Flatten holds
  - "{{ my_custom_holds_array }}"
```

An exclusivity mode is also provided, to ensure *ALL* packages but the ones you set will be upgradable.

```yaml
manala_apt_holds_exclusive: true
```

### Packages

Concise

```yaml
manala_apt_packages:
  - vim # Name of package
```

Verbose

```yaml
manala_apt_packages:
  - package:  bzip2  # Name of package, required
    state: absent # State of package, optional, default "present"
    force: true   # Force installation, optional
  # Ignore package
  - package: foo
    state: ignore # State of package, optional, default 'present'
  # Flatten packages
  - "{{ my_custom_packages_array }}"
```

### Flags

Update packages
```yaml
manala_apt:
  update: true

# Can also be set across manala roles
manala:
  update: true
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
