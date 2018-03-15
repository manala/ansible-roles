# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
### Added
- Handle options
- Handle dynamic zones records
- Configs/Zones now supports raw `content` parameter in addition of `template`
- Configs/Zones now supports `state` parameter (present|absent)
- Configs/Zones now supports `omit` parameter (false|true)
- Zones now supports `zone` parameter (serves among other things to generate `file` parameter)
- `manala_bind_zone_file` filter to standardize zone file names 

### Changed
- Default zones dir set to `/var/cache/bind`
- Zones directory owner is now set to `root`
- Zones files owner is now set to `{{ manala_bind_user }}`

### Removed
- Zones directory is not created anymore
- Reload handler

## [1.0.1] - 2017-12-06
### Added
- Debian stretch support

## [1.0.0] - 2017-06-21
### Added
- Handle installation
- Handle logs
- Handle configs
- Handle zones
- Handle services
