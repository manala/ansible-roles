# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
### Added
- Debian stretch support
- Explicit gnupg dependency as its not provided by default on debian stretch

### Changed
- Adjust tests for debian stretch support

## [1.0.11] - 2017-11-06
### Added
- Nodejs 9 support

## [1.0.10] - 2017-11-02
### Fixed
- Galera debian repositories

## [1.0.9] - 2017-10-28
### Fixed
- Docker repository key/url

## [1.0.8] - 2017-10-24
### Changed
- Pam Ssh Agent Auth preferences pattern

## [1.0.7] - 2017-10-20
### Fixed
- Debian httpredir.debian.org deprecated in favour of deb.debian.org
- Debian security repository trailing slash

## [1.0.6] - 2017-10-17
### Added
- Backports sloppy support
- Elasticsearch 5 support

### Fixed
- Elasticsearch repositories patterns source urls
- Elasticsearch keys patterns urls

### Fixed
- Mongodb repository apt key

## [1.0.5] - 2017-10-09
### Added
- Nodejs 8 support

### Changed
- Fix ansible 2.3 warnings "when statements should not include jinja2 templating delimiters"

## [1.0.4] - 2017-09-29
### Changed
- Fix varnish 4.0 repository and key

## [1.0.3] - 2017-09-28
### Changed
- Update yarn apt repository and key url

## [1.0.2] - 2017-09-25
### Changed
- Change testing manual debian package (smaller and more reliable)

## [1.0.1] - 2017-05-12
### Added
- `httpie` package preference

## [1.0.0] - 2017-05-11
### Added
- Handle sources list
- Handle preferences
- Handle repositories keys
- Handle repositories
- Handle update
- Handle packages
