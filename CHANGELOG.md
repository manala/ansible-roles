# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

## [3.6.0] - 2023-05-16
### Added
- [Apt] Nodejs 20 support

## [3.5.0] - 2023-05-16
### Added
- [MySQL] MariaDB 10.11 support
- [Apt] MariaDB 10.11 support

## [3.4.1] - 2023-04-28
### Added
- [Php] Fix sapi specific configs

## [3.4.0] - 2023-03-17
### Added
- [Grafana Agent] Introduce role

## [3.3.0] - 2023-02-06
### Changed
- [All] Update minimum version of ansible to 2.14

## [3.2.2] - 2023-02-02
### Fixed
- [Ssh] Update github key

## [3.2.1] - 2023-01-27
### Fixed
- [Apt] Update grafana key
- [Apt] Update influxdb key

## [3.2.0] - 2023-01-09
### Added
- [Apt] Nodejs 18 support
### Changed
- [Telegraf] Update base config template

## [3.1.1] - 2022-12-22
### Changed
- [Apt] Update grafana repository

## [3.1.0] - 2022-12-13
### Added
- [Php] 8.2 support

## [3.0.1] - 2022-12-12
### Changed
- [Apt] Variabilize docker repository address to dynamically match distribution
### Removed
- [Ssh] debian jessie related version 6.7 support
- [Ssh] debian stretch related version 7.4 support

## [3.0.0] - 2022-12-02
### Removed
- [All] Remove debian stretch support
- [Apt] Remove debian stretch related `elasticsearch_2`, `maxscale_2_2`, `mongodb_3_2`, `mongodb_3_4`, `mongodb_3_6`, `mongodb_4_0`, `mysql_5_6`, `mysql_wsrep_5_6`, `galera_3`, `galera_3_31` repositories patterns
- [Elasticsearch] debian stretch related version 2 support
- [Redis] debian stretch related version 3.2 support

## [2.1.0] - 2022-09-19
### Added
- [Promtail] Introduce role
### Changed
- [Apparmor] Deprecate handler "apparmor reload" in favor of "Reload apparmor"
- [Cron] Deprecate handler "cron restart" in favor of "Restart cron"
- [Dhcp] Deprecate handler "dhcp restart" in favor of "Restart dhcp"
- [Dsnqmasq] Deprecate handler "dnsmasq restart" in favor of "Restart dnsmasq"
- [Docker] Deprecate handler "docker restart" in favor of "Restart docker"
- [Elasticsearch] Deprecate handler "elasticsearch restart" in favor of "Restart elasticsearch"
- [Fail2ban] Deprecate handler "fail2ban restart" in favor of "Restart fail2ban"
- [Gitlab] Deprecate handler "gitlab reconfigure" in favor of "Reconfigure gitlab"
- [Gitlab] Deprecate handler "gitlab restart" in favor of "Restart gitlab"
- [Grafana] Deprecate handler "grafana restart" in favor of "Restart grafana"
- [Haproxy] Deprecate handler "haproxy reload" in favor of "Reload haproxy"
- [Haproxy] Deprecate handler "haproxy restart" in favor of "Restart haproxy"
- [InfluxDB] Deprecate handler "influxdb restart" in favor of "Restart influxdb"
- [InfluxDB] Deprecate handler "influxdb start" in favor of "Start influxdb"
- [Keepalived] Deprecate handler "keepalived restart" in favor of "Restart keepalived"
- [Keepalived] Deprecate handler "keepalived reload" in favor of "Reload keepalived"
- [MaxScale] Deprecate handler "maxscale restart" in favor of "Restart maxscale"
- [MongoDB] Deprecate handler "mongodb restart" in favor of "Restart mongodb"
- [MySQL] Deprecate handler "mysql restart" in favor of "Restart mysql"
- [Network] Deprecate handler "networking restart" in favor of "Restart networking"
- [Nginx] Deprecate handler "nginx restart" in favor of "Restart nginx"
- [Nginx] Deprecate handler "do nginx restart" in favor of "Do restart nginx"
- [Php] Deprecate handler "php restart" in favor of "Restart php fpm"
- [Php] Deprecate handler "php fpm restart" in favor of "Restart php fpm"
- [Php] Deprecate handler "do php fpm restart" in favor of "Do restart php fpm"
- [Php] Deprecate handler "php blackfire agent restart" in favor of "Restart php blackfire agent"
- [Proftpd] Deprecate handler "proftpd restart" in favor of "Restart proftpd"
- [Prometheus] Deprecate handler "prometheus restart" in favor of "Restart prometheus"
- [Prometheus] Deprecate handler "prometheus node exporter restart" in favor of "Restart prometheus node exporter"
- [Prometheus] Deprecate handler "prometheus nginx exporter restart" in favor of "Restart prometheus nginx exporter"
- [Prometheus] Deprecate handler "prometheus php fpm exporter restart" in favor of "Restart prometheus php fpm exporter"
- [Promtail] Deprecate handler "promtail restart" in favor of "Restart promtail"
- [Redis] Deprecate handler "redis restart" in favor of "Restart redis"
- [Redis] Deprecate handler "redis-sentinel restart" in favor of "Restart redis-sentinel"
- [RSyslog] Deprecate handler "rsyslog restart" in favor of "Restart rsyslog"
- [SensuGo] Deprecate handler "sensu-backend restart" in favor of "Restart sensu-backend"
- [SensuGo] Deprecate handler "sensu-agent restart" in favor of "Restart sensu-agent"
- [Shorewall] Deprecate handler "shorewall restart" in favor of "Restart shorewall"
- [Ssh] Deprecate handler "ssh reload" in favor of "Reload ssh"
- [Supervisor] Deprecate handler "supervisor restart" in favor of "Restart supervisor"
- [Systemd] Deprecate handler "systemd reload" in favor of "Reload systemd"
- [Telegraf] Deprecate handler "telegraf restart" in favor of "Restart telegraf"

## [2.0.3] - 2022-09-09
### Fixed
- [Apt] Fix github cli key

## [2.0.2] - 2022-08-25
### Fixed
- [Php] Fix extension handling when extension is already disabled

## [2.0.1] - 2022-08-17
### Added
- [Apt] Add GlusterFS 10.2 repository
- [Apt] Add HAProxy 2.6 repository
### Changed
- [Apt] Update Symfony repository

## [2.0.0] - 2022-07-20
### Changed
- [All] Update minimum version of ansible to 2.10
- [All] Use fqcn
- [Ngrok] Switch to v3 stable
- [Symfony CLI] Switch to open source version
- [Gomplate] Use github api to get latest version
- [Vault CLI] Use github api to get latest version
### Added
- [Apt] Install gnupg package
- [Prometheus] Introduce role
### Fixed
- [Apt] Update aptly key

## [1.0.11] - 2022-03-04
### Added
- [Apt] GitHub cli repository

## [1.0.10] - 2022-03-01
### Changed
- [Apt] Trust MySQL repository on stretch
### Added
- [Apt] Add Galera 4.10 and MySQL wsrep 8.0.26 repositories
- [MySQL] Add `login_*` parameters in `users` and `databases` tasks.
- [MySQL] Python installed package is configurable.

## [1.0.9] - 2022-02-21
### Changed
- [Aptly] Publishing is now conditionned on existing published repositories instead of locals
- [Apt] Remove explicit architecture on Manala repository pattern
### Added
- [Aptly] `Repositories` task now handle `architecture` when publishing

## [1.0.8] - 2022-02-09
### Added
- [Apt] Symfony repository

## [1.0.7] - 2022-02-04
### Changed
- [Php] Ensure extensions idempotence

## [1.0.6] - 2022-02-02
### Added
- [MySQL] Support server/client handling via `manala_mysql_server` flag

## [1.0.5] - 2022-01-26
### Changed
- [Apt] Add new Mysql key id and rename the old one `mysql_legacy`

## [1.0.4] - 2022-01-19
### Fixed
- [Composer] No interaction on install check to prevent blocking root warning

## [1.0.3] - 2022-01-10
### Fixed
- [Php] Support multiple `include` in fpm pool configs.

## [1.0.2] - 2022-01-05
### Fixed
- [Mysql] Remove `(want='present')` from staten in `users` and `databases` tasks

## [1.0.1] - 2021-12-27
### Fixed
- [Apt] Kopia key id

## [1.0.0] - 2021-12-17
### Added
- [All] Add debian bullseye support
- [Accounts] `ignore` users state
- [Accounts] users short syntax
- [Accounts] `ignore` groups state
- [Php] 8.1 support

### Fixed
- [Apt] Percona key url
- [Cron] Remove empty lines between jobs
- [MongoDB] `python-pymongo` or `python3-pymongo` apt package as requirements for users handling, depending of tha ansible python version
- [ProFTPd] Remove useless leading spaces in users password file

### Removed
- [All] Remove debian jessie support
- [Ansible Galaxy] Remove alternatives support
- [Apt] Remove deprecated `debian_security` `debian_security_src` `debian_updates` `debian_updates_src` `debian_backports` `dotdeb` `maxscale_2_2_6` `sury_php_debian` repositories patterns
- [Apt] Remove deprecated `sury_php_debian` keys patterns
- [Apt] Remove debian jessie related `mariadb_10_0`, `elasticsearch_1_7`, `nodesource_0_10`, `nodesource_0_12`, `nodesource_5` repositories patterns
- [Apt] Remove debian jessie related `mariadb_legacy` keys patterns
- [Apt] Remove `php5-*` preferences pattern
- [Apt] Remove deprecated `phpmyadmin`, `phppgadmin`, `oauth2-proxy`, `thefuck`, and `httpie` preferences pattern, all related to deprecated manala debian packages
- [Apt] Remove 'logentries' repository, key, and preference patterns (no more available)
- [Apt] Remove 'sensu' repository, key, and preference patterns  (no more available)
- [Beanstalkd] Remove role
- [Elasticsearch] debian jessie related version 1.7 support
- [Grafana] Remove versions 2.0/2.1/2.5 support
- [Graylog Sidecar] Remove role
- [Heka] Remove role
- [Hugo] Remove role
- [Logentries] Remove role
- [Merge] Remove role
- [Mongo Express] Remove role
- [OAuth2 Proxy] Remove role
- [Timezone] Stop using handlers
- [Mailhog] Remove role
- [Nginx] Remove config filters
- [Opcache Dashboard] Remove role
- [PhantomJS] Remove role
- [PhpMyAdmin] Remove role
- [PhpPgAdmin] Remove role
- [PhpRedisAdmin] Remove role
- [Proxmox] Remove role
- [Redis] Remove version 2.8 support
- [Rtail] Remove role
- [Vault] Remove role
- [Varnish] Remove role

### Changed
- [Apt] Don't ensure anymore that configs (`/etc/apt/apt.conf.d`) and preferences (`/etc/apt/preferences.d`) directory exists
- [Apt] Switch default preferences pin priority from 900 to 1000
- [Apt] Use regular expressions in preferences patterns when possible (such as `php`)
- [OhMyZsh] Update users template (see: https://github.com/ohmyzsh/ohmyzsh/commits/master/templates/zshrc.zsh-template)
- [Grafana] Group services handling and stop using handlers
- [Shorewall] Explicit config file permissions
- [Systemd] Use native systemd module for `daemon-reload`

## [0.1.141] - 2021-12-10
### Added
- [Php] Supports php 8.1 for debian stretch and buster
- [Apt] Php 8.1 repository pattern

## [0.1.140] - 2021-11-30
### Added
- [Apt] Add GlusterFS 6.10 repository

## [0.1.139] - 2021-11-17
### Added
- [Apt] Add HAProxy 2.4 repository

## [0.1.138] - 2021-11-03
### Added
- [Accounts] Add trusted GPG public keys

## [0.1.137] - 2021-10-14
### Added
- [MySQL] Supports mariadb 10.6 for debian stretch and buster
- [Apt] MariaDB 10.6 repository pattern

## [0.1.136] - 2021-10-01
### Fixed
- Fix collection preparing script (also looks fo filters in vars/ directory)

## [0.1.135] - 2021-10-01
### Added
- [Gomplate] Add multi architecture support (amd64/arm64)
- [Vault Cli] Add multi architecture support (amd64/arm64)
- [Symfony Cli] Add multi architecture support (amd64/arm64)
- [Ngrok] Add multi architecture support (amd64/arm64)
- [Apt] Add multi architecture support (amd64/arm64/armhf)

### Fixed
- [Gomplate] Fix latest version url parsing when digits contains more than 1 character (just like `3.10.0`)
- [Vault Cli] Fix latest version url parsing when digits contains more than 1 character (just like `3.10.0`)
- [Vault Cli] Fix bin destination and permissions handling

## [0.1.134] - 2021-09-30
### Fixed
- [Gomplate] Fix regex introduced in 0.1.133

## [0.1.133] - 2021-09-30
### Fixed
- [Gomplate] Fix latest version url parsing when digits contains more than 1 character (just like `3.10.0`)

## [0.1.132] - 2021-09-21
### Added
- [Apt] Maxscale 2.5 support
- [Apt] Maxscale 6.1 support
- [Maxscale] MaxScale 2.5 support for Debian stretch and buster
- [Maxscale] MaxScale 6.1 support for Debian stretch and buster

## [0.1.131] - 2021-09-02
### Added
- [Sensu Go] Add file permissions variables

### Changed
- [Sensu Go] Change default file permissions to sensu:sensu - 0640

## [0.1.130] - 2021-06-18
### Changed
- [Apt] Mica repository and key

## [0.1.129] - 2021-06-16
### Added
- [Docker] Handle containers labels option

## [0.1.128] - 2021-06-16
### Added
- [Docker] Handle containers etc_hosts option

## [0.1.127] - 2021-05-17
### Added
- [Apt] Nodejs 16 support

## [0.1.126] - 2021-04-27
### Added
- [Apt] Add Galera 4.8
- [Apt] Add Galera wsrep 8.0.22, 8.0.23

## [0.1.125] - 2021-03-29
### Added
- Default job users can now be defined using `manala_cron_files_defaults`

## [0.1.124] - 2021-03-27
### Fixed
- [Redis] Fix 3.2 templates

## [0.1.123] - 2021-03-26
### Fixed
- [Elasticsearch] Use absolute path when including sub templates
- [Php] Use absolute path when including sub templates
- [Redis] Use absolute path when including sub templates
- [Ssh] Use absolute path when including sub templates

## [0.1.122] - 2021-03-24
### Added
- [Apt] Add Kopia

### Changed
- [Ngrok] Use unified exclusive template lookup
- [Ngrok] Deprecate environment oriented templates
- [Ngrok] Deprecate dict's array configs

## [0.1.121] - 2021-03-08
- Deprecate dict's array sources list

## [0.1.120] - 2021-03-03
### Changed
- [Apt] "packages" tasks must occurs before "holds" one, so that package can be held right after their installation

## [0.1.119] - 2021-03-02
### Added
- [Apt] Add Galera 4 repositories

## [0.1.118] - 2021-03-02
### Added
- [Nginx] Config filters

### Changed
- [Nginx] Use unified exclusive template lookup
- [Nginx] Deprecate environment oriented templates
- [Nginx] Deprecate dict's array configs
- [Nginx] Deprecate `manala_nginx_user` and `manala_nginx_log_dir` variables (only used in dict's array configs)

### Removed
- [Nginx] Don't force configs directory presence anymore

## [0.1.117] - 2021-02-25
### Added
- [Apt] PHP 8.0 support

### Changed
- [Apt] Group package by state, respecting order

## [0.1.116] - 2021-02-23
### Fixed
- [Supervisor] Fix config filter

## [0.1.115] - 2021-02-23
### Fixed
- [Php] XDebug 3 configuration templates

## [0.1.114] - 2021-02-23
### Fixed
- [Vim] Fix templates

## [0.1.113] - 2021-02-23
### Fixed
- [Git] Fix templates

## [0.1.112] - 2021-02-23
### Fixed
- [Ssh] Fix templates

## [0.1.111] - 2021-02-23
### Removed
- [Supervisor] Don't force config directory presence anymore

### Changed
- [Supervisor] Rename `manala_supervisor_config_parameters` filter to `manala_supervisor_config_section`

### Fixed
- [Git] Fix config filter
- [OhMyZsh] Fix users template indentation
- [Redis] Fix config filter
- [Ssh] Fix client template indentation

## [0.1.110] - 2021-02-22
### Added
- [Php] PHP 8.0 support
- [Php] Config filters
- [Php] "state" applications parameter (present|ignore)
- [Php] "ignore" extensions state parameter value
- [Php] "ignore" sapis state parameter value
- [Git] Dict based config filters
- [OhMyZsh] Flatten users array
- [OhMyZsh] Dict based users config filters
- [Vim] Dict based config filters
- [Ssh] Dict based config filters
- [Ssh] Introduce version check

### Changed
- [Php] Use unified exclusive template lookup
- [Php] "manala_php_extensions_pecl_versioned" default value to true (See: https://www.patreon.com/posts/october-update-42636315)
- [Php] Deprecate "manala_php_extensions_pecl_versioned"
- [Php] Deprecate environment oriented templates
- [Php] Deprecate dict's array configs
- [Git] Deprecate dict's array config
- [OhMyZsh] Update users templates
- [OhMyZsh] Deprecate dict's array users config
- [Vim] Deprecate dict's array config
- [Ssh] Deprecate dict's array config

### Removed
- [Php] "cgi" and "phpdbg" sapi configs support
- [Php] useless "cli", "cgi" and "phpdbg" sapi restart handlers
- [Ssh] Useless `manala_ssh_client` flag

## [0.1.109] - 2021-02-04
### Added
- [Composer] Update flags

## [0.1.108] - 2021-01-28
### Changed
- [MySQL] Group services handling and stop using handlers

## [0.1.107] - 2021-01-27
### Fixed
- [Composer] Fix task so it works with ansible check diff

## [0.1.106] - 2021-01-26
### Changed
- [Composer] Handle versions (specific and major)
- [Composer] Use dict based users auth config

## [0.1.105] - 2021-01-18
### Added
- [MySQL] Add Galera_3_31 repository to set on Jessie (last version before deprecation)

## [0.1.104] - 2021-01-15
### Added
- [MySQL] Supports `sql_log_bin` directive on `manala_mysql_users`
- [Gitlab] Flatten configs array

### Changed
- [Gitlab] Use unified exclusive template lookup
- [Aptly] Dict based config filters
- [Aptly] Flatten repositories array
- [Aptly] `ignore` repository state
- [Aptly] Deprecate dict's array config
- [Cron] Use unified exclusive template lookup
- [Cron] Use template ansible module instead of cron ones
- [Cron] Deprecate job `name` parameter
- [Cron] Rename job `job` parameter into `command`

### Removed
- [Cron] Already deprecated dict's array based environment variable handling

## [0.1.103] - 2021-01-11
### Added
- [GlusterFS] `ignore` volumes state

### Changed
- [GlusterFS] Flatten volumes array

## [0.1.102] - 2021-01-11
### Added
- [InbfluxDB] Dict based config filters

### Changed
- [InbfluxDB] Deprecate dict's array configs

## [0.1.101] - 2021-01-07
### Removed
- [HAProxy] Useless `manala_environment_parameters` filter
- [Keepalived] Useless `manala_environment_parameters` filter
- [Apt] Drop elasticsearch 1.5/1.6 support
- [Elasticsearch] Drop 1.5/1.6 support

### Added
- [HAProxy] Handle string comments in `manala_environment` filter
- [Keepalived] Handle string comments in `manala_environment` filter
- [Elasticsearch] Yaml config filter
- [Elasticsearch] Version dependent config/environment files group & mode

### Changed
- [Elasticsearch] Use environment filter
- [Elasticsearch] Deprecate dict's array config/environment templates

## [0.1.100] - 2020-12-22
### Removed
- [Redis] Version 2.4 support
- [Redis] Version 3.0 support
- [Redis] Version 4.0 support

### Added
- [MongoDB] Config content support
- [MongoDB] Config dict support
- [MongoDB] Flatten users array
- [Redis] Version 3.2 support
- [Redis] Version 6.0 support (dict config only)
- [Redis] Config filters

### Changed
- [MongoDB] Deprecate environment oriented templates
- [MongoDB] Deprecate dict's array configs
- [Redis] Rename `manala_redis_config*` variables to `manala_redis_server_config*` (providing backward compatibility)
- [Redis] Guess only MAJOR.MINOR version parts
- [Redis] Deprecate environment oriented templates
- [Redis] Deprecate dict's array configs

## [0.1.99] - 2020-12-18
### Added
- [Docker] `ignore` containers state
- [Docker] Dict based daemon config

### Changed
- [Docker] Flatten containers array
- [Docker] Deprecate dict's array daemon config

## [0.1.98] - 2020-12-17
### Changed
- [Mount] Switch from `eq` to more widely available `equalto` test
- [MySQL] Switch from `eq` to more widely available `equalto` test
- [Systemd] Switch from `eq` to more widely available `equalto` test

## [0.1.97] - 2020-12-16
### Added
- [Backup Manager] Config filters

### Changed
- [Backup Manager] Use unified exclusive template lookup
- [Backup Manager] Deprecate dbms oriented templates
- [Backup Manager] Deprecate dict's array configs

## [0.1.96] - 2020-12-15
### Added
- [Apt] Nodejs 14 support
- [MySQL] `ignore` users state
- [MySQL] `ignore` databases state
- [MySQL] Flatten users array
- [MySQL] Flatten databases array
- [MySQL] Config(s) filters

### Changed
- [MySQL] Use unified exclusive template lookup
- [MySQL] Deprecate dict's array config(s)
- [MySQL] Deprecate environment oriented templates

## [0.1.95] - 2020-12-09
### Removed
- [MaxScale] Version inferior to 2.2 support
- [Apt] MaxScale version inferior to 2.2 support

### Changed
- [MaxScale] Use unified exclusive template lookup
- [MaxScale] Deprecate dict's array config
- [MaxScale] Deprecate dict's array configs
- [MaxScale] Exclusive mode applied on all configs files (not only `*.cnf`)
- [Keepalived] Don't try to create environment file dir
- [Haproxy] Don't try to create environment file dir

### Added
- [Haproxy] Allow content based config

## [0.1.94] - 2020-12-04
### Changed
- [Haproxy] Use errorfiles unified exclusive template lookup

## [0.1.93] - 2020-12-04
### Changed
- [Proftpd] Use unified exclusive template lookup
- [Proftpd] Deprecate dict's array configs
- [Proftpd] Exclusive mode applied on all files (not only `*.conf`)
- [Proftpd] Boolean config values are converted to "on/off" instead of "On/Off"
- [Haproxy] Use unified exclusive template lookup
- [Haproxy] Exclusive mode applied on all files (not only `*.cfg`)
- [Haproxy] Deprecate dict's array environment
- [Haproxy] Deprecate dict's array configs

### Added
- [Proftpd] Config filters
- [Proftpd] Users defaults values now handles `home` and `shell`
- [Proftpd] Handle required parameters keys in config filters
- [Keepalived] Handle required parameters keys in environment filters
- [Logrotate] Handle required parameters keys in config filters
- [Rsyslog] Handle required parameters keys in config filters
- [Supervisor] Handle required parameters keys in config filters
- [Telegraf] Handle required parameters keys in config filters
- [Haproxy] Environment filters
- [Haproxy] Flatten configs array

### Fixed
- [Haproxy] Force restart on environment changes

## [0.1.92] - 2020-12-02
### Added
- [Keepalived] Environment filters
- [Keepalived] Deprecate dict's array environment
- [Keepalived] Deprecate dict's array config

## [0.1.91] - 2020-11-30
### Changed
- [Shorewall] Use unified exclusive template lookup
- [Shorewall] Deprecate dict's array config
- [Shorewall] Deprecate dict's array configs

## [0.1.90] - 2020-11-12
### Fixed
- Collection filters handling in tasks

## [0.1.89] - 2020-11-12
### Added
- [Backup Manager] Handle list configs parameters

## [0.1.88] - 2020-11-12
### Fixed
- [Files] Pass `task_vars` to indentified sub modules in attributes plugin #2

## [0.1.87] - 2020-11-10
### Fixed
- [Files] Pass `task_vars` to indentified sub modules in attributes plugin

## [0.1.86] - 2020-11-09
### Added
- [Systemd] `ignore` service state
- [Mount] `ignore` points state
- [Files] `ignore` attribute state
- [Files] file parents flag
- [Files] file force flag
- [Files] directory parents flag
- [Files] directory force flag

### Changed
- [Systemd] Use unified exclusive template lookup
- [Systemd] dict's array configs
- [Systemd] Flatten services array
- [Mount] Flatten points array
- [Files] Flatten attributes array

## [0.1.85] - 2020-10-30
### Fixed
- [Collection] Collection is now functionning correctly again
- [Collection] Versions 0.1.83, 0.1.84 and 0.1.84-2 are to avoid

### Changed
- [Network] Use unified exclusive template lookup
- [Network] Deprecate dict's array hosts
- [Network] Deprecate dict's array interfaces configs
- [Network] Deprecate dict's array interfaces config
- [Network] Deprecate dict's array resolver config
- [Network] Deprecate dict's array routing tables

## [0.1.84-2] - 2020-10-30
### Changed
- Nothing new from 0.1.84
- This version is for test

## [0.1.84] - 2020-10-30
### Changed
- [Network] Use unified exclusive template lookup
- [Network] Deprecate dict's array hosts
- [Network] Deprecate dict's array interfaces configs
- [Network] Deprecate dict's array interfaces config
- [Network] Deprecate dict's array resolver config
- [Network] Deprecate dict's array routing tables

## [0.1.83] - 2020-10-29
### Changed
- Nothing new from 0.1.82
- This version is for test, but perfectly usable

## [0.1.82] - 2020-10-28
### Fixed
- [Supervisor] `configs/inet_http_server.conf.j2` used old style macros

## [0.1.81] - 2020-10-28
### Changed
- [Rsyslog] Use unified exclusive template lookup
- [Rsyslog] Deprecate dict's array configs

### Added
- [Rsyslog] Configs filters

## [0.1.80] - 2020-10-27
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
