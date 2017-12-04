# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
### Added
- Debian stretch support

### Changed
- Tests on default user shell have been removed according to a debian stretch bug,
  where default user shell is empty (see: https://github.com/manala/ansible-roles/issues/63)

## [1.0.0] - 2017-05-12
### Added
- Handle groups
- Handle users
