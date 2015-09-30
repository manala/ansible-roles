<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: Apt

This role will add third party sources to the package manager by:
- Adding source URL as new repository
- Adding secure key specified
- Managing packages prefereces files (aka. pinning)
- Installing packages

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.8.0+

## Dependencies

None.

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.apt
```

## Role Handlers

None

## Role Variables

### Definition

| Name                                       | Default                | Type         | Description                         |
| ------------------------------------------ | ---------------------- | ------------ | ----------------------------------- |
| `elao_apt_update`                          | False                  | Bool         | Execute apt update.                 |
| `elao_apt_repositories`                    | [ ]                    | Array        | Collection of repositories.         |
| `elao_apt_repositories.source`             | -                      | String       | A source string for the repository. |
| `elao_apt_repositories.key.url`            | -                      | String (URL) | URL to the secure key.              |
| `elao_apt_repositories.key.id`             | -                      | String       | Id of the secure key.               |
| `elao_apt_preferences`                     | [ ]                    | Array        | Collection of preferences.          |
| `elao_apt_preferences.file`                | -                      | String       | Preference file name.               |
| `elao_apt_preferences.template`            | preferences/default.js | String       | Preference template.                |
| `elao_apt_preferences.config.Package`      | -                      | String       | Packages involved.                  |
| `elao_apt_preferences.config.Pin`          | -                      | String       | Pin directives.                     |
| `elao_apt_preferences.config.Pin-Priority` | -                      | Integer      | Priority level of the rule.         |
| `elao_apt_packages`                        | [ ]                    | Array        | Collection of packages.             |

### Configuration example

Packages, concise:

```
---
elao_apt_packages:
  - bzip2 # Name of package
```

Packages, verbose:

```
---
elao_apt_packages:
  - name:  bzip2  # Required
    state: absent # Optionnal, default 'present'
    force: true   # Optionnal
```

Others:

```
---

elao_apt_update: true

# Use full description, or pre defined patterns
elao_apt_repositories:
  - backports
  - postgresql
  - dotdeb
  - dotdebb_php55
  - dotdebb_php56
  - nginx
  - varnish
  - nodesource
  - mongodb
  - bearstech
  # Use pre-defined template...
  - jenkins
  # ... or full description
  - source: deb http://pkg.jenkins-ci.org/debian binary/
    key:
      url: http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key
      id:  D50582E6
  # Remove proxmox entreprise
  - source: deb https://enterprise.proxmox.com/debian {{ ansible_distribution_release }} pve-enterprise
    state:  absent

elao_apt_preferences:
  # Dotdeb (low priority by default)
  - file: dotdeb
    config:
      - Package:      '*'
      - Pin:          origin packages.dotdeb.org
      - Pin-Priority: 100
  # Php
  - file: php
    config:
      - Package:       php*
      - Pin:           origin packages.dotdeb.org
      - Pin-Priority:  900
  # Mysql
  - file: mysql
    config:
      - Package:       mysql*
      - Pin:           origin packages.dotdeb.org
      - Pin-Priority:  900
  # Nginx
  - file: nginx
    config:
      - Package:       nginx*
      - Pin:           origin nginx.org
      - Pin-Priority:  900
  # Ruby
  - file: ruby
    config:
      - Package:       ruby*
      - Pin:           origin deb.bearstech.com
      - Pin-Priority:  900
  # NodeJS
  - file: nodejs
    config:
      - Package:       nodejs
      - Pin:           origin deb.nodesource.com
      - Pin-Priority:  900
  # Haproxy
  - file: haproxy
    config:
      - Package:       haproxy*
      - Pin:           release a={{ ansible_distribution_release }}-backports
      - Pin-Priority:  900
  # Varnish
  - file: varnish
    config:
      - Package:       varnish*
      - Pin:           origin repo.varnish-cache.org
      - Pin-Priority:  900
  # MongoDB
  - file: mongodb
    config:
      Package:       mongodb-*
      Pin:           origin docs.mongodb.org
      Pin-Priority:  900
  # Backports
  - file: backports
    config:
      - Package:       git* haproxy*
      - Pin:           release a={{ ansible_distribution_release }}-backports
      - Pin-Priority:  900
  # Git
  - file: backports
    config:
      - Package:       git*
      - Pin:           release a={{ ansible_distribution_release }}-backports
      - Pin-Priority:  900
  # Haproxy
  - file: backports
    config:
      - Package:       haproxy*
      - Pin:           release a={{ ansible_distribution_release }}-backports
      - Pin-Priority:  900

```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.apt }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
