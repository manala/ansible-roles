<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: Apt

This role will add third party sources to the package manager by:
- Adding source URL as new repository
- Adding secure key specified
- Managing packages prefereces files (aka. pinning)

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

|Name|Default|Type|Description|
|----|----|-----------|-------|
`elao_apt`|Array|Dictionnary|Collection of repositories.
`elao_apt.name`|-|String|Name of the repository (alphanumeric, no spaces).
`elao_apt.source`|-|String|A source string for the repository.
`elao_apt.key.url`|-|String (URL)|URL to the secure key.
`elao_apt.key.id`|-|String|Id of the secure key.
`elao_apt.state`|-|String|Used to specify if repository should ben absent or present
`elao_apt.preferences`|Array|Dictionnary|Collection of preferences
`elao_apt.preferences.package`|-|String|Packages involved
`elao_apt.preferences.pin`|-|String|Pin directives
`elao_apt.preferences.priority`|-|Integer|Priority level of the rule


### Configuration example

```
---

elao_apt:
  - name:   jenkins
    source: deb http://pkg.jenkins-ci.org/debian binary/
    key:
      url: http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key
      id:  "D50582E6"
  - name:   proxmox
    source: deb https://enterprise.proxmox.com/debian {{ ansible_distribution_release }} pve-enterprise
    state:  absent
  - name: postgresql
    source: deb http://apt.postgresql.org/pub/repos/apt/ {{ ansible_distribution_release }}-pgdg main
    key:
      url: https://www.postgresql.org/media/keys/ACCC4CF8.asc
      id:  "ACCC4CF8"
  - name: dotdeb
    source: deb http://packages.dotdeb.org {{ ansible_distribution_release }} all
    key:
      url: http://www.dotdeb.org/dotdeb.gpg
      id:  "89DF5277"
    preferences:
      - package:  "php*"
        pin:      origin packages.dotdeb.org
        priority: 100
    preferences:
      - package:  "mysql*"
        pin:      origin packages.dotdeb.org
        priority: 100
    state: present
  - name: dotdeb_php55
    source: deb http://packages.dotdeb.org {{ ansible_distribution_release }}-php55 all
  - name: dotdeb_php56
    source: deb http://packages.dotdeb.org {{ ansible_distribution_release }}-php56 all
  - name: backports
    source: deb http://cdn.debian.net/debian {{ ansible_distribution_release }}-backports main
    preferences:
      - package:  git*
        pin:      release a={{ ansible_distribution_release }}-backports
        priority: 900
      - package:  haproxy*
        pin:      release a={{ ansible_distribution_release }}-backports
        priority: 900
  - name: varnish
    source: deb https://repo.varnish-cache.org/debian/ {{ ansible_distribution_release }} varnish-4.0
    key:
      url: https://repo.varnish-cache.org/debian/GPG-key.txt
      id:  "C4DEFFEB"
    preferences:
      - package:  varnish*
        pin:      origin repo.varnish-cache.org
        priority: 900
  - name: nginx
    source: deb http://nginx.org/packages/debian/ {{ ansible_distribution_release }} nginx
    key:
      url: http://nginx.org/keys/nginx_signing.key
      id:  "7BD9BF62"
    preferences:
      - package:  nginx*
        pin:      origin nginx.org
        priority: 900
  - name: nodejs
    source: deb https://deb.nodesource.com/node_0.12 {{ ansible_distribution_release }} main
    key:
      url: https://deb.nodesource.com/gpgkey/nodesource.gpg.key
      id:  "68576280"
    preferences:
      - package:  nodejs
        pin:      origin deb.nodesource.com
        priority: 900
  - name: mongodb
    source: deb http://repo.mongodb.org/apt/debian {{ ansible_distribution_release }}/mongodb-org/3.0 main
    key:
      url: http://docs.mongodb.org/10gen-gpg-key.asc
      id:  7F0CEB10
    preferences:
      - package:  mongodb-*
        pin:      origin docs.mongodb.org
        priority: 900
  - name: ruby
    source: deb http://deb.bearstech.com/debian {{ ansible_distribution_release }}-bearstech main
    key:
      url: http://deb.bearstech.com/bearstech-archive.gpg
      id:  "90158EE0"
    preferences:
      - package:  ruby*
        pin:      origin deb.bearstech.com
        priority: 900
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.apt }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
