!!! IMPORTANT !!!

According to this thread (see: https://www.mail-archive.com/ansible-devel@googlegroups.com/msg03272.html),
python utilities for unit tests must be either:
- locally carried
- imported by git clone or ansible-galaxy from https://github.com/ansible-collections/community.internal_test_tools

In order to reduce the sucking effect, i've decided to locally import them :)

These files/directories are copy/pasted from https://github.com/ansible-collections/community.internal_test_tools,
release 0.6.1, where `ansible_collections.community.internal_test_tools` imports are replaced to `ansible_collections.manala.roles`:

/tests/unit/compat
/tests/unit/plugins/modules/utils.py
 
