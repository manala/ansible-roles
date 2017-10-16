# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
### Added
- Backports sloppy support
- Elasticsearch 5 support

### Fixed
- Elasticsearch repositories patterns source urls
- Elasticsearch keys patterns urls

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
