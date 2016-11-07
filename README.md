# Ansible Role: Backup Manager

This role will deal with the setup of [backup-manager](https://github.com/sukria/Backup-Manager).

It's part of the Manala <a href="http://www.manala.io" target="_blank">Ansible stack</a> but can be used as a stand alone component.


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
ansible-galaxy install manala.backup-manager
```

Using ansible galaxy requirements file:

```yaml
- src: manala.backup-manager
```

## Role Variables

| Name                                | Default                      | Type   | Description          |
| ----------------------------------- | ---------------------------- | ------ | -------------------- |


### Backup manager variable

#### Local Storage

To setup where and how store backups

| Name                              | Value                        | Type   | Description                          |
| --------------------------------- | ---------------------------- | ------ | ------------------------------------ |
| BM_REPOSITORY_ROOT                | /srv/backup                  | Path   | Path where local backups are stored  |
| BM_REPOSITORY_CHMOD               | 755                          | octal  | Backup directory mode                |
| BM_ARCHIVE_TTL                    | 5                            | int    | Number of backup to keep             |
| BM_ARCHIVE_METHOD                 | tarball tarball-incremental  | string | How backups are stored (you can mix) |
| BM_ARCHIVE_CHMOD                  | 644                          | octal  | Backup files mode                    |
| BM_ARCHIVE_PREFIX                 | backup_                      | string | Prefix of the backup files           |
| BM_ARCHIVE_PURGEDUPS              | true                         | bool   | Allow to delete old backups          |

#### Backup directories

To setup directories to backup

| Name                              | Value                        | Type   | Description                          |
| --------------------------------- | ---------------------------- | ------ | ------------------------------------ |
| BM_TARBALL_DIRECTORIES            | /srv/app/uploads             | path   | Directories to backup                |
| BM_TARBALL_BLACKLIST              | /srv/app/uploads/cache       | path   | Directories to exclude from backup   |

#### Backup transfer

Setup remote backup (i.e. ftp)

| Name                              | Value                        | Type   | Description                           |
| --------------------------------- | ---------------------------- | ------ | ------------------------------------- |
| BM_UPLOAD_METHOD                  | ftp                          | string | Upload method                         |
| BM_UPLOAD_FTP_USER                | admin                        | string | FTP username                          |
| BM_UPLOAD_FTP_PASSWORD            | azerty                       | string | FTP password                          |
| BM_UPLOAD_FTP_HOSTS               | ftp.backup.com               | string | FTP hosts                             |
| BM_UPLOAD_FTP_PURGE               | true                         | bool   | Clear remote directory before upload  |
| BM_UPLOAD_FTP_DESTINATION         | /backup                      | path   | Remote directory                      |

#### Incremental Archives

Setup incremental archives where BM_ARCHIVE_METHOD = tarball-incremental

| BM_TARBALLINC_MASTERDATETYPE      | weekly, monthy           | string | Complete backup frequency             |
| --------------------------------- | ------------------------ | ------ | ------------------------------------- |
| BM_TARBALLINC_MASTERDATEVALUE     | 3                        | int    | Complete backup day                   |
| BM_TARBALL_FILETYPE               | tar.gz                   | string | Tarball file type                     |

#### MySQL backup

Setup MySQL backup

| Name                      | Value                                       | Type   | Description                     |
| ------------------------- | ------------------------------------------- | ------ | ------------------------------- |
| BM_MYSQL_ADMINLOGIN       | admin                                       | string | MySQL login                     |
| BM_MYSQL_ADMINPASS        | azerty                                      | string | MySQL password                  |
| BM_MYSQL_HOST             | localhost                                   | string | MySQL host                      |
| BM_MYSQL_PORT             | 3600                                        | int    | MySQL port                      |
| BM_MYSQL_DATABASES        | foobar ALL                                  | string | Database to backup              |
| BM_MYSQL_DBEXCLUDE        | information_schema mysql performance_schema | string | Database to exclude from backup |
| BM_MYSQL_FILETYPE         | bzip2                                       | string | Backup compression method       |


#### Hooks

Execute hooks before and after backup

| Name                      | Value                                       | Type   | Description                      |
| ------------------------- | ------------------------------------------- | ------ | -------------------------------- |
| BM_PRE_BACKUP_COMMAND     |                                             | string | Command to execute before backup |
| BM_POST_BACKUP_COMMAND    |                                             | string | Command to execute after backup  |

### MySQL backup example

```yaml
elao_backup_manager_configs:
  - file:     mysql.conf
    template: configs/mysql.conf.j2
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
elao_backup_manager_configs:
  - file:    uploads.conf
    template: configs/base.conf.j2
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
    - { role: manala.backup-manager }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
