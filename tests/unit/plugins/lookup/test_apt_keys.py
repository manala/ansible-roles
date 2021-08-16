from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.community.general.tests.unit.compat import unittest
from ansible.plugins.loader import lookup_loader

from ansible.errors import AnsibleError


class Test(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.lookup = lookup_loader.get('manala.roles.apt_keys')

    def test_not_dict(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[NotImplemented], {}, []])
        self.assertEqual("Expected a dict but was a <class 'NotImplementedType'>", str(error.exception))

    def test_missing_index(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[{'foo': 'bar'}], {}, []])
        self.assertEqual('Missing "id" key', str(error.exception))

    def test_merge(self):
        self.assertListEqual([
            {'id': 'foo', '_discriminator': 'bar'},
        ], self.lookup.run([
            [
                {'id': 'foo', '_discriminator': 'foo'},
                {'id': 'foo', '_discriminator': 'bar'},
            ],
            {},
            [],
        ]))

    def test_flatten(self):
        self.assertListEqual([
            {'id': 'foo'},
            {'id': 'bar'},
        ], self.lookup.run([
            [
                {'id': 'foo'},
                [
                    {'id': 'bar'},
                ]
            ],
            {},
            [],
        ]))

    def test_short_syntax(self):
        self.assertListEqual([
            {'id': 'foo'},
        ], self.lookup.run([
            [
                'foo',
            ],
            {
                'foo': {'id': 'foo'},
            },
            []
        ]))

    def test_verbose_syntax(self):
        self.assertListEqual([
            {'id': 'foo'},
        ], self.lookup.run([
            [
                {'id': 'foo'},
            ],
            {},
            []
        ]))

    def test_repositories(self):
        self.assertListEqual([
            {'id': 'foo'},
        ], self.lookup.run([
            [],
            {
                'foo': {'id': 'foo'},
            },
            [
                {'key': 'foo'}
            ]
        ]))
