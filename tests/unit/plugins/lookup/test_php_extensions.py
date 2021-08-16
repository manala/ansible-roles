from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.community.general.tests.unit.compat import unittest
from ansible.plugins.loader import lookup_loader

from ansible.errors import AnsibleError


class Test(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.lookup = lookup_loader.get('manala.roles.php_extensions')

    def test_not_dict(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[NotImplemented], [], []])
        self.assertEqual("Expected a dict but was a <class 'NotImplementedType'>", str(error.exception))

    def test_missing_index(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[{'foo': 'bar'}], [], []])
        self.assertEqual('Missing "extension" key', str(error.exception))

    def test_merge(self):
        self.assertListEqual([
            {'extension': 'foo', 'enabled': None, '_discriminator': 'bar', 'state': 'present'},
        ], self.lookup.run([
            [
                {'extension': 'foo', '_discriminator': 'foo'},
                {'extension': 'foo', '_discriminator': 'bar'},
            ],
            [],
            [],
        ]))

    def test_flatten(self):
        self.assertListEqual([
            {'extension': 'foo', 'enabled': None, 'state': 'present'},
            {'extension': 'bar', 'enabled': None, 'state': 'present'},
        ], self.lookup.run([
            [
                {'extension': 'foo'},
                [
                    {'extension': 'bar'},
                ]
            ],
            [],
            [],
        ]))

    def test_state(self):
        self.assertListEqual([
            {'extension': 'foo', 'enabled': None, 'state': 'present'},
            {'extension': 'bar', 'enabled': None, 'state': 'present'},
            {'extension': 'baz', 'enabled': None, 'state': 'absent'},
        ], self.lookup.run([
            [
                {'extension': 'foo'},
                {'extension': 'bar', 'state': 'present'},
                {'extension': 'baz', 'state': 'absent'},
                {'extension': 'qux', 'state': 'ignore'},
            ],
            [],
            [],
        ]))

    def test_invalid_state(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[{'extension': 'foo', 'state': 'foo'}], [], []])
        self.assertEqual('Expected a state of "present", "absent" or "ignore" but was "foo"', str(error.exception))

    def test_wantstate(self):
        self.assertListEqual([
            {'extension': 'foo', 'enabled': None, 'state': 'present'},
            {'extension': 'bar', 'enabled': None, 'state': 'present'},
        ], self.lookup.run([
            [
                {'extension': 'foo'},
                {'extension': 'bar', 'state': 'present'},
                {'extension': 'baz', 'state': 'absent'},
                {'extension': 'qux', 'state': 'ignore'},
            ],
            [],
            [],
        ], {}, **{'wantstate': 'present'}))

    def test_invalid_wantstate(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[], [], []], {}, **{'wantstate': 'foo'})
        self.assertEqual('Expected a wanstate of "present" or "absent" but was "foo"', str(error.exception))

    def wantenabled(self):
        self.assertListEqual([
            {'extension': 'foo', 'enabled': True, 'state': 'present'},
        ], self.lookup.run([
            [
                {'extension': 'foo', 'enabled': True},
                {'extension': 'bar', 'enabled': False},
            ],
            [],
            [],
        ], {}, **{'wantenabled': True}))

    def test_wantmap(self):
        self.assertListEqual([
            'foo',
            'bar',
        ], self.lookup.run([
            [
                {'extension': 'foo'},
                {'extension': 'bar'},
            ],
            [],
            [],
        ], {}, **{'wantmap': True}))

    def test_short_syntax(self):
        self.assertListEqual([
            {'extension': 'foo', 'enabled': None, 'state': 'present'},
        ], self.lookup.run([
            [
                'foo',
            ],
            [],
            [],
        ]))

    def test_sapis_available(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([['foo'], [], ['foo']])
        self.assertEqual('Extension "foo" is known as a sapi', str(error.exception))

    def test_extensions_available(self):
        self.assertListEqual([
            {'extension': 'bar', 'enabled': None, 'state': 'present'},
        ], self.lookup.run([
            [
                {'extension': 'foo'},
                {'extension': 'bar'},
            ],
            [
                'foo'
            ],
            [],
        ]))
