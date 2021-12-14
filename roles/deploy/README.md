# Ansible Role: Deploy

This role will deal with __Deployment__.

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2.9+

Using ansible galaxy cli:

```bash
ansible-galaxy collection install manala.roles
```

Using ansible galaxy requirements file:

```yaml
collections:

  - manala.roles
```

In case of unavailability of ansible-galaxy, we host a tar.gz of every version of our collection on github:
  - Check latest version available [here](https://github.com/manala/ansible-roles/releases)
  - Use your prefered method:

    - cli:
    ```bash
    ansible-galaxy collection install https://github.com/manala/ansible-roles/releases/download/$VERSION/manala-roles-$VERSION.tar.gz
    ```

    - requirements.yaml:
    ```yaml
    collections:

      - name: https://github.com/manala/ansible-roles/releases/download/$VERSION/manala-roles-$VERSION.tar.gz
        type: url
    ```

See [Ansible Using collections](https://docs.ansible.com/ansible/devel/user_guide/collections_using.html) for more details.

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
  tasks:
    - import_role:  
        name: manala.roles.deploy
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
