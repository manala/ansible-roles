# Ansible Role: Apt

This role will add third party sources to the package manager by:
- Adding source URL as new repository
- Adding secure key specified
- Managing packages preferences files (aka. pinning)
- Installing packages

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

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

| Name                      | Default  | Type  | Description                |
| ------------------------- | -------- | ----- | -------------------------- |
| `manala_apt_components`   | ['main'] | Array | Collection of components   |
| `manala_apt_sources_list` | []       | Array | Collection of sources      |
| `manala_apt_repositories` | []       | Array | Collection of repositories |
| `manala_apt_preferences`  | []       | Array | Collection of preferences  |
| `manala_apt_packages`     | []       | Array | Collection of packages     |

### Example

```yaml
- hosts: all
  vars:
    manala_apt_repositories:
      - contrib
    manala_apt_preferences:
      - git@debian_backports
      - dotdeb:100
      - php@dotdeb_php56:300
      - nginx@nginx
    manala_apt_packages:
      - ttf-mscorefonts-installer
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
  - deb: http://httpredir.debian.org/debian wheezy main
  - deb http://httpredir.debian.org/debian wheezy contrib
```

Or use predefined templates

```yaml
manala_apt_sources_list_template: sources_list/debian.j2
```

Or combine both

```yaml
manala_apt_sources_list_template: sources_list/debian_src.j2
manala_apt_sources_list:
  - deb-src: http://httpredir.debian.org/debian wheezy main
  - deb-src http://httpredir.debian.org/debian wheezy contrib
```

### Repositories

Concise, pattern based

```yaml
manala_apt_repositories:
  - debian_security
  - debian_security_src
  - debian_updates
  - debian_updates_src
  - debian_backports
  - ubuntu_security
  - ubuntu_updates
  - ubuntu_partner
  - ubuntu_backports
  - dotdeb
  - dotdeb_php54
  - dotdeb_php55
  - dotdeb_php56
  - nginx
  - bearstech
  - nodesource_0_10
  - nodesource_0_12
  - nodesource_4
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
  - galera
  - grafana
  - elasticsearch_1_5
  - elasticsearch_1_6
  - elasticsearch_1_7
  - ppa_ansible
  - blackfire
```

Verbose, pattern based

```yaml
manala_apt_repositories:
  - pattern: debian_backports
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
  - git@debian_backports         # "git*"" from debian backports repository, high priority
  - dotdeb:100                   # "*" from dotdeb repository, low priority
  - php@dotdeb                   # "php*" from dotdeb repository, high priority
  - redis@dotdeb                 # "redis*" from dotdeb repository, high priority
  - libssl1.0.0@debian_backports # "libssl1.0.0" from debian backports repository, high priority (in this case "libssl1.0.0" is not a pre-defined preference pattern; as a matter of consequence the package is directly used)
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
  - name:  bzip2  # Name of package, required
    state: absent # State of package, optionnal, default 'present'
    force: true   # Force installation, optionnal
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
