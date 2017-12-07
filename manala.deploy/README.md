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

## How to

The following steps provide an how to run the deployment of your application.

First of all, you will have to set a `hosts` file with group for the deployment, for example, a typical `ansible/hosts` file:

```
staging ansible_ssh_host=127.0.0.1 ansible_ssh_user=app
prod-1 ansible_ssh_host=127.0.0.1 ansible_ssh_user=app
prod-2 ansible_ssh_host=127.0.0.1 ansible_ssh_user=app

[deploy_staging]
staging

[deploy_prod]
prod-1
prod-2

[deploy_prod_primary]
prod-1

[deploy:children]
deploy_staging
deploy_prod
```
_This file takes the assumption that you have one server for the staging and two servers for the production. It will be able to deployment simultaneously on the two servers at once for the prod servers_

You'll need a `ansible/deploy.yml` file with this content to link your deploy with the _manala.deploy_ role:
```yaml
--

- hosts: deploy
  any_errors_fatal: true
  roles:
    - manala.deploy
  # Optional information, could be useful for mono-repository
  #tags:
  #    - my-tag
  #vars_files:
  #  - "deploy/my-app.{{ app_env }}.yml"
  #tasks:
  #  - include: "tasks/deploy.yml"
```

Create a file `ansible/group_vars/deploy.yml` which will contain the recipe of the deployment process.

```yaml
---

#######
# Dir #
#######

manala_deploy_dir: /var/www/my-manala-project.local/htdocs #The directory to which the deployment will take place on the target server

############
# Releases #
############

manala_deploy_releases: 5 #The number of release you would like to keep on the target server

############
# Strategy #
############

manala_deploy_strategy: git #The deploy strategy
# Other strategy:
#manala_deploy_strategy: synchronize
#manala_deploy_strategy: unarchive


manala_deploy_strategy_git_repo:    git@github.com:vendor/app.git #The git repository
manala_deploy_strategy_git_version: prod #Target branch used

#Other strategy parameters:
#manala_deploy_strategy_synchronize_src: "public/"
#manala_deploy_strategy_synchronize_rsync_options: ~
#manala_deploy_strategy_unarchive_src: "/tmp/build/release/prod/manala.tar.gz"

##########
# Copied #
##########

manala_deploy_copied: #Files copied from previous release
  - vendor
  - node_modules

##########
# Shared #
##########

manala_deploy_shared_files:
  - app/config/parameters.yml

manala_deploy_shared_dirs:
  - var/logs
  - web/uploads


############
# Writable #
############

manala_deploy_writable_dirs_default:
  mode:   ug=rwx,o=rx
  follow: true

manala_deploy_writable_dirs:
  - var/cache
  - var/logs
  - web/uploads
```

This is the global recipe used for the deploy, if you want to personalize the recipe for one of your environment, you will have to create a specific `ansible/group_vars/deploy_prod.yml` file for example, to overwrite or add some more tasks to the recipe:

```yaml
---

############
# Strategy #
############

manala_deploy_strategy_git_version: prod

###########
# Removed #
###########

manala_deploy_removed:
  - web/app_dev.php

#########
# Tasks #
#########

manala_deploy_tasks:
  - make: install@staging
  - make: build@staging
  - make: migration@staging
    when: "'deploy_prod_primary' in group_names"
  - command: sudo /usr/sbin/service php7.1-fpm reload

# The when case is used to run the command only on the server that met the requirements given

```

After that, you are all set, you can run the command to deploy on your staging environment:
```
ansible-playbook ansible/deploy.yml --inventory-file=ansible/hosts --limit=deploy_staging
```

## Extra

This role can be used with two strategies in parallel. A common case could be to create a local release based on a git strategy, and then deploy using the unarchive strategy.

Your `hosts` will then need to have an additional release entry (to the previous deploy one):
```
localhost_demo ansible_connection=local
localhost_prod ansible_connection=local

[release_demo]
localhost_demo

[release_prod]
localhost_prod

[release:children]
release_demo
release_prod
```

You will need the `ansible/release.yml` file with a similar configuration:
```yaml
---
- hosts: release
  any_errors_fatal: true
  roles:
    - manala.deploy
  tasks:
    - name: Release > Remove archive
      file:
        path: /tmp/build/release/prod/current.tar.gz
        state: absent
    - name: Release > Create archive
      shell: "tar zcvf /tmp/build/release/prod/current.tar.gz ."
      args:
        chdir: /tmp/build/release/prod/current
        creates: current.tar.gz
```

And your `ansile/group_vars/deploy_prod.yml` file will describe the strategy that consist of unarchive the created release on the server
```yaml
---

############
# Strategy #
############

manala_deploy_strategy_unarchive_src: "/tmp/build/release/prod/current.tar.gz"

#######
# Dir #
#######

manala_deploy_dir: /srv/app

###########
# Removed #
###########

manala_deploy_removed:
  - web/app_test.php

#########
# Tasks #
#########

manala_deploy_tasks:
  - make: install@demo
  - make: build@demo
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
