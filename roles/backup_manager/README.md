# Ansible Role: Backup Manager [![Build Status](https://travis-ci.org/manala/ansible-role-backup_manager.svg?branch=master)](https://travis-ci.org/manala/ansible-role-backup_manager)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of [Backup Manager](https://github.com/sukria/Backup-Manager).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

This role is made to work with the __manala__ backup-manager debian package, available on the __manala__ debian repository. Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.

```yaml
manala_apt_preferences:
 - backup-manager@manala
```

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.backup_manager
```

Using ansible galaxy requirements file:

```yaml
- src: manala.backup_manager
```

## Role Variables

| Name                                             | Default                    | Type    | Description                            |
| ------------------------------------------------ | -------------------------- | ------- | -------------------------------------- |
| `manala_backup_manager_install_packages`         | ~                          | Array   | Dependency packages to install         |
| `manala_backup_manager_install_packages_default` | ['backup-manager']         | Array   | Default dependency packages to install |
| `manala_backup_manager_configs_exclusive`        | false                      | Boolean | Configs exclusivity                    |
| `manala_backup_manager_configs_dir`              | '/etc/backup-manager.d'    | String  | Configs directory path                 |
| `manala_backup_manager_configs_template`         | ~                          | String  | Configs template path                  |
| `manala_backup_manager_configs`                  | []                         | Array   | Collection of configs                  |
| `manala_backup_manager_bin`                      | '/usr/sbin/backup-manager' | String  | Binary path                            |

### Backup manager variable

#### Local Storage

To setup where and how store backups

| Name                   | Value                         | Type    | Description                          |
| ---------------------  | ----------------------------- | ------- | ------------------------------------ |
| `BM_REPOSITORY_ROOT`   | '/srv/backup'                 | String  | Path where local backups are stored  |
| `BM_REPOSITORY_CHMOD`  | 755                           | Octal   | Backup directory mode                |
| `BM_ARCHIVE_TTL'       | 5                             | Integer | Number of backup to keep             |
| `BM_ARCHIVE_METHOD`    | 'tarball tarball-incremental' | String  | How backups are stored (you can mix) |
| `BM_ARCHIVE_CHMOD`     | 644                           | Octal   | Backup files mode                    |
| `BM_ARCHIVE_PREFIX`    | 'backup_'                     | String  | Prefix of the backup files           |
| `BM_ARCHIVE_PURGEDUPS` | true                          | Boolean | Allow to delete old backups          |

#### Backup directories

To setup directories to backup

| Name                     | Value                    | Type   | Description                             |
| ------------------------ | ------------------------ | ------ | --------------------------------------- |
| `BM_TARBALL_DIRECTORIES` | '/srv/app/uploads'       | String | Directories path to backup              |
| `BM_TARBALL_BLACKLIST`   | '/srv/app/uploads/cache' | String | Directories path to exclude from backup |

#### Backup transfer

Setup remote backup (i.e. ftp)

| Name                        | Value            | Type    | Description                          |
| --------------------------- | ---------------- | ------- | ------------------------------------ |
| `BM_UPLOAD_METHOD`          | 'ftp'            | String  | Upload method                        |
| `BM_UPLOAD_FTP_USER`        | 'admin'          | String  | FTP username                         |
| `BM_UPLOAD_FTP_PASSWORD`    | 'azerty'         | String  | FTP password                         |
| `BM_UPLOAD_FTP_HOSTS`       | 'ftp.backup.com' | String  | FTP hosts                            |
| `BM_UPLOAD_FTP_PURGE`       | true             | Boolean | Clear remote directory before upload |
| `BM_UPLOAD_FTP_DESTINATION` | '/backup'        | String  | Remote directory path                |

#### Incremental Archives

Setup incremental archives where BM_ARCHIVE_METHOD = tarball-incremental

| Name                            | Value             | Type    | Description               |
| ------------------------------- | ----------------- | ------- | ------------------------- |
| `BM_TARBALLINC_MASTERDATETYPE`  | 'weekly, monthy'  | String  | Complete backup frequency |
| `BM_TARBALLINC_MASTERDATEVALUE` | 3                 | Integer | Complete backup day       |
| `BM_TARBALL_FILETYPE`           | 'tar.gz'          | String  | Tarball file type         |

#### MySQL backup

Setup MySQL backup

| Name                  | Value                                         | Type    | Description                     |
| --------------------- | --------------------------------------------- | ------- | ------------------------------- |
| `BM_MYSQL_ADMINLOGIN` | 'admin'                                       | String  | MySQL login                     |
| `BM_MYSQL_ADMINPASS`  | 'azerty'                                      | String  | MySQL password                  |
| `BM_MYSQL_HOST`       | 'localhost'                                   | String  | MySQL host                      |
| `BM_MYSQL_PORT`       | 3600                                          | Integer | MySQL port                      |
| `BM_MYSQL_DATABASES`  | 'foobar ALL'                                  | String  | Database to backup              |
| `BM_MYSQL_DBEXCLUDE`  | 'information_schema mysql performance_schema' | String  | Database to exclude from backup |
| `BM_MYSQL_FILETYPE`   | 'bzip2'                                       | String  | Backup compression method       |


#### Hooks

Execute hooks before and after backup

| Name                     | Value                                       | Type   | Description                      |
| ------------------------ | ------------------------------------------- | ------ | -------------------------------- |
| `BM_PRE_BACKUP_COMMAND`  |                                             | String | Command to execute before backup |
| `BM_POST_BACKUP_COMMAND` |                                             | String | Command to execute after backup  |

### MySQL backup example

```yaml
manala_backup_manager_configs:
  - file:     mysql.conf
    template: configs/mysql.j2
    config:
      - BM_REPOSITORY_CHMOD: 775
      - BM_ARCHIVE_CHMOD:    664

      - BM_REPOSITORY_ROOT:  /srv/backup/mysql
      - BM_ARCHIVE_TTL:      5
      - BM_ARCHIVE_PREFIX:   backup

      - BM_MYSQL_ADMINLOGIN: root
      - BM_MYSQL_ADMINPASS:  ~
      - BM_MYSQL_HOST:       localhost
      - BM_MYSQL_DBEXCLUDE:  information_schema mysql performance_schema
```

### Files backup example

```yaml
manala_backup_manager_configs:
  - file:    uploads.conf
    template: configs/default.j2
    config:
      - BM_REPOSITORY_CHMOD:           775
      - BM_ARCHIVE_CHMOD:              664

      - BM_REPOSITORY_ROOT:            /srv/backup/uploads
      - BM_ARCHIVE_TTL:                5
      - BM_ARCHIVE_PURGEDUPS:          true
      - BM_ARCHIVE_METHOD:             tarball-incremental

      - BM_TARBALLINC_MASTERDATETYPE:  weekly
      - BM_TARBALLINC_MASTERDATEVALUE: 1

      - BM_TARBALL_FILETYPE:           tar.gz
      - BM_TARBALL_DIRECTORIES:        /srv/app/web/uploads
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.backup_manager }
```

## CRON

Enable CRON with [manala/ansible-role-cron](https://github.com/manala/ansible-role-cron) :

```yaml
manala_cron_files:
  - file: backup-manager
    user: root
    jobs:
      - name:   backup-manager
        job:    for file in {{ manala_backup_manager_configs_dir }}/*.conf; do {{ manala_backup_manager_bin }} --conffile $file; done
        minute: 25
        hour:   6
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
