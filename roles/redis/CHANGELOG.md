# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

## [2.0.7] - 2021-03-27
### Fixed
- Fix 3.2 templates

## [2.0.6] - 2021-03-26
### Fixed
- Use absolute path when including sub templates

## [2.0.5] - 2021-02-23
### Fixed
- Fix config filter

## [2.0.4] - 2020-12-22
### Removed
- Version 2.4 support
- Version 3.0 support
- Version 4.0 support

### Added
- Version 3.2 support
- Version 6.0 support (dict config only)
- Config filters

# Changed
- Rename `manala_redis_config*` variables to `manala_redis_server_config*` (providing backward compatibility)
- Guess only MAJOR.MINOR version parts
- Deprecate environment oriented templates
- Deprecate dict's array configs

## [2.0.3] - 2020-08-26
### Changed
- Explicit file permissions

## [2.0.2] - 2020-07-07
### Changed
- More permissive dev config templates

## [2.0.1] - 2020-02-13
### Added
- Tags for each tasks, with the format `manala_rolename.taskname`

## [2.0.0] - 2019-11-21
### Removed
- Debian wheezy support

## [1.0.7] - 2019-10-29
### Fixed
- Cleanup version comparisons

## [1.0.6] - 2019-10-24
### Added
- Debian buster support

## [1.0.5] - 2018-10-31
### Added
- Redis 5.0 support

## [1.0.4] - 2018-10-17
### Fixed
- Python 3 compatibility

## [1.0.3] - 2018-07-19
### Added
- Redis 4.0 support

## [1.0.2] - 2018-06-05
### Added
- Handle dependency packages to install

### Changed
- Replace deprecated jinja tests used as filters
- Replace deprecated uses of "include"
- Pass apt module packages list directly to the `name` option

## [1.0.1] - 2017-12-06
### Added
- Install and configure redis-sentinel (>= 3.0)
- Debian stretch support

## [1.0.0] - 2017-06-09
### Added
- Install redis-server
- Autodetect installed redis version and choose template accordingly
- Add redis 3.0 config templates
- Add redis 2.8 config templates
- Add redis 2.4 config templates
