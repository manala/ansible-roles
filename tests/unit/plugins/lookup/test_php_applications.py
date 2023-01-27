from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.manala.roles.tests.unit.compat import unittest
from ansible.plugins.loader import lookup_loader

from ansible.errors import AnsibleError


class Test(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.lookup = lookup_loader.get('manala.roles.php_applications')

    def test_not_dict(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[NotImplemented], {}])
        self.assertEqual("Expected a dict but was a <class 'NotImplementedType'>", str(error.exception))

    def test_missing_index(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[{'foo': 'bar'}], {}])
        self.assertEqual('Missing "application" key', str(error.exception))

    def test_no_source(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[{'application': 'foo'}], {}])
        self.assertEqual('No source', str(error.exception))

    def test_merge(self):
        self.assertListEqual([
            {'application': 'foo', 'source': 'foo', 'source_version': None, 'version': None, '_discriminator': 'bar', 'state': 'present'},
        ], self.lookup.run([
            [
                {'application': 'foo', 'source': 'foo', '_discriminator': 'foo'},
                {'application': 'foo', 'source': 'foo', '_discriminator': 'bar'},
            ],
            {},
        ]))

    def test_flatten(self):
        self.assertListEqual([
            {'application': 'foo', 'source': 'foo', 'source_version': None, 'version': None, 'state': 'present'},
            {'application': 'bar', 'source': 'bar', 'source_version': None, 'version': None, 'state': 'present'},
        ], self.lookup.run([
            [
                {'application': 'foo', 'source': 'foo'},
                [
                    {'application': 'bar', 'source': 'bar'},
                ]
            ],
            {},
        ]))

    def test_state(self):
        self.assertListEqual([
            {'application': 'foo', 'source': 'foo', 'source_version': None, 'version': None, 'state': 'present'},
            {'application': 'bar', 'source': 'bar', 'source_version': None, 'version': None, 'state': 'present'},
        ], self.lookup.run([
            [
                {'application': 'foo', 'source': 'foo'},
                {'application': 'bar', 'source': 'bar', 'state': 'present'},
                {'application': 'baz', 'source': 'baz', 'state': 'ignore'},
            ],
            {},
        ]))

    def test_invalid_state(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[{'application': 'foo', 'source': 'foo', 'state': 'foo'}], {}])
        self.assertEqual('Expected a state of "present" or "ignore" but was "foo"', str(error.exception))

    def test_wantstate(self):
        self.assertListEqual([
            {'application': 'foo', 'source': 'foo', 'source_version': None, 'version': None, 'state': 'present'},
            {'application': 'bar', 'source': 'bar', 'source_version': None, 'version': None, 'state': 'present'},
        ], self.lookup.run([
            [
                {'application': 'foo', 'source': 'foo'},
                {'application': 'bar', 'source': 'bar', 'state': 'present'},
                {'application': 'baz', 'source': 'baz', 'state': 'ignore'},
            ],
            {},
        ], {}, **{'wantstate': 'present'}))

    def test_invalid_wantstate(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[], {}], {}, **{'wantstate': 'foo'})
        self.assertEqual('Expected a wanstate of "present" but was "foo"', str(error.exception))

    def test_short_syntax(self):
        self.assertListEqual([
            {'application': 'foo', 'source': 'foo', 'source_version': None, 'version': None, 'state': 'present'},
            {'application': 'bar', 'source': 'bar', 'source_version': None, 'version': '1.2.3', 'state': 'present'},
        ], self.lookup.run([
            [
                'foo',
                'bar@1.2.3',
            ],
            {
                'foo': {'source': 'foo'},
                'bar': {'source': 'bar'},
            },
        ]))

    def test_unknown_pattern(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([['foo'], {}])
        self.assertEqual('Unknown "foo" pattern', str(error.exception))

    def test(self):
        self.assertListEqual([
            {'application': 'foo', 'source': 'foo', 'source_version': None, 'version': None, 'state': 'present'},
            {'application': 'bar', 'source': 'bar/1.2.3', 'source_version': 'bar/{version}', 'version': '1.2.3', 'state': 'present'},
        ], self.lookup.run([
            [
                {'application': 'foo'},
                {'application': 'bar', 'source_version': 'bar/{version}', 'version': '1.2.3'},
            ],
            {
                'foo': {'source': 'foo'},
            },
        ]))
