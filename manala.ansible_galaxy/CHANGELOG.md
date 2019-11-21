# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

## [2.0.0] - 2019-11-21
### Removed
- Debian wheezy support

## [1.0.6] - 2019-10-24
### Added
- Debian buster support

## [1.0.5] - 2019-05-21
### Fixed
- Alt galaxy bin variable handling when requirement check is unsuccessful
- Disable changed status when writing temporary roles requirements file in check mode

## [1.0.4] - 2018-10-17
### Fixed
- Python 3 compatibility

### Changed
- Ignore SSL certificate validation errors on debian wheezy when using
  official ansible galaxy bin (incompatible default python version)

## [1.0.3] - 2018-06-05
### Changed
- Replace deprecated jinja tests used as filters
- Replace deprecated uses of "include"

## [1.0.2] - 2017-12-06
### Added
- Debian stretch support

## [1.0.1] - 2017-11-10
### Added
- Clean temporary roles requirements file

## [1.0.0] - 2017-06-21
### Added
- Handle alternatives
- Handle roles
