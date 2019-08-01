# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
### Added
- Debian buster support

## [1.0.4] - 2018-10-17
### Fixed
- Python 3 compatibility

## [1.0.3] - 2018-06-05
### Changed
- Replace deprecated uses of "include"

## [1.0.2] - 2017-12-06
### Added
- Debian stretch support

### Changed
- Skip linting on manual systemctl call in "systemd reload" handler

## [1.0.1] - 2017-08-22
### Changed
- Fix systemd configs task

## [1.0.0] - 2017-07-17
### Added
- Add support for tmpfiles.d (#1)
- Support systemd drop-in files
- Manage systemd services states (mask, disable)
