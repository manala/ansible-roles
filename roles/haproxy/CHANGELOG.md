# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

## [1.0.5] - 2019-10-24
### Added
- Debian buster support

## [1.0.4] - 2019-03-19
### Added
- Allow to split configuration files

### Removed
- Remove Debian Wheezy support

## [1.0.3] - 2018-06-05
### Added
- Handle dependency packages to install

### Changed
- Replace deprecated uses of "include"
- Pass apt module packages list directly to the `name` option

## [1.0.2] - 2018-03-28
### Changed
- Replace handlers "haproxy restart"/"do haproxy restart" by a single "haproxy reload",
  as reloading takes natively and seamlessly care of configuration validation

## [1.0.1] - 2017-12-06
### Added
- Debian stretch support

## [1.0.0] - 2017-06-21
### Added
- Handle installation
- Handle error files
- Handle config
- Handle services
