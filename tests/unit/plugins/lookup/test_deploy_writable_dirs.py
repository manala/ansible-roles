from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.community.general.tests.unit.compat import unittest
from ansible.plugins.loader import lookup_loader

from ansible.errors import AnsibleError


class Test(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.lookup = lookup_loader.get('manala.roles.deploy_writable_dirs')

    def test_not_dict(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[NotImplemented], {}])
        self.assertEqual("Expected a dict but was a <class 'NotImplementedType'>", str(error.exception))

    def test_missing_index(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[{'foo': 'bar'}], {}])
        self.assertEqual('Missing "dir" key', str(error.exception))

    def test_merge(self):
        self.assertListEqual([
            {'dir': 'foo', '_discriminator': 'bar'},
        ], self.lookup.run([
            [
                {'dir': 'foo', '_discriminator': 'foo'},
                {'dir': 'foo', '_discriminator': 'bar'},
            ],
            {}
        ]))

    def test_flatten(self):
        self.assertListEqual([
            {'dir': 'foo'},
            {'dir': 'bar'},
        ], self.lookup.run([
            [
                {'dir': 'foo'},
                [
                    {'dir': 'bar'},
                ],
            ],
            {}
        ]))

    def test_short_syntax(self):
        self.assertListEqual([
            {'dir': 'foo'},
        ], self.lookup.run([
            [
                'foo',
            ],
            {}
        ]))

    def test_default(self):
        self.assertListEqual([
            {'dir': 'foo', 'bar': 'bar'},
        ], self.lookup.run([
            [
                {'dir': 'foo'},
            ],
            {
                'bar': 'bar'
            }
        ]))
