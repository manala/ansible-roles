# Ansible Role: Backup Manager

This role will deal with the setup of [Backup Manager](https://github.com/sukria/Backup-Manager).

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

This role is made to work with the backup-manager debian package. Please use the [**manala.roles.apt**](../apt/) role to handle it properly.

```yaml
manala_apt_preferences:
  - backup-manager@manala
```

## Dependencies

None.

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

#### Local Storage

To setup where and how store backups

| Name                   | Value                         | Type    | Description                          |
| ---------------------  | ----------------------------- | ------- | ------------------------------------ |
| `BM_REPOSITORY_ROOT`   | '/srv/backup'                 | String  | Path where local backups are stored  |
| `BM_REPOSITORY_CHMOD`  | 755                           | Octal   | Backup directory mode                |
| `BM_ARCHIVE_TTL`       | 5                             | Integer | Number of backup to keep             |
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

### Configs

`manala_backup_manager_configs` allows you to define backup manager configuration files using template and config, or raw content.

A state (present|absent|ignore) can be provided.

A default template can be provided

```yaml
manala_backup_manager_configs_defaults:
  template: configs/debian/backup-manager.conf.j2
```

```yaml
manala_backup_manager_configs:
  - file: foo.conf
    config:
      BM_REPOSITORY_CHMOD: 775
      BM_ARCHIVE_CHMOD: 664
      BM_REPOSITORY_ROOT: /srv/backup/mysql
      # Flatten configs
      BM_TARBALL_DIRECTORIES:
        - foo
        - bar
        - "{{ my_custom_configs_array }}"
  # Raw content
  - file: content.conf
    content: |
      # Where to store the archives
      export BM_REPOSITORY_ROOT="/var/archives"
      # Where to place temporary files
      export BM_TEMP_DIR="/tmp"
  # Template based
  - file: template.conf
    template: my/backup_manager.conf.j2
    config:
      foo: bar
  # Ensure config is absent
  - file: absent.conf
    state: absent # "present" by default
  # Ignore config
  - file: ignore.conf
    state: ignore
  # Flatten configs
  - "{{ my_custom_configs_array }}"
```

`manala_backup_manager_configs_exclusive` allow you to clean up existing backup manager configuration files into directory defined by the `manala_backup_manager_configs_dir` key. Made to be sure no old or manually created files will alter current configuration.

```yaml
manala_backup_manager_configs_exclusive: true
```

### Files backup example

```yaml
manala_backup_manager_configs:
  - file: uploads.conf
    config:
      BM_REPOSITORY_CHMOD: 775
      BM_ARCHIVE_CHMOD: 664

      BM_REPOSITORY_ROOT: /srv/backup/uploads
      BM_ARCHIVE_TTL: 5
      BM_ARCHIVE_PURGEDUPS: true
      BM_ARCHIVE_METHOD: tarball-incremental

      BM_TARBALLINC_MASTERDATETYPE: weekly
      BM_TARBALLINC_MASTERDATEVALUE: 1

      BM_TARBALL_FILETYPE: tar.gz
      BM_TARBALL_DIRECTORIES: /srv/app/web/uploads
```

## Example playbook

```yaml
- hosts: servers
  tasks:
    - ansible.builtin.import_role:  
        name: manala.roles.backup_manager
```

## CRON

Enable CRON with [manala/ansible-role-cron](https://github.com/manala/ansible-role-cron) :

```yaml
manala_cron_files:
  - file: backup-manager
    user: root
    jobs:
      - name: backup-manager
        job: for file in {{ manala_backup_manager_configs_dir }}/*.conf; do {{ manala_backup_manager_bin }} --conffile $file; done
        minute: 25
        hour: 6
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
