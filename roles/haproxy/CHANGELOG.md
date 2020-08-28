# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

## [1.0.8] - 2020-08-28
### Changed
- Explicit file permissions

## [1.0.7] - 2020-02-13
### Added
- Tags for each tasks, with the format `manala_rolename.taskname`

## [1.0.6] - 2019-11-29
### Changed
- Update 'lookup' to use 'query'
- Minimum required version of ansible up to 2.5.0

### Added
- Handle configs raw content

## [1.0.5] - 2019-10-24
### Added
- Debian buster support

## [1.0.4] - 2019-03-19
### Added
- Allow to split configuration files

### Removed
- Remove Debian Wheezy support

## [1.0.3] - 2018-06-05
### Added
- Handle dependency packages to install

### Changed
- Replace deprecated uses of "include"
- Pass apt module packages list directly to the `name` option

## [1.0.2] - 2018-03-28
### Changed
- Replace handlers "haproxy restart"/"do haproxy restart" by a single "haproxy reload",
  as reloading takes natively and seamlessly care of configuration validation

## [1.0.1] - 2017-12-06
### Added
- Debian stretch support

## [1.0.0] - 2017-06-21
### Added
- Handle installation
- Handle error files
- Handle config
- Handle services
