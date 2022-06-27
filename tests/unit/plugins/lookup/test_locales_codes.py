from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.manala.roles.tests.unit.compat import unittest
from ansible.plugins.loader import lookup_loader

from ansible.errors import AnsibleError


class Test(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.lookup = lookup_loader.get('manala.roles.locales_codes')

    def test_not_dict(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[NotImplemented], []])
        self.assertEqual("Expected a dict but was a <class 'NotImplementedType'>", str(error.exception))

    def test_missing_index(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[{'foo': 'bar'}], []])
        self.assertEqual('Missing "code" key', str(error.exception))

    def test_merge(self):
        self.assertListEqual([
            {'code': 'foo', '_discriminator': 'bar', 'state': 'present'},
        ], self.lookup.run([
            [
                {'code': 'foo', '_discriminator': 'foo'},
                {'code': 'foo', '_discriminator': 'bar'},
            ],
            [],
        ]))

    def test_flatten(self):
        self.assertListEqual([
            {'code': 'foo', 'state': 'present'},
            {'code': 'bar', 'state': 'present'},
        ], self.lookup.run([
            [
                {'code': 'foo'},
                [
                    {'code': 'bar'},
                ]
            ],
            [],
        ]))

    def test_state(self):
        self.assertListEqual([
            {'code': 'foo', 'state': 'present'},
            {'code': 'bar', 'state': 'present'},
            {'code': 'baz', 'state': 'absent'},
        ], self.lookup.run([
            [
                {'code': 'foo'},
                {'code': 'bar', 'state': 'present'},
                {'code': 'baz', 'state': 'absent'},
            ],
            [],
        ]))

    def test_short_syntax(self):
        self.assertListEqual([
            {'code': 'foo', 'state': 'present'},
        ], self.lookup.run([
            [
                'foo',
            ],
            [],
        ]))

    def test_wantcodedenormalized(self):
        self.assertListEqual([
            {'code': '.UTF-8', 'code_denormalized': '.utf8', 'state': 'present'},
        ], self.lookup.run([
            [
                {'code': '.UTF-8'},
            ],
            [],
        ], {}, **{'wantcodedenormalized': True}))

    def test_wantstatecurrent(self):
        self.assertListEqual([
            {'code': 'foo', 'state': 'present', 'state_current': 'present'},
            {'code': 'bar', 'state': 'present', 'state_current': 'absent'},
        ], self.lookup.run([
            [
                {'code': 'foo'},
                {'code': 'bar'},
            ],
            [
                'foo'
            ],
        ], {}, **{'wantstatecurrent': True}))
