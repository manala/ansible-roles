# Ansible Role: Bind [![Build Status](https://travis-ci.org/manala/ansible-role-bind.svg?branch=master)](https://travis-ci.org/manala/ansible-role-bind)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the setup of [Bind](https://www.isc.org/downloads/bind/).

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.bind
```

Using ansible galaxy requirements file:

```yaml
- src: manala.bind
```

## Role Filters

| Name                    | Description                 |
| ----------------------- | --------------------------- |
| `manala_bind_zone_file` | Standardize zone file names |

## Role Variables

| Name                      | Default                       | Type   | Description            |
| ------------------------- | ----------------------------- | ------ | ---------------------- |
| `manala_bind_user`        | bind                          | String | User                   |
| `manala_bind_group`       | bind                          | String | Group                  |
| `manala_bind_options`     | ['-u {{ manala_bind_user }}'] | Array  | Options                |
| `manala_bind_log_dir`     | /var/log/bind                 | String | Log dir                |
| `manala_bind_configs`     | []                            | Array  | List of config files   |
| `manala_bind_configs_dir` | /etc/bind                     | String | Config files directory |
| `manala_bind_zones_dir`   | /var/cache/bind               | String | Zone files directory   |
| `manala_bind_zones`       | []                            | Array  | List of zone files     |

### Configuration example

#### Options

See: https://linux.die.net/man/8/named

```yaml
manala_bind_options:
  - -u {{ manala_bind_user }}
  - -4 # IPv4 only
```

#### Configs

`file` path is relative to `manala_bind_configs_dir` parameter.

Configs contents could be specified as jinja2 `template` or raw `content`.

Config entries also supports a `state` (present|absent) and a `omit` (false|true) parameter.

```yaml
manala_bind_configs:
  - file: named.conf.options
    template: bind/configs/named.conf.options.j2
  - file: named.conf.local
    content: |
      // Consider adding the 1918 zones here, if they are not used in your
      // organization
      include "{{ manala_bind_configs_dir }}/zones.rfc1918";
  - file: named.conf.foo
    state: absent
  - file: named.conf.bar
    omit: true
```

#### Zones - Static

Either `zone` or `file` parameter is mandatory. If not defined, `file` parameter is computed from `zone`.

`file` path is relative to `manala_bind_zones_dir` parameter.

Configs contents could be specified as jinja2 `template` or raw `content`.

Config entries also supports a `state` (present|absent) and a `omit` (false|true) parameter.

```yaml
manala_bind_zones:
  - zone: foo.local
    template: bind/zones/db.foo.local.j2
  - zone: bar.local
    content: |
      @  IN SOA ns.bar.local. contact.bar.local. (
                  1       ; serial
                  604800  ; refresh (1 week)
                  86400   ; retry (1 day)
                  2419200 ; expire (4 weeks)
                  86400   ; minimum (1 day)
                  )
      @  IN NS  ns.bar.local.
      ns IN A   172.16.1.1";
  - zone: baz.local
    state: absent
  - zone: qux.local
    omit: true
```

#### Zones - Dynamic

`zone` parameter is mandatory, and `dynamic` parameter must be se to true.

The zone configuration must allow update from (at least) localhost.

Considering the dynamic nature of the zone file, `content` or `template` parameters are only taken into account when the file does not exists yet. One can see this as a zone bootstraping.

```yaml
manala_bind_configs:
  - file: named.conf.local
    content: |
      zone "foo.local" {
          type master;
          file "{{ 'foo.local'|manala_bind_zone_file }}";
          allow-update { localhost; };
      };

manala_bind_zones:
  - zone: foo.local
    dynamic: true
    content: |
      @  IN SOA ns.foo.local. contact.foo.local. (
                  1       ; serial
                  604800  ; refresh (1 week)
                  86400   ; retry (1 day)
                  2419200 ; expire (4 weeks)
                  86400   ; minimum (1 day)
                  )
      @  IN NS  ns.foo.local.
      ns IN A   172.16.1.1";
    records:
      - { record: bar, value: 172.16.1.123 }
```

## Example playbook

```yaml
- hosts: servers
  roles:
    - { role: manala.bind }
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
