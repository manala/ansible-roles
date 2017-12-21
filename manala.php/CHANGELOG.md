# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
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
