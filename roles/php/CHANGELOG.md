# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
### Changed
- Changed cli memory_limit default config (previous was `-1`). Use a safer 512M default.

## [2.0.5] - 2020-06-19
### Fixed
- Missing configs tags

## [2.0.4] - 2020-06-17
### Added
- Handle configs states (present|absent) & raw content

### Changed
- Cli memory_limit default config is now `-1` in  templates

### Fixed
- Replace deprecated uses of "include"

## [2.0.3] - 2020-02-13
### Added
- Tags for each tasks, with the format `manala_rolename.taskname`

## [2.0.2] - 2020-01-06
### Added
- Handle PHP 7.4 version

## [2.0.1] - 2019-11-29
### Changed
- Update 'lookup' to use 'query'

## [2.0.0] - 2019-11-21
### Removed
- Debian wheezy support (coming along with php 5.4/5.5)

## [1.0.15] - 2019-10-29
### Fixed
- Cleanup version comparisons

## [1.0.14] - 2019-10-24
### Added
- Debian buster support

## [1.0.13] - 2019-01-25
### Added
- Add Drush support as PHP application

## [1.0.12] - 2018-12-13
### Fixed
- Missing tags in configs tasks

### Added
- Handle PHP 7.3 version

## [1.0.11] - 2018-10-17
### Fixed
- Python 3 compatibility

## [1.0.10] - 2018-09-12
### Fixed
- Empty environment variables (`""`) raise errors as well as null ones (See: https://github.com/php/php-src/blob/PHP-7.2.9/sapi/fpm/fpm/fpm_conf.c#L1447)

## [1.0.9] - 2018-06-05
### Changed
- Replace deprecated jinja tests used as filters
- Pass apt module packages list directly to the `name` option

### Fixed
- Give opportunity to specify certificates validation on application download

## [1.0.8] - 2018-03-28
### Changed
- Provide "cli" and "fpm" as default sapis

## [1.0.7] - 2018-01-23
### Fixed
- Quote pool environment variables and restrict allowed types

### Changed
- Pass 'env' variables on a per-pool basis
- Alphabetically sort pools 'env' variables

### Added
- "apc.enable_cli" config options set as true by default

## [1.0.6] - 2017-12-21
### Added
- Allow to pass 'env' variables to php pools

## [1.0.5] - 2017-12-08
### Added
- Handle PHP 7.2 version
  * Remove deprecated "track_errors" config option
  * Add new "request_slowlog_trace_depth" fpm pool option
  * Add "sodium" embedded extension
  * Add "ds", "mongo", "sass" pecl or like extensions

## [1.0.4] - 2017-12-06
### Added
- Debian stretch support
- Introduce "manala_php_extensions_pecl_versioned" variable

## [1.0.3] - 2017-10-30
### Changed
- Fix ansible 2.3 warnings "when statements should not include jinja2 templating delimiters"

## [1.0.2] - 2017-06-30
### Added
- Add stretch to debian distributions allowed to install php 7 or php 7.1

## [1.0.1] - 2017-05-10
### Added
- Handle php version 5.6 on debian jessie using sury php repository

## [1.0.0] - 2017-05-10
### Added
- Install packages
- Handle extensions
- Handle configs
- Handle fpm pools
- Setup blackfire
- Handle services
- Handle applications
