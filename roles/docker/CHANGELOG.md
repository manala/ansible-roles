# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

## [2.0.1] - 2019-11-21
### Added
- Handle capabilities option

## [2.0.0] - 2019-11-21
### Removed
- Debian wheezy support

## [1.0.17] - 2019-10-24
### Added
- Debian buster support

## [1.0.16] - 2019-03-19
### Added
- Handle pull option
- Handle privileged option

## [1.0.15] - 2018-11-16
### Fixed
- Keep legacy sysvinit services handling in ansible 2.6+

## [1.0.14] - 2018-11-12
### Added
- Handle containers memory & ulimits options

## [1.0.13] - 2018-10-17
### Fixed
- Python 3 compatibility

## [1.0.12] - 2018-06-29
### Added
- Handle containers entrypoint/command

## [1.0.11] - 2018-06-05
### Added
- Handle dependency packages to install

### Changed
- Replace deprecated uses of "include"
- Pass apt module packages list directly to the `name` option

## [1.0.10] - 2018-02-22
### Added
- Handle containers

## [1.0.9] - 2017-12-06
### Added
- Debian stretch support

## [1.0.8] - 2017-11-09
### Added
- Handle daemon config

### Fixed
- Use the most safe storage-driver (vfs) in tests, to avoid platform dependant issues

## [1.0.7] - 2017-10-28
### Fixed
- Repository key/url and package name

### Changed
- Fix ansible 2.3 warnings "when statements should not include jinja2 templating delimiters"

## [1.0.6] - 2017-06-02
### Added
- manala/openl10n-cli application pattern

## [1.0.5] - 2017-03-16
### Fixed
- Better tty/interative applications handling

## [1.0.4] - 2017-03-15
### Fixed
- manala/security-checker application pattern image

## [1.0.3] - 2017-03-14
### Added
- manala/parallel-lint application pattern

## [1.0.2] - 2017-03-14
### Changed
- Introduce applications environment

## [1.0.1] - 2017-02-23
### Added
- Handle applications
- Handle update

## [1.0.0] - 2016-12-29
### Added
- Install docker
