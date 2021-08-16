from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.community.general.tests.unit.compat import unittest
from ansible.plugins.loader import lookup_loader

from ansible.errors import AnsibleError


class Test(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.lookup = lookup_loader.get('manala.roles.ansible_galaxy_roles')

    def test_not_dict(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([NotImplemented])
        self.assertEqual("Expected a dict but was a <class 'NotImplementedType'>", str(error.exception))

    def test_missing_index(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([{'foo': 'bar'}])
        self.assertEqual('Missing "src" key', str(error.exception))

    def test_merge(self):
        self.assertListEqual([
            {'src': 'foo', '_discriminator': 'bar'},
        ], self.lookup.run([
            {'src': 'foo', '_discriminator': 'foo'},
            {'src': 'foo', '_discriminator': 'bar'},
        ]))

    def test_flatten(self):
        self.assertListEqual([
            {'src': 'foo'},
            {'src': 'bar'},
        ], self.lookup.run([
            {'src': 'foo'},
            [
                {'src': 'bar'},
            ],
        ]))

    def test_short_syntax(self):
        self.assertListEqual([
            {'src': 'foo'},
        ], self.lookup.run([
            'foo',
        ]))

    def test_verbose_syntax(self):
        self.assertListEqual([
            {'src': 'foo', 'version': 'foo'},
        ], self.lookup.run([
            {'src': 'foo', 'version': 'foo'},
        ]))
