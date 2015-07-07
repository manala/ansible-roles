<img src="http://www.elao.com/images/corpo/logo_red_small.png"/>

# Ansible Role: cron

This role will assume the setup of cron

It's part of the ELAO [Ansible stack](http://ansible.elao.com) but can be used as a stand alone component.

## Requirements

- Ansible 1.7.2+

## Dependencies

None.

## Installation

Using ansible galaxy:

```bash
ansible-galaxy install elao.cron
```
You can add this role as a dependency for other roles by adding the role to the meta/main.yml file of your own role:

```yaml
dependencies:
  - { role: elao.cron }
```

## Role Handlers

| Name         | Type     | Description           |
| ------------ | -------- | --------------------- |
| cron restart | Service  |  Restart cron service |

## Role Variables

| Name                     | Default | Type   | Description                                                                     |
| ------------------------ | ------- | ------ | ------------------------------------------------------------------------------- |
| elao_cron_jobs.name      |         | string | Description of crontab entry. Must be unique.                                   |
| elao_cron_jobs.job       |         | string | The command to execute. Required if state=present                               |
| elao_cron_jobs.minute    | *       | string | Minute when the job should run (0-59, *, */2, etc)                              |
| elao_cron_jobs.hour      | *       | string | Hour when the job should run (0-23, *, */2, etc)                                |
| elao_cron_jobs.day       | *       | string | Day of the month the job should run (1-31, *, */2, etc)                         |
| elao_cron_jobs.month     | *       | string | Month of the year the job should run (1-12, *, */2, etc)                        |
| elao_cron_jobs.weekday   | *       | string | Day of the week that the job should run (0-6 for Sunday-Saturday, *, etc)       |
| elao_cron_jobs.cron_file |         | string | If specified, uses this file in cron.d instead of an individual user's crontab. |
| elao_cron_jobs.user      | root    | string | The specific user whose crontab should be modified.                             |
| elao_cron_jobs.state     | present | string | Whether to ensure the job is present or absent.                                 |

### Configuration example

```yaml
elao_cron_jobs:
  # Ensure a job that runs at 2 and 5 exists.
  # Creates an entry like "0 5,2 * * ls -alh > /dev/null"
  - name: check dirs
    minute: 0
    hour: 5,2
    job: "ls -alh > /dev/null"
  # Ensure an old job is no longer present. Removes any job that is prefixed
  # by "#Ansible: an old job" from the crontab
  - name: an old job"
    state: absent
```

## Example playbook

    - hosts: servers
      roles:
         - { role: elao.cron }

# Licence

MIT

# Author information

ELAO [**(http://www.elao.com/)**](http://www.elao.com)
