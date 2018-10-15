# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
### Fixed
- Python 3 compatibility

## [1.0.6] - 2018-06-05
### Added
- Handle role inclusion

### Changed
- Pass apt module packages list directly to the `name` option
- Replace deprecated uses of "include"

## [1.0.5] - 2017-12-20
### Fixed
- Install composer from https

## [1.0.4] - 2017-12-14
### Fixed
- Only tries to touch non existing shared files

## [1.0.3] - 2017-12-06
### Added
- Debian stretch support

## [1.0.2] - 2017-10-30
### Changed
- Fix ansible 2.3 warnings "when statements should not include jinja2 templating delimiters"

## [1.0.1] - 2017-05-18
### Added
- Unarchive strategy

## [1.0.0] - 2017-05-16
### Added
- Handle setup
- Handle strategies
- Handle unfinished deployments
- Handle shared paths
- Handle copied paths
- Handle writable dirs
- Handle tasks and posts tasks
