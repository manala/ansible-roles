from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.community.general.tests.unit.compat import unittest
from ansible.plugins.loader import lookup_loader

from ansible.errors import AnsibleError


class Test(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.lookup = lookup_loader.get('manala.roles.accounts_users_authorized_keys')

    def test_not_dict(self):
        self.assertListEqual([
            {'user': 'bar', 'authorized_keys': ''},
        ], self.lookup.run([
            'foo',
            {'user': 'bar', 'authorized_keys': []},
        ]))

    def test_missing_index(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([{'foo': 'bar'}])
        self.assertEqual('Missing "user" key', str(error.exception))

    def test_merge(self):
        self.assertListEqual([
            {'user': 'foo', 'authorized_keys': '', '_discriminator': 'bar'},
        ], self.lookup.run([
            {'user': 'foo', 'authorized_keys': [], '_discriminator': 'foo'},
            {'user': 'foo', 'authorized_keys': [], '_discriminator': 'bar'},
        ]))

    def test_without_authorized_keys(self):
        self.assertListEqual([
        ], self.lookup.run([
            {'user': 'foo'},
        ]))

    def test_with_authorized_keys(self):
        self.assertListEqual([
            {'user': 'foo', 'authorized_keys': 'foo\nbar'},
        ], self.lookup.run([
            {'user': 'foo', 'authorized_keys': ['foo', 'bar']},
        ]))

    def test_with_authorized_keys_file(self):
        self.assertListEqual([
            {'user': 'foo', 'authorized_keys': 'foo\nbar'},
            {'user': 'bar', 'authorized_keys': 'foo\nbar', 'authorized_keys_file': '/bar'},
            {'user': 'baz', 'authorized_keys': 'foo\nbar', 'authorized_keys_file': '~baz/.ssh/baz'},
            {'user': 'qux', 'authorized_keys': 'foo\nbar'},
            {'user': 'quux', 'authorized_keys': 'foo\nbar'},
        ], self.lookup.run([
            {'user': 'foo', 'authorized_keys': ['foo', 'bar'], 'authorized_keys_file': 'omit'},
            {'user': 'bar', 'authorized_keys': ['foo', 'bar'], 'authorized_keys_file': '/bar'},
            {'user': 'baz', 'authorized_keys': ['foo', 'bar'], 'authorized_keys_file': 'baz'},
            {'user': 'qux', 'authorized_keys': ['foo', 'bar'], 'authorized_keys_file': ''},
            {'user': 'quux', 'authorized_keys': ['foo', 'bar'], 'authorized_keys_file': None},
        ], {'omit': 'omit'}))
