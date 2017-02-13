# Ansible Role: Maxscale

This role will deal with the setup and configuration of MaxScale the Mysql/MariaDB proxy.

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

This role is made to work with the __mariadb maxscale__ debian packages, available on the [__mariadb__ repository](https://downloads.mariadb.com/MaxScale/).
Please use the [**manala.apt**](https://galaxy.ansible.com/manala/apt/) role to handle it properly.
