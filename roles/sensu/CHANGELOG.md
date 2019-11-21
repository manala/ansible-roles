# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
### Removed
- Debian wheezy support

## [1.0.5] - 2018-11-16
### Fixed
- Keep legacy sysvinit services handling in ansible 2.6+

## [1.0.4] - 2018-10-17
### Fixed
- Python 3 compatibility

## [1.0.3] - 2018-07-10
### Changed
- Default config files user:group and permission are now set to `sensu:sensu` 0644

## [1.0.2] - 2018-06-05
### Added
- Handle dependency packages to install

### Changed
- Replace deprecated uses of "include"
- Pass apt module packages list directly to the `name` option

## [1.0.1] - 2017-12-06
### Added
- Debian stretch support

## [1.0.0] - 2016-01-24
### Added
- Install and configure sensu-server, sensu-client and sensu-api
- Install ruby gems
- Configure sensu checks
