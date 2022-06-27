from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.manala.roles.tests.unit.compat import unittest
from ansible.plugins.loader import lookup_loader

from ansible.errors import AnsibleError


class Test(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.lookup = lookup_loader.get('manala.roles.npm_packages')

    def test_missing_index(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[{'foo': 'bar'}]])
        self.assertEqual('Missing "package" key', str(error.exception))

    def test_merge(self):
        self.assertListEqual([
            {'package': 'foo', '_discriminator': 'bar'},
        ], self.lookup.run([
            [
                {'package': 'foo', '_discriminator': 'foo'},
                {'package': 'foo', '_discriminator': 'bar'},
            ],
        ]))

    def test_short_syntax(self):
        self.assertListEqual([
            {'package': 'foo'},
        ], self.lookup.run([
            'foo',
        ]))

    def test(self):
        self.assertListEqual([
            {'package': 'foo'},
        ], self.lookup.run([
            [
                {'package': 'foo'},
            ],
        ]))
