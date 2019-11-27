# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

## [2.0.0] - 2019-11-21
### Removed
- Debian wheezy support

## [1.0.6] - 2019-10-29
### Fixed
- Cleanup version comparisons

## [1.0.5] - 2019-10-24
### Added
- Debian buster support
- Config template for 6.2

### Fixed
- Config snapshots handling
- Missing version 2.0 config template handling

## [1.0.4] - 2018-11-16
### Fixed
- Keep legacy sysvinit services handling in ansible 2.6+

## [1.0.3] - 2018-10-17
### Fixed
- Python 3 compatibility

## [1.0.2] - 2018-06-05
### Added
- Handle dependency packages to install
- Loop over api calls until its ready

### Changed
- Fix missings ansible 2.1 deprecation "Supplying headers via HEADER_* is deprecated"
- Replace deprecated jinja tests used as filters
- Replace deprecated uses of "include"
- Pass apt module packages list directly to the `name` option

## [1.0.1] - 2017-12-06
### Added
- Debian stretch support

### Changed
- Fix ansible 2.1 deprecation "Supplying headers via HEADER_* is deprecated"

## [1.0.0] - 2016-01-27
### Added
- Install grafana
- Add grafana v2.0, v2.1, v2.5, v3.1, v4.0, v4.1 config templates
- Configure grafana datasources
- Configure grafana dashboards
