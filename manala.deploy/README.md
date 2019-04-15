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

### Strategies

#### Include strategy

The `include` strategy allows to use a custom strategy to deliver the code to the server.

Example that extracts an archive from AWS S3:

```yaml
manala_deploy_strategy: include
manala_deploy_strategy_include_name: "{{ playbook_dir }}/tasks/deploy-s3-archive.yml"
manala_deploy_strategy_include_options:
  s3_object: "/app/{{ app_version | default('master') }}/latest.tar.gz"
```

> tasks/deploy-s3-archive.yml
```yaml
- name: strategy/s3
  block:
    - name: strategy/s3 > Create tmp dir
      tempfile:
        state: directory
        suffix: manala_deploy
      register: deploy_tmp

    - name: strategy/s3 > Get S3 archive
      aws_s3:
        bucket: releases
        object: "{{ manala_deploy_strategy_include_options.s3_object }}"
        dest: "{{ deploy_tmp.path }}/archive.tar.gz"
        mode: get

    - name: strategy/s3 > Create release dir
      file:
        path: "{{ deploy_helper.new_release_path }}/"
        state: directory

    - name: strategy/s3 > Unarchive
      unarchive:
        src: "{{ deploy_tmp.path }}/archive.tar.gz"
        dest: "{{ deploy_helper.new_release_path }}"
        remote_src: yes
```

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
