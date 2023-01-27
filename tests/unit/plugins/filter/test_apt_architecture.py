from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.manala.roles.tests.unit.compat import unittest
from ansible_collections.manala.roles.plugins.filter.apt_architecture import architecture

from ansible.errors import AnsibleFilterError


class TestArchitecture(unittest.TestCase):

    def test_unsupported(self):
        with self.assertRaises(AnsibleFilterError) as error:
            architecture('foo')
        self.assertEqual('unsupported "foo" architecture', str(error.exception))

    def test(self):
        self.assertEqual('amd64', architecture('x86_64'))
        self.assertEqual('arm64', architecture('aarch64'))
        self.assertEqual('armhf', architecture('armv7l'))
