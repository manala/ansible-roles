# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

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
