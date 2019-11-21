# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
### Removed
- Debian wheezy support

## [1.0.7] - 2019-10-24
### Added
- Debian buster support

## [1.0.6] - 2018-11-15
### Changed
- Update base config template for ansible 2.6.5

## [1.0.5] - 2018-10-17
### Fixed
- Python 3 compatibility

## [1.0.4] - 2018-06-05
### Added
- Handle dependency packages to install

### Changed
- Update base config template for ansible 2.5.0
- Replace deprecated uses of "include"
- Pass apt module packages list directly to the `name` option

## [1.0.3] - 2018-03-14
### Changed
- Update base config template

## [1.0.2] - 2017-12-06
### Added
- Debian stretch support

## [1.0.1] - 2017-11-09
### Added
- Handle hosts file
- Handle config
- Handle host_vars files
- Handle group_vars files

## [1.0.0] - 2017-05-29
### Added
- Handle installation
