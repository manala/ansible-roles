<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: Packages repositories

This role will add third party sources to the package manager by:
- Adding source URL as new repository
- Addin GPG key specified
- Managing packages pin files 

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Dependencies

None.

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.packages-repositories
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.packages-repositories }
```

## Role Handlers

None

## Role Variables

### Definition

|Name|Default|Type|Description|
|----|----|-----------|-------|
`elao_packages_repositories`|Array|Dictionnary|Collection of repositories.
`elao_packages_repositories.name`|-|String|Name of the repository.
`elao_packages_repositories.source`|-|String|A source string for the repository..
`elao_packages_repositories.gpg_key`|-|String (URL)|URL to the key.
`elao_packages_repositories.state`|-|String|used to specify if item is being added or revoked
`elao_packages_repositories_config_template`|None|String (path)|Path to a custom `pinning` template
`elao_packages_repositories_pinning`|Array|Dictionnary|Collection of pinning rules
`elao_packages_repositories_pinning.name`|-|String|Name of the rule
`elao_packages_repositories_pinning.package`|-|String|Packages involved
`elao_packages_repositories_pinning.pin`|-|String|Pin directives
`elao_packages_repositories_pinning.priority`|-|Integer|Priority level of the rule


### Configuration example

```
---

elao_packages_repositories:
    - name:     dotdeb
      source:   deb http://packages.dotdeb.org {{ ansible_distribution_release }} all
      gpg_key:  http://www.dotdeb.org/dotdeb.gpg
      state:    present
    - name:     dotdeb-dist-php55
      source:   deb http://packages.dotdeb.org {{ ansible_distribution_release }}-php55 all
      gpg_key:  ~
      state:    absent
    - name:     dotdeb-dist-php56
      source:   deb http://packages.dotdeb.org {{ ansible_distribution_release }}-php56 all
      state:    present
    - name:     backports
      source:   deb http://debian.proxad.net/debian {{ ansible_distribution_release }}-backports main
      state:    present

elao_packages_repositories_config_template: "{{ playbook_dir ~ '/templates/source-repositories/pinning.j2' }}"

elao_packages_repositories_pinning:
    - name:     dotdeb
      package:  "*"
      pin:      origin packages.dotdeb.org
      priority: 100
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.packages-repositories }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)