# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

## [2.0.3] - 2021-01-15
### Added
- Dict based config filters
- Flatten repositories array
- `ignore` repository state

# Changed
- Deprecate dict's array config

## [2.0.2] - 2020-08-28
### Changed
- Explicit file permissions

## [2.0.1] - 2020-02-13
### Added
- Tags for each tasks, with the format `manala_rolename.taskname`

## [2.0.0] - 2019-11-21
### Removed
- Debian wheezy support

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
- Debian stretch support
- Import pre-generated gpg key instead of generate it in tests

## [1.0.0] - 2017-06-21
### Added
- Handle installation
- Handle config
- Handle repositories
