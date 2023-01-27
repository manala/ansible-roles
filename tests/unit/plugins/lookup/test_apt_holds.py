from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.manala.roles.tests.unit.compat import unittest
from ansible.plugins.loader import lookup_loader

from ansible.errors import AnsibleError


class Test(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.lookup = lookup_loader.get('manala.roles.apt_holds')

    def test_not_dict(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[NotImplemented], []])
        self.assertEqual("Expected a dict but was a <class 'NotImplementedType'>", str(error.exception))

    def test_missing_index(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[{'foo': 'bar'}], []])
        self.assertEqual('Missing "package" key', str(error.exception))

    def test_merge(self):
        self.assertListEqual([
            {'package': 'foo', '_discriminator': 'bar', 'state': 'present'},
        ], self.lookup.run([
            [
                {'package': 'foo', '_discriminator': 'foo'},
                {'package': 'foo', '_discriminator': 'bar'},
            ],
            []
        ]))

    def test_flatten(self):
        self.assertListEqual([
            {'package': 'foo', 'state': 'present'},
            {'package': 'bar', 'state': 'present'},
        ], self.lookup.run([
            [
                {'package': 'foo'},
                [
                    {'package': 'bar'},
                ]
            ],
            {},
            [],
        ]))

    def test_state(self):
        self.assertListEqual([
            {'package': 'foo', 'state': 'present'},
            {'package': 'bar', 'state': 'present'},
            {'package': 'baz', 'state': 'absent'},
        ], self.lookup.run([
            [
                {'package': 'foo'},
                {'package': 'bar', 'state': 'present'},
                {'package': 'baz', 'state': 'absent'},
                {'package': 'qux', 'state': 'ignore'},
            ],
            {},
            [],
        ]))

    def test_invalid_state(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[{'package': 'foo', 'state': 'foo'}], []])
        self.assertEqual('Expected a state of "present", "absent" or "ignore" but was "foo"', str(error.exception))

    def test(self):
        self.assertListEqual([
            {'package': 'exclusive', 'state': 'absent'},
            {'package': 'foo', 'state': 'present'},
            {'package': 'bar', 'state': 'present'},
        ], self.lookup.run([
            [
                'foo',
                {'package': 'bar'},
            ],
            [
                'exclusive'
            ]
        ]))
