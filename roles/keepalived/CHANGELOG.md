# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
### Removed
- Useless `manala_environment_parameters` filter

### Added
- Handle string comments in `manala_environment` filter

## [1.0.9] - 2020-12-09
### Changed
- Don't try to create environment file dir

## [1.0.8] - 2020-12-04
### Added
- Handle required parameters keys in environment filters

## [1.0.7] - 2020-12-02
### Added
- Environment filters
- Deprecate dict's array environment
- Deprecate dict's array config

## [1.0.6] - 2020-08-26
### Changed
- Explicit file permissions

## [1.0.5] - 2020-02-13
### Added
- Tags for each tasks, with the format `manala_rolename.taskname`

## [1.0.4] - 2019-10-24
### Added
- Debian buster support

## [1.0.3] - 2018-10-17
### Fixed
- Python 3 compatibility

## [1.0.2] - 2018-06-05
### Added
- Handle dependency packages to install

### Changed
- Replace deprecated uses of "include"
- Pass apt module packages list directly to the `name` option

## [1.0.1] - 2017-12-06
### Added
- Configure keepalived environment file
- Debian stretch support

## [1.0.0] - 2017-06-09
### Added
- Handle installation
- Handle config
- Handle services
