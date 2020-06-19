# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

## [2.0.3] - 2020-06-19
### Removed
- Redundant HTTPS fastcgi parameter

## [2.0.2] - 2020-02-13
### Added
- Tags for each tasks, with the format `manala_rolename.taskname`

## [2.0.1] - 2019-11-29
### Changed
- Update 'lookup' to use 'query'
- Minimum required version of ansible up to 2.5.0

## [2.0.0] - 2019-11-21
### Removed
- Debian wheezy support

### Changed
- Update Magento 2 default configuration

### Added
- Handle configs states (present|absent) & raw content

## [1.0.9] - 2019-10-24
### Added
- Debian buster support

## [1.0.8] - 2019-04-16
### Added
- Add prestashop 1.7 template
- Handle modules

## [1.0.7] - 2019-01-25
### Added
- Add list of trusted IPs from Cloudflare and Cloudfront
- Add Drupal 7 default template

## [1.0.6] - 2018-10-31
### Fixed
- Fixed wrong `Feature-Policy` options syntax and set The `Referrer-Policy` header to `strict-origin-when-cross-origin`

### Added
- Add new Magento 2 default configuration file

## [1.0.5] - 2018-10-17
### Fixed
- Python 3 compatibility

## [1.0.4] - 2018-10-12
### Added
- New template to handle default security headers configuration
- New Drupal 8 default template

## [1.0.3] - 2018-06-05
### Added
- Handle dependency packages to install

### Changed
- Replace deprecated uses of "include"
- Pass apt module packages list directly to the `name` option

## [1.0.2] - 2018-03-01
### Changed
- Disable client_max_body_size on ssl offloading dev template

## [1.0.1] - 2017-12-06
### Added
- Debian stretch support

## [1.0.0] - 2017-05-16
### Added
- Handle installation
- Handle configuration(s)
- Handle services
