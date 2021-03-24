# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

## [3.0.3] - 2021-03-24
### Changed
- Use unified exclusive template lookup
- Deprecate environment oriented templates
- Deprecate dict's array configs

## [3.0.2] - 2020-10-08
### Modified
- Clean jinja "format" usages

## [3.0.1] - 2020-08-26
### Changed
- Explicit file permissions

## [3.0.0] - 2020-07-03
### Added
- Debian buster support

### Changed
- Install from upstream binaries instead of manala debian repository

## [2.0.1] - 2020-02-13
### Added
- Tags for each tasks, with the format `manala_rolename.taskname`

## [2.0.0] - 2019-11-21
### Removed
- Debian wheezy support

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
- Debian stretch support

## [1.0.0] - 2016-12-21
### Added
- Handle installation
- Handle configs
