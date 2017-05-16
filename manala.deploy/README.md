# Ansible Role: Deploy [![Build Status](https://travis-ci.org/manala/ansible-role-deploy.svg?branch=master)](https://travis-ci.org/manala/ansible-role-deploy)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with __Deployment__.

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.deploy
```

Using ansible galaxy requirements file:

```yaml
- src: manala.deploy
```

## Role Variables

| Name                         | Default| Type  | Description  |
|----------------------------- |------- |------ |------------- |
|                              |        |       |              |

### Tasks

Without options

```yaml
manala_deploy_tasks:
  - foo
  - foo:  ~
    when: "'deploy_demo_master' in group_names"
```

Single or default option

```yaml
manala_deploy_tasks:
  - foo: bar
  - foo: bar
    when: "'deploy_demo_master' in group_names"
```

Multiple options

```yaml
manala_deploy_tasks:
  - foo:
      baz: bar
      bar: baz
  - foo:
      baz: bar
      bar: baz
    when: "'deploy_demo_master' in group_names"
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.deploy }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
