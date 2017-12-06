# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

## [1.0.2] - 2017-12-06
### Added
- Debian stretch support

## [1.0.1] - 2017-10-04
### Changed
- Use unsafe_writes when updating /etc/hosts to work around some situations
  where /etc/hosts is mounted and atomic writes are impossible (such as docker)

## [1.0.0] - 2017-07-17
### Added
- Handle hosts
- Handle resolver
- Handle interfaces
