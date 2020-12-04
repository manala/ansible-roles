# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
### Added
- Handle required parameters keys in config filters

## [2.0.10] - 2020-10-26
### Added
- Flatten configs array

## [2.0.9] - 2020-10-21
### Fixed
- Toml encoder edge cases

## [2.0.8] - 2020-10-21
### Fixed
- Missing dependency in filters

## [2.0.7] - 2020-10-20
### Added
- Config filters
- Ensure config directory exists

### Changed
- Use unified exclusive template lookup
- Deprecate dict's array configs
- Don't touch config if empty or no template defined
- Exclusive mode applied on all files (not only `*.conf`)
- Cleanup `input_docker.conf.j2` configs template

## [2.0.6] - 2020-08-28
### Changed
- Explicit file permissions

## [2.0.5] - 2020-02-13
### Added
- Tags for each tasks, with the format `manala_rolename.taskname`

## [2.0.4] - 2020-01-10
### Added
- Fix typo in template "input_docker"

## [2.0.3] - 2020-01-09
### Added
- Fix typo in template "input_docker"

## [2.0.2] - 2020-01-09
### Added
- Configs template "input_docker"

## [2.0.1] - 2019-11-29
### Changed
- Update 'lookup' to use 'query'
- Minimum required version of ansible up to 2.5.0

## [2.0.0] - 2019-11-21
### Removed
- Debian wheezy support

## [1.0.8] - 2019-10-24
### Added
- Debian buster support

## [1.0.7] - 2019-10-23
### Changed
- Remove check config before service restart

## [1.0.6] - 2019-06-18
### Fixed
- Telegraf 1.11 config template

## [1.0.5] - 2018-11-07
### Fixed
- Telegraf 1.8.3 config(s) templates

### Added
- Handle configs file state (absent|present)
- Configs template "input_cgroup"
- Configs template "input_netstat"
- Configs template "input_kernel"
- Configs template "input_kernel_vmstat"
- Configs template "input_processes"
- Configs template "input_mysql"
- Configs template "input_nginx"
- Configs template "input_phpfpm"

## [1.0.4] - 2018-10-17
### Fixed
- Python 3 compatibility

## [1.0.3] - 2018-06-05
### Added
- Handle dependency packages to install

### Changed
- Replace deprecated uses of "include"
- Pass apt module packages list directly to the `name` option

## [1.0.2] - 2017-12-06
### Added
- Debian stretch support

## [1.0.1] - 2017-09-28
### Changed
- Fix tests

## [1.0.0] - 2017-05-22
### Added
- Install and configure telegraf v1.3.0
