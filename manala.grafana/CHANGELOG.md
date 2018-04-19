# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
### Added
- Handle dependency packages to install

### Changed
- Fix missings ansible 2.1 deprecation "Supplying headers via HEADER_* is deprecated"
- Replace deprecated jinja tests used as filters
- Replace deprecated uses of "include"

## [1.0.1] - 2017-12-06
### Added
- Debian stretch support

### Changed
- Fix ansible 2.1 deprecation "Supplying headers via HEADER_* is deprecated"

## [1.0.0] - 2016-01-27
### Added
- Install grafana
- Add grafana v2.0, v2.1, v2.5, v3.1, v4.0, v4.1 config templates
- Configure grafana datasources
- Configure grafana dashboards
