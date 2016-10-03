# Ansible Role: Deploy

This role will deal with __Deployment__.

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.

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
