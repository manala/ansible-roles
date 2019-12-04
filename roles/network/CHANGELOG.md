# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
### Added
- Install ifupdown package

## [2.0.0] - 2019-11-21
### Removed
- Debian wheezy support

## [1.0.7] - 2019-10-24
### Added
- Debian buster support

## [1.0.6] - 2019-09-11
### Added
- Allow to configure interfaces with multiple config files (/etc/network/interfaces.d)

## [1.0.5] - 2018-10-17
### Fixed
- Python 3 compatibility

## [1.0.4] - 2018-08-22
### Changed
- Tabulation based indentation for interfaces

## [1.0.3] - 2018-06-05
### Added
- Handle routing tables

### Changed
- Enhance hosts regex handling

## [1.0.2] - 2017-12-06
### Added
- Debian stretch support

### Changed
- Replace deprecated uses of "include"

## [1.0.1] - 2017-10-04
### Changed
- Use unsafe_writes when updating /etc/hosts to work around some situations
  where /etc/hosts is mounted and atomic writes are impossible (such as docker)

## [1.0.0] - 2017-07-17
### Added
- Handle hosts
- Handle resolver
- Handle interfaces
