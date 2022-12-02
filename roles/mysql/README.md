# Ansible Role: Mysql

This role will deal with the setup of [Mysql](https://www.mysql.com/) (>= 5.7).

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

None.

## Dependencies

None.

## Installation

Installation instructions can be found in the main [README.md](https://github.com/manala/ansible-roles/blob/master/README.md)

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

## Configuration example

Install client only
```yaml
manala_mysql_server: false  # Default true
```

### Configure `my.cnf` example

Create an alternative link for debian MySQL official packages
```yaml
manala_mysql_config_alternative: /etc/mysql/my.manala.cnf
```

Use template
```yaml
manala_mysql_config_template: mysql/my.cnf.j2
manala_mysql_config:
  foo: bar
```

Use dict parameters
```yaml
manala_mysql_config:
  mysqld:
    bind-address: 0.0.0.0
    innodb_buffer_pool_size: 4G
```

Use raw content
```yaml
manala_mysql_config: |
  [mysqld]
  bind-address = 0.0.0.0
  innodb_buffer_pool_size = 4G
```

### Configure `/etc/mysql/conf.d` example

A state (present|absent|ignore) can be provided.

```yaml
# Keep configs directory clean
manala_mysql_configs_exclusive: true

manala_mysql_configs:
  # Dict parameters
  - file: foo.cnf
    config:
      client:
        port: 3306
        socket: /var/run/mysqld/mysqld.sock
  # Raw content
  - file: bar.cnf
    config: |
      [client]
      port = 3306
      socket = /var/run/mysqld/mysqld.sock
  # Template
  - file: baz.cnf # file name based on template name if not defined
    template: mysql/baz.cnf.j2
    config:
      foo: bar
  # Ensure config is absent
  - file: absent.cnf
    state: absent # "present" by default
  # Ignore config
  - file: ignore.cnf
    state: ignore
  # Flatten configs
  - "{{ my_custom_configs_array }}"
```

### Users

```yaml
manala_mysql_users:
  # Creates database user 'foo' and password '12345' with all database privileges and 'WITH GRANT OPTION'
  - name: foo
    password: 12345
    priv: '*.*:ALL,GRANT'
  # Modify user `bar` to require SSL connections. Note that REQUIRESSL is a special privilege that should only apply to *.* by itself
  - name: bar
    append_privs: true
    priv: '*.*:REQUIRESSL'
  # Ensure user `baz@localhost` is absent
  - name: baz
    host: localhost
    state: absent
  # Ignore user
  - name: qux
    state: ignore
  # Flatten users
  - "{{ my_custom_users_array }}"
  # Example of skipping binary logging while adding user
  - name: foo
    password: 12345
    priv: '*.*:ALL,GRANT'
    sql_log_bin: false
```

### Databases

```yaml
manala_mysql_databases:
  # Creates foo database
  - name: foo
    encoding: utf8
    collation: utf8_general_ci
  # Ensure database baz is absent
  - name: baz
    state: absent
  # Ignore database
  - name: qux
    state: ignore
  # Flatten databases
  - "{{ my_custom_databases_array }}"
```

### Change default data directory

Be aware it will not clean your previous data directory nor migrate it.

```yaml
manala_mysql_data_dir: /mnt/data

# Required on mariadb
manala_mysql_data_dir_initialize: true

manala_mysql_configs:
  - file: mysqld.cnf
    config:
      mysqld:
        datadir: /mnt/data
```

## MariaDB

If you are using the apt role, define the wanted MariaDB version:

```yaml
manala_apt_preferences:
 - mariadb@mariadb_10_5
```

You will also need to override default packages:

```yaml
manala_mysql_install_packages_default:
  - mariadb-server
  - mariadb-client
```

## Example playbook

```yaml
- hosts: servers
  tasks:
    - ansible.builtin.import_role:  
        name: manala.roles.mysql
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
