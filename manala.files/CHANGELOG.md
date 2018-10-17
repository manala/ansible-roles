# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
### Fixed
- Python 3 compatibility

## [1.0.4] - 2018-07-02
### Added
- Handle url unarchiving

## [1.0.3] - 2018-06-05
### Fixed
- Replace link_file "touch" step by a combination of an unforced empty copy and a classic file module. This offers the same behaviour to the linked file, but don't report it as changed each time the role is played

### Changed
- Replace deprecated uses of "include"

## [1.0.2] - 2017-12-06
### Added
- Debian stretch support

## [1.0.1] - 2017-09-25
### Changes
- Fix tests

## [1.0.0] - 2017-05-22
### Added
- Handle attributes
