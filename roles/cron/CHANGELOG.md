# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

## [3.0.0] - 2021-01-15
### Changed
- Use unified exclusive template lookup
- Use template ansible module instead of cron ones
- Deprecate job `name` parameter
- Rename job `job` parameter into `command`

### Removed
- Already deprecated dict's array based environment variable handling

## [2.0.3] - 2020-07-09
### Added
- Handle defaults parameters for files

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

## [1.0.5] - 2019-10-24
### Added
- Debian buster support

## [1.0.4] - 2018-10-17
### Fixed
- Python 3 compatibility

## [1.0.3] - 2018-10-12
### Added
- Support environment variables as dict ("env")

### Changed
- Deprecate legacy "environment" parameter

## [1.0.2] - 2018-06-05
### Added
- Handle dependency packages to install

### Changed
- Replace deprecated uses of "include"
- Pass apt module packages list directly to the `name` option

## [1.0.1] - 2017-12-06
### Added
- Debian stretch support

## [1.0.0] - 2017-06-21
### Added
- Handle installation
- Handle files
- Handle services
