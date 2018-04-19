# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
### Added
- Elasticsearch 6 support (become default)

### Changed
- Replace deprecated jinja tests used as filters

### Removed
- Default php sapis (cli & fpm) as they are now handled by the manala.php role itself

## [1.0.13] - 2018-02-06
### Removed
- Debian wheezy support for "exa" and "thefuck" packages

## [1.0.12] - 2018-01-23
### Fixed
- Increase "max_input_vars" in php admin pool (phpmyadmin is a bit greedy when
  a mysql table has many fields)

## [1.0.11] - 2018-01-15
### Fixed
- Force phantomjs debian package from manala repository (even if available on
  debian jessie-backports and stretch, upstream version is not statically linked
  and suffers from limitations)

## [1.0.10] - 2017-12-18
### Fixed
- Drop global low priority sury apt preferences for php (this was taken from dotdeb repository policy, but became irrelevant for sury)

## [1.0.9] - 2017-12-08
### Added
- PHP 7.2 support

## [1.0.8] - 2017-12-06
### Added
- Debian stretch support

### Changed
- Style default 404 pages

## [1.0.7] - 2017-11-06
### Added
- Nodejs 9 (and future) support

## [1.0.6] - 2017-10-17
### Added
- Exa package from manala by default
- Elasticsearch 5 support (become default) (elasticsearch-head plugin not supported)
- Java version 8 (backports) for debian jessie

## [1.0.5] - 2017-10-09
### Added
- Nodejs 8 support

## [1.0.4] - 2017-09-08
### Added
- Respect thefuck dependencies (python-pathlib2 is available on wheezy via manala,
  and on jessie via backports, python-pkg-resources is already available in a poor version on wheezy, and in a decent version on jessie via backports)

## [1.0.3] - 2017-09-06
### Changed
- Limit httpie installation on jessie

### Added
- Respect httpie dependencies (python3-requests >= 2.5.2, python3-urllib3 >= 1.16, available on backports)

## [1.0.2] - 2017-06-14
### Added
- Force npm update to false to avoid unwanted npm package updates

## [1.0.1] - 2017-05-12
### Added
- `httpie` package preference & pattern

## [1.0.0] - 2017-05-11
### Added
- Handle skeleton patterns & options
