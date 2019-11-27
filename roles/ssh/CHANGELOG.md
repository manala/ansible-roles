# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

## [1.0.6] - 2019-10-24
### Added
- Debian buster support

## [1.0.5] - 2018-10-17
### Fixed
- Python 3 compatibility

## [1.0.4] - 2018-07-10
### Fixed
- RekeyLimit parameter as default on debian jessie/stretch client config template

## [1.0.3] - 2018-06-05
### Added
- Handle dependency packages to install

### Changed
- Replace deprecated uses of "include"
- Pass apt module packages list directly to the `name` option

## [1.0.2] - 2017-12-06
### Added
- Debian stretch support

## [1.0.1] - 2017-10-07
### Added
- Config sshd tests

### Changed
- Don't redefine already default options in default sshd config templates

### Removed
- Unused testing files

## [1.0.0] - 2017-07-17
### Added
- Handle install
- Handle config
- Handle known hosts
- Handle services
