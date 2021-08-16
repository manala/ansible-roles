from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.community.general.tests.unit.compat import unittest
from ansible.plugins.loader import lookup_loader

from ansible.errors import AnsibleError


class Test(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.lookup = lookup_loader.get('manala.roles.environment_files')

    def test_not_dict(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[NotImplemented], {}])
        self.assertEqual("Expected a dict but was a <class 'NotImplementedType'>", str(error.exception))

    def test_missing_index(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[{'foo': 'bar'}], {}])
        self.assertEqual('Missing "file" key', str(error.exception))

    def test_merge(self):
        self.assertListEqual([
            {'file': 'foo', '_discriminator': 'bar', 'export': False},
        ], self.lookup.run([
            [
                {'file': 'foo', '_discriminator': 'foo'},
                {'file': 'foo', '_discriminator': 'bar'},
            ],
            {},
        ]))

    def test_flatten(self):
        self.assertListEqual([
            {'file': 'foo', 'export': False},
            {'file': 'bar', 'export': False},
        ], self.lookup.run([
            [
                {'file': 'foo'},
                [
                    {'file': 'bar'},
                ]
            ],
            {},
        ]))

    def test_short_syntax(self):
        self.assertListEqual([
            {'file': 'bar', 'export': True},
        ], self.lookup.run([
            [
                'foo',
            ],
            {
                'foo': {'file': 'bar', 'export': True},
            },
        ]))

    def test_invalid_pattern(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([['foo'], {}])
        self.assertEqual('"foo" is not a valid pattern', str(error.exception))

    def test(self):
        self.assertListEqual([
            {'file': 'foo', 'export': False},
            {'file': 'bar', 'export': True},
        ], self.lookup.run([
            [
                {'file': 'foo'},
                {'file': 'bar', 'export': True},
            ],
            {},
        ]))
