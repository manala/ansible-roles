from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.community.general.tests.unit.compat import unittest
from ansible.plugins.loader import lookup_loader

from ansible.errors import AnsibleError


class Test(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.lookup = lookup_loader.get('manala.roles.ssh_known_hosts')

    def test_not_dict(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[NotImplemented], {}])
        self.assertEqual("Expected a dict but was a <class 'NotImplementedType'>", str(error.exception))

    def test_missing_index(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[{'foo': 'bar'}], {}])
        self.assertEqual('Missing "host" key', str(error.exception))

    def test_merge(self):
        self.assertListEqual([
            {'host': 'foo', '_discriminator': 'bar'},
        ], self.lookup.run([
            [
                {'host': 'foo', '_discriminator': 'foo'},
                {'host': 'foo', '_discriminator': 'bar'},
            ],
            {},
        ]))

    def test_flatten(self):
        self.assertListEqual([
            {'host': 'foo'},
            {'host': 'bar'},
        ], self.lookup.run([
            [
                {'host': 'foo'},
                [
                    {'host': 'bar'},
                ],
            ],
            {}
        ]))

    def test_short_syntax(self):
        self.assertListEqual([
            {'host': 'host', 'file': '/file'},
        ], self.lookup.run([
            [
                'foo',
            ],
            {
                'foo': {'host': 'host', 'file': '/file'},
            },
        ]))

    def test_file_relative(self):
        self.assertListEqual([
            {'host': 'foo', 'file': 'path/foo'},
            {'host': 'bar', 'file': '/bar'},
        ], self.lookup.run([
            [
                {'host': 'foo', 'file': 'foo'},
                {'host': 'bar', 'file': '/bar'},
            ],
            {},
        ], {'role_path': 'path'}))
