# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
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
