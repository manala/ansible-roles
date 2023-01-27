from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.manala.roles.tests.unit.compat import unittest
from ansible.plugins.loader import lookup_loader

from ansible.errors import AnsibleError


class Test(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.lookup = lookup_loader.get('manala.roles.apt_repositories')

    def test_not_dict(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[NotImplemented], {}, [], []])
        self.assertEqual("Expected a dict but was a <class 'NotImplementedType'>", str(error.exception))

    def test_missing_index(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[{'foo': 'bar'}], {}, [], []])
        self.assertEqual('Missing "source" key', str(error.exception))

    def test_merge(self):
        self.assertListEqual([
            {'source': 'foo', 'file': '/etc/apt/sources.list.d/foo.list', '_discriminator': 'bar', 'state': 'present'},
        ], self.lookup.run([
            [
                {'source': 'foo', '_discriminator': 'foo'},
                {'source': 'foo', '_discriminator': 'bar'},
            ],
            {},
            [],
            [],
        ]))

    def test_flatten(self):
        self.assertListEqual([
            {'source': 'foo', 'file': '/etc/apt/sources.list.d/foo.list', 'state': 'present'},
            {'source': 'bar', 'file': '/etc/apt/sources.list.d/bar.list', 'state': 'present'},
        ], self.lookup.run([
            [
                {'source': 'foo'},
                [
                    {'source': 'bar'},
                ]
            ],
            {},
            [],
            [],
        ]))

    def test_state(self):
        self.assertListEqual([
            {'source': 'foo', 'file': '/etc/apt/sources.list.d/foo.list', 'state': 'present'},
            {'source': 'bar', 'file': '/etc/apt/sources.list.d/bar.list', 'state': 'present'},
            {'source': 'baz', 'file': '/etc/apt/sources.list.d/baz.list', 'state': 'absent'},
        ], self.lookup.run([
            [
                {'source': 'foo'},
                {'source': 'bar', 'state': 'present'},
                {'source': 'baz', 'state': 'absent'},
                {'source': 'qux', 'state': 'ignore'},
            ],
            [],
            '',
            '',
        ]))

    def test_invalid_state(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[{'source': 'foo', 'key': {'url': 'foo', 'id': 'foo'}, 'state': 'foo'}], {}, [], []])
        self.assertEqual('Expected a state of "present", "absent" or "ignore" but was "foo"', str(error.exception))

    def test_wantstate(self):
        self.assertListEqual([
            {'source': 'foo', 'file': '/etc/apt/sources.list.d/foo.list', 'state': 'present'},
            {'source': 'bar', 'file': '/etc/apt/sources.list.d/bar.list', 'state': 'present'},
        ], self.lookup.run([
            [
                {'source': 'foo'},
                {'source': 'bar', 'state': 'present'},
                {'source': 'baz', 'state': 'absent'},
                {'source': 'qux', 'state': 'ignore'},
            ],
            {},
            [],
            [],
        ], {}, **{'wantstate': 'present'}))

    def test_invalid_wantstate(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[], {}, [], []], {}, **{'wantstate': 'foo'})
        self.assertEqual('Expected a wanstate of "present" or "absent" but was "foo"', str(error.exception))

    def test_short_syntax(self):
        self.assertListEqual([
            {'source': 'foo', 'repository': 'foo', 'file': '/etc/apt/sources.list.d/foo.list', 'state': 'present'},
        ], self.lookup.run([
            [
                'foo',
            ],
            {
                'foo': {'source': 'foo'},
            },
            [],
            []
        ]))

    def test_pattern_syntax(self):
        self.assertListEqual([
            {'source': 'foo', 'repository': 'foo', 'file': '/etc/apt/sources.list.d/foo.list', 'state': 'present'},
        ], self.lookup.run([
            [
                {'repository': 'foo'},
            ],
            {
                'foo': {'source': 'foo'},
            },
            [],
            []
        ]))

    def test_verbose_syntax(self):
        self.assertListEqual([
            {'source': 'foo', 'key': {'url': 'foo', 'id': 'foo'}, 'file': '/etc/apt/sources.list.d/foo.list', 'state': 'present'},
            {'source': 'bar', 'file': '/etc/apt/sources.list.d/baz.list', 'state': 'present'},
        ], self.lookup.run([
            [
                {'source': 'foo', 'key': {'url': 'foo', 'id': 'foo'}},
                {'source': 'bar', 'file': 'baz.list'},
            ],
            {},
            [],
            []
        ]))

    def test_exclusive(self):
        self.assertListEqual([
            {'file': '/exclusive.list', 'state': 'absent'},
        ], self.lookup.run([
            [],
            {},
            [],
            [
                {'path': '/exclusive.list'}
            ]
        ]))

    def test_preferences(self):
        self.assertListEqual([
            {'source': 'foo', 'repository': 'foo', 'file': '/etc/apt/sources.list.d/foo.list', 'state': 'present'},
        ], self.lookup.run([
            [],
            {
                'foo': {'source': 'foo'},
            },
            [
                {'repository': 'foo'}
            ],
            []
        ]))
