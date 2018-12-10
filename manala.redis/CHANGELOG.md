# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

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
