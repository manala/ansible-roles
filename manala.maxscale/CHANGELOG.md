# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

## [1.0.5] - 2019-10-24
### Added
- Debian buster support
- MaxScale 2.3 support for Debian jessie, stretch and buster

## [1.0.4] - 2018-11-16
### Fixed
- Keep legacy sysvinit services handling in ansible 2.6+

## [1.0.3] - 2018-10-17
### Fixed
- Python 3 compatibility

## [1.0.2] - 2018-06-05
### Added
- Handle dependency packages to install
- Test version 2.2.6
- Handle config boolean parameters
- Handle configs (starting from MaxScale 2.1)
- Handle network users file as json (MaxScale 2.2+)

### Changed
- Replace deprecated uses of "include"
- Pass apt module packages list directly to the `name` option

### Removed
- Environment opinionated default config template

## [1.0.1] - 2017-12-06
### Added
- Debian stretch support

## [1.0.0] - 2017-06-09
### Added
- Handle installation
- Handle config
- Handle services
- Handle users
