# Ansible Role: Deploy

This role will deal with __Deployment__.

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

None.

## Dependencies

None.

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

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
      ansible.builtin.tempfile:
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
      ansible.builtin.file:
        path: "{{ deploy_helper.new_release_path }}/"
        state: directory

    - name: strategy/s3 > Unarchive
      ansible.builtin.unarchive:
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
  tasks:
    - ansible.builtin.import_role:  
        name: manala.roles.deploy
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
