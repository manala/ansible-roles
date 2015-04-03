Ansible Role - phpMyAdmin
=========================

A phpMyAdmin role to install phpMyAdmin on elao symfony standard vagrant box


Requirements
------------

This role only run on elao symfony standard vagrant box. See https://vagrantcloud.com/elao/symfony-standard-debian


Role Variables
--------------

    elao_mysql_phpmyadmin_host: phppgadmin  # phpMyAdmin host


Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: elao.mysql-phpmyadmin}


License
-------

MIT


Author Information
------------------

http://www.elao.com/
