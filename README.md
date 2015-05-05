<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: Apt

This role will add third party sources to the package manager by:
- Adding source URL as new repository
- Adding secure key specified
- Managing packages prefereces files (aka. pinning)
- Installing packages

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

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

### Configuration example

```
---

elao_apt_packages:
  - name: mysql-client
  - name: mysql-server
    state: absent

elao_apt_repositories:
  # Remove proxmox entreprise
  - source: deb https://enterprise.proxmox.com/debian {{ ansible_distribution_release }} pve-enterprise
    state:  absent
  # Jenkins
  - source: deb http://pkg.jenkins-ci.org/debian binary/
    key:
      url: http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key
      id:  D50582E6
  # postgreSQL
  - source: deb http://apt.postgresql.org/pub/repos/apt/ {{ ansible_distribution_release }}-pgdg main
    key:
      url: https://www.postgresql.org/media/keys/ACCC4CF8.asc
      id:  ACCC4CF8
  # Dotdeb
  - source: deb http://packages.dotdeb.org {{ ansible_distribution_release }} all
    key:
      url: http://www.dotdeb.org/dotdeb.gpg
      id:  89DF5277
  # Dotdeb PHP 5.5
  - source: deb http://packages.dotdeb.org {{ ansible_distribution_release }}-php55 all
  # Dotdeb PHP 5.6
  - source: deb http://packages.dotdeb.org {{ ansible_distribution_release }}-php56 all
  # Backports
  - source: deb http://cdn.debian.net/debian {{ ansible_distribution_release }}-backports main
  # Varnish
  - source: deb https://repo.varnish-cache.org/debian/ {{ ansible_distribution_release }} varnish-4.0
    key:
      url: https://repo.varnish-cache.org/debian/GPG-key.txt
      id:  C4DEFFEB
  # Nginx
  - source: deb http://nginx.org/packages/debian/ {{ ansible_distribution_release }} nginx
    key:
      url: http://nginx.org/keys/nginx_signing.key
      id:  7BD9BF62
  # NodeJS
  - source: deb https://deb.nodesource.com/node_0.12 {{ ansible_distribution_release }} main
    key:
      url: https://deb.nodesource.com/gpgkey/nodesource.gpg.key
      id:  68576280
  # MongoDB
  - source: deb http://repo.mongodb.org/apt/debian {{ ansible_distribution_release }}/mongodb-org/3.0 main
    key:
      url: http://docs.mongodb.org/10gen-gpg-key.asc
      id:  7F0CEB10
  # Ruby
  - source: deb http://deb.bearstech.com/debian {{ ansible_distribution_release }}-bearstech main
    key:
      url: http://deb.bearstech.com/bearstech-archive.gpg
      id:  90158EE0

elao_apt_preferences:
  # Dotdeb
  - file: dotdeb
    config:
      Package:       php* mysql*
      Pin:           origin packages.dotdeb.org
      Pin-Priority:  100
  # Backports
  - file: backports
    config:
      Package:       git* haproxy*
      Pin:           release a={{ ansible_distribution_release }}-backports
      Pin-Priority:  900
  # Haproxy
  - file: haproxy
    config:
      Package:       haproxy*
      Pin:           release a={{ ansible_distribution_release }}-backports
      Pin-Priority:  900
  # Varnish
  - file: varnish
    config:
      Package:       varnish*
      Pin:           origin repo.varnish-cache.org
      Pin-Priority:  900
  # Nginx
  - file: nginx
    config:
      Package:       nginx*
      Pin:           origin nginx.org
      Pin-Priority:  900
  # NodeJS
  - file: nodejs
    config:
      Package:       nodejs
      Pin:           origin deb.nodesource.com
      Pin-Priority:  900
  # MongoDB
  - file: mongodb
    config:
      Package:       mongodb-*
      Pin:           origin docs.mongodb.org
      Pin-Priority:  900
  - file: ruby
    config:
      Package:       ruby*
      Pin:           origin deb.bearstech.com
      Pin-Priority:  900
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.apt }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
