# Ansible Role: HAProxy

This role will deal with the setup of [HAProxy](http://www.haproxy.org/).

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

None.

## Dependencies

None.

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Configuration example

Handle errorfiles

```yaml
manala_haproxy_errorfiles_exclusive: true

manala_haproxy_errorfiles:
  # Template based
  - file: 400.http
    template: errorfiles/400.http.j2
  # Raw content based
  - file: 400.http
    config: |
      HTTP/1.0 400 Bad request
      Cache-Control: no-cache
      Connection: close
      Content-Type: text/html

      <html><body><h1>400 Bad request</h1>
      Your browser sent an invalid request.
      </body></html>
  # Ensure errorfile is absent
  - file: 432.http
    state: absent # "present" by default
  # Ignore errorfile
  - file: ignore.http
    state: ignore
  # Flatten configs
  - "{{ my_custom_errorfiles_array }}"
```

Use custom config template

```yaml
manala_haproxy_config_template: haproxy/haproxy.cfg.j2
```

Use content based config

```yaml
manala_haproxy_config: |
  defaults
      log     global
      option  dontlognull
      option  abortonclose
```

### Split configuration files

As mentioned in the documentation it's possible to split configuration files as haproxy will load all files found in a specific folder when this one is provided to the `-f` option at service startup.
On Debian this configuration path is handle by the `/etc/default/haproxy` file and the `CONFIG` environment variable.

**Be carefull:** *Files are added in lexical order (using LC_COLLATE=C) to the list of configuration files to be loaded*

#### Defining configuration files

```yaml
manala_haproxy_environment_template: environment/debian/haproxy.j2
manala_haproxy_environment:
  CONFIG: "{{ manala_haproxy_configs_dir }}" # /etc/haproxy/conf.d

manala_haproxy_configs_exclusive: true
manala_haproxy_configs:
  # Template based
  - file: 010-global.cfg
    template: all/haproxy/010-global.j2
  # Raw content based
  - file: 020-defaults.cfg
    config: |
      defaults
          log     global
          option  dontlognull
          option  abortonclose
  # Ensure config is absent
  - file: absent.cfg
    state: absent # "present" by default
  # Ignore config
  - file: ignore.cfg
    state: ignore
  # Flatten configs
  - "{{ my_custom_configs_array }}"
```

## Example playbook

```yaml
- hosts: servers
  tasks:
    - ansible.builtin.import_role:  
        name: manala.roles.haproxy
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
