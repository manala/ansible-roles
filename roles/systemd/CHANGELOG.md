# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
### Added
- Tags for each tasks, with the format `manala_rolename.taskname`

## [1.0.8] - 2019-11-29
### Changed
- Update 'lookup' to use 'query'
- Minimum required version of ansible up to 2.5.0

## [1.0.7] - 2019-10-30
### Fixed
- tmpfiles_configs (task, template and test)

## [1.0.6] - 2019-10-29
### Added
- handle system_configs exclusive
- system_configs tests

### Updated
- tmpfiles_configs exclusive

### Changed
- Tasks order (services is now after system_configs and tmpfiles_configs)

## [1.0.5] - 2019-10-24
### Added
- Debian buster support

## [1.0.4] - 2018-10-17
### Fixed
- Python 3 compatibility

## [1.0.3] - 2018-06-05
### Changed
- Replace deprecated uses of "include"

## [1.0.2] - 2017-12-06
### Added
- Debian stretch support

### Changed
- Skip linting on manual systemctl call in "systemd reload" handler

## [1.0.1] - 2017-08-22
### Changed
- Fix systemd configs task

## [1.0.0] - 2017-07-17
### Added
- Add support for tmpfiles.d (#1)
- Support systemd drop-in files
- Manage systemd services states (mask, disable)
