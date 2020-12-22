# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

## [2.0.7] - 2020-12-22
### Added
- Config content support
- Config dict support
- Flatten users array

### Changed
- Deprecate environment oriented templates
- Deprecate dict's array configs

## [2.0.6] - 2020-10-14
### Fixed
- Explicitly enable service

## [2.0.5] - 2020-10-08
### Added
- Mongodb 4.4 support

## [2.0.4] - 2020-10-07
### Added
- Role can manage MongoDB users

## [2.0.3] - 2020-08-28
### Changed
- Explicit file permissions

## [2.0.2] - 2020-02-13
### Added
- Tags for each tasks, with the format `manala_rolename.taskname`

## [2.0.1] - 2019-11-26
### Added
- Debian buster support

## [2.0.0] - 2019-11-21
### Removed
- Debian wheezy support

## [1.0.4] - 2018-10-17
### Fixed
- Python 3 compatibility

## [1.0.3] - 2018-06-05
### Added
- Handle dependency packages to install

### Changed
- Replace deprecated uses of "include"
- Pass apt module packages list directly to the `name` option

## [1.0.2] - 2017-12-06
### Added
- Debian stretch support

## [1.0.1] - 2017-10-17
### Fixed
- Repository apt key in tests

## [1.0.0] - 2017-06-09
### Added
- Handle installation
- Handle config
- Handle services
