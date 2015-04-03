<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: Apt repositories

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
ansible-galaxy install elao.apt-repositories
```

## Role Handlers

None

## Role Variables

### Definition

|Name|Default|Type|Description|
|----|----|-----------|-------|
`elao_apt_repositories`|Array|Dictionnary|Collection of repositories.
`elao_apt_repositories.name`|-|String|Name of the repository (alphanumeric, no spaces).
`elao_apt_repositories.source`|-|String|A source string for the repository.
`elao_apt_repositories.key.url`|-|String (URL)|URL to the secure key.
`elao_apt_repositories.key.id`|-|String|Id of the secure key.
`elao_apt_repositories.state`|-|String|Used to specify if repository should ben absent or present
`elao_apt_repositories.preferences`|Array|Dictionnary|Collection of preferences
`elao_apt_repositories.preferences.package`|-|String|Packages involved
`elao_apt_repositories.preferences.pin`|-|String|Pin directives
`elao_apt_repositories.preferences.priority`|-|Integer|Priority level of the rule


### Configuration example

```
---

elao_apt_repositories:
  - name:   jenkins
    source: deb http://pkg.jenkins-ci.org/debian binary/
    key:
      url: http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key
      id:  "D50582E6"
  - name:   proxmox
    source: deb https://enterprise.proxmox.com/debian wheezy pve-enterprise
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
      - package:  "*"
        pin:      origin packages.dotdeb.org
        priority: 100
    state: present
  - name: dotdeb_php55
    source: deb http://packages.dotdeb.org {{ ansible_distribution_release }}-php55 all
  - name: dotdeb_php56
    source: deb http://packages.dotdeb.org {{ ansible_distribution_release }}-php56 all
  - name: backports
    source: deb http://cdn.debian.net/debian {{ ansible_distribution_release }}-backports main
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.apt-repositories }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
