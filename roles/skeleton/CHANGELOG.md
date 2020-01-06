# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

## [2.0.1] - 2020-01-06
### Added
- PHP 7.4 support

### Changed
- Php and nodejs default versions same across distribution releases

## [2.0.0] - 2019-11-23
### Removed
- Debian wheezy support
- Php 5.4/5.5 support
- Php dotdeb support

### Fixed
- Zsh role dependecy order

## [1.0.35] - 2019-10-24
### Added
- Debian buster support
- Nodejs 12 support (became default on debian jessie/stretch/buster)

## [1.0.34] - 2019-09-20
### Added
- Elasticsearch version 7 support

## [1.0.33] - 2019-07-10
### Fixed
- Update dependency roles names

## [1.0.32] - 2019-04-16
### Fixed
- Handle wheezy archive repo

## [1.0.31] - 2019-04-02
### Changed
- Use manala (on wheezy/jessie) or backports (on stretch) supervisor apt preference

## [1.0.30] - 2019-04-01
### Fixed
- Handle jessie archive repo

## [1.0.29] - 2019-02-04
### Changed
- Both allow app passwordless mysql connections from localhost and anywhere

## [1.0.28] - 2019-01-25
# Removed
- Remove default php applications (php-cs-fixer / phpcs / security-checker )

### Changed
- Re-allow mysql connections from anywhere

## [1.0.27] - 2019-01-10
### Fixed
- Fix dotdeb php 5.5/5.6 apt preferences

## [1.0.26] - 2018-12-13
### Added
- PHP 7.3 support

## [1.0.25] - 2018-11-23
### Changed
- Simplify `apt_preferences` mapping by using replace filters instead of fixed versions arrays
- Update default mysql version (5.6 -> 5.7)
- Update default mariadb version (10.1 -> 10.3)

## [1.0.24] - 2018-11-16
### Fixed
- Use updated `python-httplib2` debian package from manala, to work around
  dependency break inroduced by `libssl1.1` `1.1.1-1`

## [1.0.23] - 2018-11-13
### Added
- Wget package

## [1.0.22] - 2018-11-12
# Removed
- Remove docker support
- Remove accounts support (Needed only for docker)
- Remove systemd support (Needed only for docker)

## [1.0.21] - 2018-11-12
# Removed
- Disable docker.socket service handling via systemd, as it's no more reliable
  starting from Docker CE 18.09.0 (See: https://github.com/docker/docker-ce-packaging/pull/257)

## [1.0.20] - 2018-10-12
### Added
- Introduce "env_vars" app options. Such environment variables will be both
  available in zsh and php fpm

## [1.0.19] - 2018-08-21
### Added
- Thumbor default config

## [1.0.18] - 2018-08-14
### Fixed
- A surreptitiously intruded backquote

## [1.0.17] - 2018-08-13
### Added
- Nodejs 10 support (became default on debian jessie/stretch)

## [1.0.16] - 2018-07-05
### Fixed
- Ensure heka & rtail packages are absent

## [1.0.15] - 2018-06-26
### Added
- Thumbor support

### Changed
- Rtail support (deprecated)
- Heka support (deprecated)

## [1.0.14] - 2018-06-05
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
