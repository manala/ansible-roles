<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: Apt

This role will add third party sources to the package manager by:
- Adding source URL as new repository
- Adding secure key specified
- Managing packages preferences files (aka. pinning)
- Installing packages

## Requirements

- Ansible 1.8.0+

## Dependencies

None.

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.apt,1.0
```

## Role Handlers

None

## Role Variables

### Definition

| Name                    | Default  | Type  | Description                |
| ----------------------- | -------- | ----- | -------------------------- |
| `elao_apt_update`       | False    | Bool  | Update                     |
| `elao_apt_upgrade`      | False    | Bool  | Upgrade                    |
| `elao_apt_components`   | ['main'] | Array | Collection of components   |
| `elao_apt_sources_list` | []       | Array | Collection of sources      |
| `elao_apt_repositories` | []       | Array | Collection of repositories |
| `elao_apt_preferences`  | []       | Array | Collection of preferences  |
| `elao_apt_packages`     | []       | Array | Collection of packages     |

### Example

```yaml
- hosts: all
  vars:
    elao_apt_update: true
    elao_apt_repositories:
      - contrib
    elao_apt_preferences:
      - git@backports
      - ~@dotdeb:100
      - php@dotdeb_php56
      - nginx@nginx
    elao_apt_packages:
      - ttf-mscorefonts-installer
  roles:
    - role: elao.apt
```

### Update

Update packages

```yaml
elao_apt_update: true
```

### Upgrade

Upgrade packages

```yaml
elao_apt_upgrade: true
```

### Components

Specify apt components

```yaml
elao_apt_components: ['main', 'contrib', 'non-free']
```

### Sources list

Define manually each sources

```yaml
elao_apt_sources_list:
  - deb: http://httpredir.debian.org/debian wheezy main
  - deb http://httpredir.debian.org/debian wheezy contrib
```

Or use predefined templates

```yaml
elao_apt_sources_list_template: sources_list/debian.list.j2
```

Or combine both

```yaml
elao_apt_sources_list_template: sources_list/debian_src.list.j2
elao_apt_sources_list:
  - deb-src: http://httpredir.debian.org/debian wheezy main
  - deb-src http://httpredir.debian.org/debian wheezy contrib
```

### Repositories

Concise, pattern based

```yaml
elao_apt_repositories:
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
  - proxmox_enterprise
  - logentries
  - galera
  - grafana
  - elasticsearch_1_5
  - elasticsearch_1_6
  - elasticsearch_1_7
  - ppa_ansible
```

Verbose, pattern based

```yaml
elao_apt_repositories:
  - pattern: backports
    state:   absent
```

Verbose

```yaml
elao_apt_repositories:
  - source: deb http://pkg.jenkins-ci.org/debian binary/
    key:
      url: http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key
      id:  D50582E6
  - source: deb https://enterprise.proxmox.com/debian {{ ansible_distribution_release }} pve-enterprise
    state:  absent
```

### Preferences

Concise, pattern based

Format: [preference pattern]@[repository pattern]:[pin priority]

Note that referenced repositories will automatically be include as present using "elao_apt_repositories" process.

```yaml
elao_apt_preferences:
  - git@backports # git* from backports reposotiry, high priority
  - ~@dotdeb:100  # all from dotdeb repository, low priority
  - php@dotdeb    # php* from backports reposotiry, high priority
```

Verbose

```yaml
elao_apt_preferences:
  - file: dotdeb
    config:
      - Package:      '*'
      - Pin:          origin packages.dotdeb.org
      - Pin-Priority: 100
  - file: php
    config:
      - Package:       php*
      - Pin:           origin packages.dotdeb.org
      - Pin-Priority:  900
```

### Packages

Concise

```yaml
elao_apt_packages:
  - vim # Name of package
```

Verbose

```yaml
elao_apt_packages:
  - name:  bzip2  # Name of package, required
    state: absent # State of package, optionnal, default 'present'
    force: true   # Force installation, optionnal
```

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
