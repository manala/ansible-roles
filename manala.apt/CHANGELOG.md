# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
### Added
- Handle preferences & repositories states (present|absent)
- PHP 7.3 support

## [1.0.24] - 2018-10-17
### Fixed
- Python 3 compatibility

## [1.0.23] - 2018-08-21
### Fixed
- MaxScale minor versions repository patterns keys

## [1.0.22] - 2018-08-21
### Added
- MaxScale minor versions repository patterns

## [1.0.21] - 2018-08-13
### Added
- Nodejs 10 support

## [1.0.20] - 2018-07-10
### Fixed
- Sensu repository & key pattern url

## [1.0.19] - 2018-06-26
### Added
- Certbot preferences pattern missing dependencies
- Thumbor preferences pattern

### Removed
- Elasticsearch < 2.0.0 support on debian stretch

### Changed
- Cleanup distribution handling (blacklist old stables instead of whitelist current stable)

## [1.0.18] - 2018-06-05
### Added
- Percona repository pattern
- Handle dependency packages to install
- Elasticsearch 6 support
- MaxScale 2.2.6 repository pattern

### Fixed
- Fix wrong Sensu APT source distribution ID
- Fix wrong maxscale keyserver

### Changed
- Update aptly key
- Replace deprecated jinja tests used as filters
- Replace deprecated uses of "include"
- Pass apt module packages list directly to the `name` option

## [1.0.17] - 2018-03-21
### Added
- MongoDB 3.6 support

## [1.0.16] - 2018-03-14
### Added
- Certbot preferences pattern

## [1.0.15] - 2018-01-15
### Fixed
- Use keyserver.ubuntu.com for influxdata key (avoid everlasting sni issues with
  wheezy)

## [1.0.14] - 2017-12-08
### Added
- PHP 7.2 support

## [1.0.13] - 2017-12-06
### Added
- Debian stretch support

### Changed
- Adjust tests for debian stretch support

## [1.0.12] - 2017-11-21
### Added
- MaxScale 2.1.10 support
- Proxmox key

### Changed
- Always use keyserver.ubuntu.com when possible

### Fixed
- RabbitMQ key id
- Make Grafana repository distribution release dependent
- Make MongoDB repository distribution release dependent

## [1.0.11] - 2017-11-06
### Added
- Nodejs 9 support

## [1.0.10] - 2017-11-02
### Fixed
- Galera debian repositories

## [1.0.9] - 2017-10-28
### Fixed
- Docker repository key/url

## [1.0.8] - 2017-10-24
### Changed
- Pam Ssh Agent Auth preferences pattern

## [1.0.7] - 2017-10-20
### Fixed
- Debian httpredir.debian.org deprecated in favour of deb.debian.org
- Debian security repository trailing slash

## [1.0.6] - 2017-10-17
### Added
- Backports sloppy support
- Elasticsearch 5 support

### Fixed
- Elasticsearch repositories patterns source urls
- Elasticsearch keys patterns urls

### Fixed
- Mongodb repository apt key

## [1.0.5] - 2017-10-09
### Added
- Nodejs 8 support

### Changed
- Fix ansible 2.3 warnings "when statements should not include jinja2 templating delimiters"

## [1.0.4] - 2017-09-29
### Changed
- Fix varnish 4.0 repository and key

## [1.0.3] - 2017-09-28
### Changed
- Update yarn apt repository and key url

## [1.0.2] - 2017-09-25
### Changed
- Change testing manual debian package (smaller and more reliable)

## [1.0.1] - 2017-05-12
### Added
- `httpie` package preference

## [1.0.0] - 2017-05-11
### Added
- Handle sources list
- Handle preferences
- Handle repositories keys
- Handle repositories
- Handle update
- Handle packages
