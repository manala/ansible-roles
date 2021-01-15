# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

## [2.0.10] - 2021-01-15
### Added
- Supports `sql_log_bin` directive on `manala_mysql_users`

## [2.0.9] - 2020-12-17
### Changed
- Switch from `eq` to more widely available `equalto` test

## [2.0.8] - 2020-12-15
### Added
- `ignore` users state
- `ignore` databases state
- Flatten users array
- Flatten databases array
- Config(s) filters

### Changed
- Use unified exclusive template lookup
- Deprecate dict's array config(s)
- Deprecate environment oriented templates

## [2.0.7] - 2020-09-29
### Added
- Supports mariadb 10.5 for debian stretch and buster

## [2.0.6] - 2020-08-26
### Changed
- Explicit file permissions

## [2.0.5] - 2020-06-24
### Changed
- Omit users privileges if not defined

## [2.0.4] - 2020-06-09
### Changed
- Install dependencies based on python version

## [2.0.3] - 2020-03-13
### Added
- Supports mariadb 10.4 for debian jessie, stretch and buster

### Removed
- Remove tests for mariadb 10.0, 10.1 and 10.2 version.

## [2.0.2] - 2020-02-13
### Added
- Tags for each tasks, with the format `manala_rolename.taskname`

## [2.0.1] - 2019-11-29
### Changed
- Update 'lookup' to use 'query'
- Minimum required version of ansible up to 2.5.0

## [2.0.0] - 2019-11-21
### Removed
- Debian wheezy support

### Added
- Handle configs states (present|absent) & raw content

## [1.0.9] - 2019-10-29
### Added
- Supports `append_privs` directive on `manala_mysql_users`

## [1.0.8] - 2019-10-24
### Added
- Debian buster support

## [1.0.7] - 2019-07-11
### Added
- Supports `/etc/my.cnf` configuration with `manala_mysql_config`
- Create mysql data directory

## [1.0.6] - 2018-10-31
### Added
- Supports mariadb 10.3 for debian jessie and stretch

## [1.0.5] - 2018-10-17
### Fixed
- Python 3 compatibility

## [1.0.4] - 2018-06-05
### Added
- Handle default dependency packages to install
- Handle replications

### Changed
- Replace deprecated uses of "include"
- Pass apt module packages list directly to the `name` option

## [1.0.3] - 2018-03-28
### Changed
- Allow passing configs variables as boolean

## [1.0.2] - 2017-12-06
### Added
- Debian stretch support

## [1.0.1] - 2017-11-02
### Fixed
- Galera debian repositories

## [1.0.0] - 2017-05-18
### Added
- Handle installation
- Handle configurations
- Handle services
- Handle databases and users
