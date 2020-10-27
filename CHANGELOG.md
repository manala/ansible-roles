# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
### Fixed
- [Logrotate] Boolean evaluations in filters
- [Supervisor] Boolean evaluations in filters

## [0.1.78] - 2020-10-26
### Changed
- [Logrotate] Use unified exclusive template lookup
- [Logrotate] Deprecate dict's array configs

### Added
- [Logrotate] Configs filters
- [Supervisor] Config filters
- [Apt] Flatten configs array
- [Apt] Flatten holds array
- [Apt] Flatten keys array
- [Apt] Flatten packages array
- [Apt] Flatten preferences array
- [Apt] Flatten repositories array
- [Apt] Flatten components array
- [Oh My Zsh] Flatten themes array
- [Sudo] Flatten sudoers array
- [Telegraf] Flatten configs array
- [Supervisor] Flatten configs array
- [Motd] Flatten scripts array
- [Accounts] Flatten groups array
- [Accounts] Flatten users array

## [0.1.76] - 2020-10-21
### Fixed
- [Telegraf] Toml encoder edge cases

## [0.1.75] - 2020-10-21
### Fixed
- [Telegraf] Missing dependency in filters

## [0.1.74] - 2020-10-20
### Added
- [Telegraf] Config filters
- [Telegraf] Ensure config directory exists

### Changed
- [Apt] Configs file names based on template name if not provided
- [Motd] Scripts file names based on template name if not provided
- [Oh My Zsh] Custom theme file names based on template name if not provided
- [Oh My Zsh] Exclusive mode applied on all files (not only `*.zsh-theme`)
- [Sudo] Sudoers file names based on template name if not provided
- [Supervisor] Config file names based on template name if not provided
- [Supervisor] Exclusive mode applied on all files (not only `*.conf`)
- [Telegraf] Use unified exclusive template lookup
- [Telegraf] Deprecate dict's array configs
- [Telegraf] Don't touch config if empty or no template defined
- [Telegraf] Exclusive mode applied on all files (not only `*.conf`)
- [Telegraf] Cleanup `input_docker.conf.j2` configs template

## [0.1.73] - 2020-10-16
### Changed
- [Apt] Update Maxscale 2.4 key patterns
- [Maxscale] Update apt key for MaxScale 2.4

## [0.1.72] - 2020-10-14
### Fixed
- [Mongodb] Explicitly enable service

## [0.1.71] - 2020-10-13
### Changed
- [Oh My Zsh] Update users templates

## [0.1.70] - 2020-10-12
### Added
- [Oh My Zsh] Ensure destination directory exists
- [Oh My Zsh] Handle users state (present|ignore)
- [Oh My Zsh] Handle custom themes

## [0.1.69] - 2020-10-11
### Changed
- [Apt] Handle holds by state (present|absent|ignore)

## [0.1.68] - 2020-10-09
### Added
- [Backup manager] Lookup to handle arrays in configs

## [0.1.67] - 2020-10-08
### Modified
- [Gomplate] Clean jinja "format" usages
- [Ngrok] Clean jinja "format" usages
- [Symfony Cli] Clean jinja "format" usages
- [Vault Cli] Introduce role

## [0.1.66] - 2020-10-08
### Added
- [Mongodb] Handle MongoDB 4.4

## [0.1.65] - 2020-10-07
### Added
- [Mongodb] Role can manage MongoDB users

## [0.1.64] - 2020-10-06
### Added
- [Apt] Add 1.8 and 2.2 HAProxy repositories

## [0.1.63] - 2020-09-29
### Fixed
- [Motd] Fix script templates execution flag

### Added
- [MySQL] Supports mariadb 10.5 for debian stretch and buster
- [Apt] MariaDB 10.5 repository pattern
- [Motd] Scripts can be individually ignored
- [Supervisor] Configs can be individually ignored
- [Sudo] Sudoers can be individually ignored
- [Apt] Configs|Packages|Preferences|Repositories can be individually ignored

### Changed
- [Sudo] Use unified exclusive template lookup
- [Sudo] Deprecate dict's array configs
- [Apt] Use unified exclusive template lookup for configs

## [0.1.62] - 2020-09-11
### Fixed
- [Elasticsearch] Fix Explicit file permissions

## [0.1.61] - 2020-09-04
### Added
- [Docker] Allow applications templates

## [0.1.60] - 2020-09-03
### Fixed
- [Gitlab] Fix Explicit file permissions

## [0.1.59] - 2020-08-28
### Changed
- [All] Explicit file permissions #2

## [0.1.58] - 2020-08-26
### Changed
- [All] Explicit file permissions #1

### Fixed
- [Supervisor] Fix `inet_http_server` config template (default config handling)

## [0.1.57] - 2020-08-03
### Changed
- [Supervisor] Use unified exclusive template lookup
- [Supervisor] Deprecate environment oriented templates
- [Supervisor] Deprecate dict's array configs
- [Motd] Cleanup

## [0.1.56] - 2020-07-27
### Added
- [Motd] Support for dynamic motd scripts

## [0.1.55] - 2020-07-09
### Changed
- [Ssh] Stop printing last log on dev/test server config template

## [0.1.54] - 2020-07-09
### Added
- [Cron] Handle defaults parameters for files

## [0.1.53] - 2020-07-07
### Changed
- [Redis] More permissive dev config templates

## [0.1.52] - 2020-07-06
### Added
- [Files] A default can be provided without path, so that it applies to *all* path
- [Files] Flag `parents` to make parent directories as needed

## [0.1.51] - 2020-07-03
### Fixed
- [Symfony Cli] Fix binary path

### Added
- [Ngrok] Debian buster support

### Changed
- [Ngrok] Install from upstream binaries instead of manala debian repository

## [0.1.50] - 2020-06-30
### Fixed
- [Symfony Cli] Fix tag
- [Gomplate] Fix tag

## [0.1.48] - 2020-06-29
### Added
- [Files] Flag `force` for "link_directory" and "link_file" states

### Changed
- [Php] Changed cli memory_limit default config (previous was `-1`). Use a safer 512M default.

## [0.1.47] - 2020-06-25
### Added
- [Gomplate] Introduce role

## [0.1.46] - 2020-06-24
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
