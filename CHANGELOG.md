# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
### Changed
- [MySQL] Omit users privileges if not defined

## [0.1.45] - 2020-06-23
### Changed
- [Ssh] More permissive client test config template

## [0.1.44] - 2020-06-23
### Added
- [Ssh] Both `manala_ssh_server` and `manala_ssh_client` variables to allow both
  `server` and `client` ssh components handling

### Changed
- [Ssh] Rename variables according to `server` and `client` ssh components introduction

## [0.1.43] - 2020-06-19
### Removed
- [Nginx] Redundant HTTPS fastcgi parameter

## [0.1.42] - 2020-06-19
### Fixed
- [Php] Missing configs tags

## [0.1.41] - 2020-06-17
### Added
- [Php] Handle configs states (present|absent) & raw content

### Changed
- [Php] Cli memory_limit default config is now `-1` in  templates

### Fixed
- [Php] Replace deprecated uses of "include"

## [0.1.40] - 2020-06-12
### Added
- [Symfony Cli] Introduce role
