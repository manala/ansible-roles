# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

## [2.0.3] - 2020-01-22
## Fixed
- User & group state handling

## [2.0.2] - 2020-01-16
## Added
- Enhance state option to handle users keys

## [2.0.1] - 2019-11-29
### Changed
- Update 'lookup' to use 'query'
- Minimum required version of ansible up to 2.5.0

## [2.0.0] - 2019-11-21
### Removed
- Debian wheezy support

## [1.0.5] - 2019-10-29
### Added
- State option to handle users accounts

## [1.0.4] - 2019-10-24
### Added
- Debian buster support

## [1.0.3] - 2018-10-17
### Fixed
- Python 3 compatibility

## [1.0.2] - 2018-06-05
### Changed
- Replace deprecated jinja tests used as filters
- Replace deprecated uses of "include"

## [1.0.1] - 2017-12-06
### Added
- Debian stretch support

### Changed
- Tests on default user shell have been removed according to a debian stretch bug,
  where default user shell is empty (see: https://github.com/manala/ansible-roles/issues/63)

## [1.0.0] - 2017-05-12
### Added
- Handle groups
- Handle users
