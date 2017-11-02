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

| Name                          | Default  | Type  | Description                            |
| ----------------------------- | -------- | ----- | -------------------------------------- |
| `manala_apt_components`       | ['main'] | Array | Collection of components               |
| `manala_apt_sources_list`     | []       | Array | Collection of sources                  |
| `manala_apt_repositories`     | []       | Array | Collection of repositories             |
| `manala_apt_preferences`      | []       | Array | Collection of preferences              |
| `manala_apt_packages`         | []       | Array | Collection of packages                 |
| `manala_apt_cache_valid_time` | 3600     | Int   | Permitted age of apt cache, in seconds |

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

### Components

Specify apt components

```yaml
manala_apt_components: ['main', 'contrib', 'non-free']
```

### Sources list

Define manually each sources

```yaml
manala_apt_sources_list:
  - deb: http://deb.debian.org/debian wheezy main
  - deb http://deb.debian.org/debian wheezy contrib
```

Or use predefined templates

```yaml
manala_apt_sources_list_template: sources_list/default.j2
```

Or combine both

```yaml
manala_apt_sources_list_template: sources_list/default_src.j2
manala_apt_sources_list:
  - deb-src: http://deb.debian.org/debian wheezy main
  - deb-src http://deb.debian.org/debian wheezy contrib
```

### Repositories

Concise, pattern based

```yaml
manala_apt_repositories:
  - security # Distribution auto-detection
  - updates # Distribution auto-detection
  - partner # Distribution auto-detection
  - backports # Distribution auto-detection
  - backports_sloppy # Distribution auto-detection
  - debian_security # Deprecated, use 'security'
  - debian_security_src # Deprecated, use 'security_src'
  - debian_updates # Deprecated, use 'updates'
  - debian_updates_src # Deprecated, use 'updates_src'
  - debian_backports # Deprecated, use 'backports'
  - ubuntu_security # Deprecated, use 'security'
  - ubuntu_updates # Deprecated, use 'updates'
  - ubuntu_partner # Deprecated, use 'partner'
  - ubuntu_backports # Deprecated, use 'backports'
  - dotdeb
  - dotdeb_php54
  - dotdeb_php55
  - dotdeb_php56
  - nginx
  - bearstech
  - nodesource_0_10
  - nodesource_0_12
  - nodesource_4
  - nodesource_5
  - nodesource_6
  - nodesource_7
  - nodesource_8
  - postgresql
  - mongodb_3_0
  - mongodb_3_1
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
  - ppa_ansible
  - blackfire
  - sury_php # Distribution auto-detection
  - sury_php_debian # Deprecated, use 'sury_php'
  - sury_php_ubuntu # Deprecated, use 'sury_php'
```

Verbose, pattern based

```yaml
manala_apt_repositories:
  - pattern: backports
    state:   absent
```

Verbose

```yaml
manala_apt_repositories:
  - source: deb http://pkg.jenkins-ci.org/debian binary/
    key:
      url: http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key
      id:  D50582E6
  - source: deb https://enterprise.proxmox.com/debian {{ ansible_distribution_release }} pve-enterprise
    state:  absent
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
  - git@backports         # "git*"" from debian|ubuntu backports repository, high priority
  - dotdeb:100            # "*" from dotdeb repository, low priority
  - php@dotdeb            # "php*" from dotdeb repository, high priority
  - redis@dotdeb          # "redis*" from dotdeb repository, high priority
  - libssl1.0.0@backports # "libssl1.0.0" from debian|ubuntu backports repository, high priority (in this case "libssl1.0.0" is not a pre-defined preference pattern; as a matter of consequence the package is directly used)
```

Verbose

```yaml
manala_apt_preferences:
  - package:  '*'
    pin: release o=Debian,a=stable
    priority: 600
    file:     dotdeb
  - package:  'php-*'
    pin:      release o=Debian,a=stable
    priority: 900
    file:     php
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
    state: absent # State of package, optionnal, default 'present'
    force: true   # Force installation, optionnal
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
