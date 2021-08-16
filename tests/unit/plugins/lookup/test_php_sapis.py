from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.community.general.tests.unit.compat import unittest
from ansible.plugins.loader import lookup_loader

from ansible.errors import AnsibleError


class Test(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.lookup = lookup_loader.get('manala.roles.php_sapis')

    def test_not_dict(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[NotImplemented], []])
        self.assertEqual("Expected a dict but was a <class 'NotImplementedType'>", str(error.exception))

    def test_missing_index(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[{'foo': 'bar'}], []])
        self.assertEqual('Missing "sapi" key', str(error.exception))

    def test_merge(self):
        self.assertListEqual([
            {'sapi': 'foo', '_discriminator': 'bar', 'state': 'present'},
        ], self.lookup.run([
            [
                {'sapi': 'foo', '_discriminator': 'foo'},
                {'sapi': 'foo', '_discriminator': 'bar'},
            ],
            [
                'foo',
            ],
        ]))

    def test_flatten(self):
        self.assertListEqual([
            {'sapi': 'foo', 'state': 'present'},
            {'sapi': 'bar', 'state': 'present'},
        ], self.lookup.run([
            [
                {'sapi': 'foo'},
                [
                    {'sapi': 'bar'},
                ]
            ],
            [
                'foo',
                'bar',
            ],
        ]))

    def test_state(self):
        self.assertListEqual([
            {'sapi': 'foo', 'state': 'present'},
            {'sapi': 'bar', 'state': 'present'},
            {'sapi': 'baz', 'state': 'absent'},
        ], self.lookup.run([
            [
                {'sapi': 'foo'},
                {'sapi': 'bar', 'state': 'present'},
                {'sapi': 'baz', 'state': 'absent'},
                {'sapi': 'qux', 'state': 'ignore'},
            ],
            [
                'foo',
                'bar',
                'baz',
                'qux',
            ],
        ]))

    def test_invalid_state(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[{'sapi': 'foo', 'state': 'foo'}], ['foo']])
        self.assertEqual('Expected a state of "present", "absent" or "ignore" but was "foo"', str(error.exception))

    def test_wantstate(self):
        self.assertListEqual([
            {'sapi': 'foo', 'state': 'present'},
            {'sapi': 'bar', 'state': 'present'},
        ], self.lookup.run([
            [
                {'sapi': 'foo'},
                {'sapi': 'bar', 'state': 'present'},
                {'sapi': 'baz', 'state': 'absent'},
                {'sapi': 'qux', 'state': 'ignore'},
            ],
            [
                'foo',
                'bar',
                'baz',
                'qux',
            ],
        ], {}, **{'wantstate': 'present'}))

    def test_invalid_wantstate(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[], []], {}, **{'wantstate': 'foo'})
        self.assertEqual('Expected a wanstate of "present" or "absent" but was "foo"', str(error.exception))

    def test_wantmap(self):
        self.assertListEqual([
            'foo',
            'bar',
        ], self.lookup.run([
            [
                {'sapi': 'foo'},
                {'sapi': 'bar'},
            ],
            [
                'foo',
                'bar',
            ],
        ], {}, **{'wantmap': True}))

    def test_short_syntax(self):
        self.assertListEqual([
            {'sapi': 'foo', 'state': 'present'},
        ], self.lookup.run([
            [
                'foo',
            ],
            [
                'foo',
            ],
        ]))

    def test_unknown_sapi(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([['foo'], []])
        self.assertEqual('Unknown "foo" sapi', str(error.exception))

    def test(self):
        self.assertListEqual([
            {'sapi': 'foo', 'state': 'present'},
        ], self.lookup.run([
            [
                {'sapi': 'foo'},
            ],
            [
                'foo',
            ],
        ]))
