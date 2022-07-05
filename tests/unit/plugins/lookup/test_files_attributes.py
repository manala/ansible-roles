from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.manala.roles.tests.unit.compat import unittest
from ansible.plugins.loader import lookup_loader

from ansible.errors import AnsibleError


class Test(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.lookup = lookup_loader.get('manala.roles.files_attributes')

    def test_not_dict(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[NotImplemented], []])
        self.assertEqual("Expected a dict but was a <class 'NotImplementedType'>", str(error.exception))

    def test_missing_index(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[{'foo': 'bar'}], []])
        self.assertEqual('Missing "path" key', str(error.exception))

    def test_merge(self):
        self.assertListEqual([
            {'path': 'foo', '_discriminator': 'bar'},
        ], self.lookup.run([
            [
                {'path': 'foo', '_discriminator': 'foo'},
                {'path': 'foo', '_discriminator': 'bar'},
            ],
            [],
        ]))

    def test_flatten(self):
        self.assertListEqual([
            {'path': 'foo'},
            {'path': 'bar'},
        ], self.lookup.run([
            [
                {'path': 'foo'},
                [
                    {'path': 'bar'},
                ]
            ],
            [],
        ]))

    def test_state_ignore(self):
        self.assertListEqual([
            {'path': 'foo'},
        ], self.lookup.run([
            [
                {'path': 'foo'},
                {'path': 'bar', 'state': 'ignore'},
            ],
            [],
        ]))

    def test_state_link_directory_missing_src(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[{'path': 'foo', 'state': 'link_directory'}], []])
        self.assertEqual('Missing "src" key', str(error.exception))

    def test_state_link_directory(self):
        self.assertListEqual([
            {'path': 'bar', 'state': 'directory'},
            {'path': 'foo', 'src': 'bar', 'state': 'link'},
        ], self.lookup.run([
            [
                {'path': 'foo', 'src': 'bar', 'state': 'link_directory'},
            ],
            [],
        ]))

    def test_state_link_file_mising_src(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[{'path': 'foo', 'state': 'link_file'}], []])
        self.assertEqual('Missing "src" key', str(error.exception))

    def test_state_link_file(self):
        self.assertListEqual([
            {'path': 'bar', 'state': 'file'},
            {'path': 'foo', 'src': 'bar', 'state': 'link'},
        ], self.lookup.run([
            [
                {'path': 'foo', 'src': 'bar', 'state': 'link_file'},
            ],
            [],
        ]))

    def test_defaults(self):
        self.assertListEqual([
            {'path': 'foo'},
            {'path': 'bar', '_discriminator': 'bar'},
            {'path': 'baz', '_discriminator': 'baz'},
        ], self.lookup.run([
            [
                {'path': 'foo'},
                {'path': 'bar'},
                {'path': 'baz'},
            ],
            [
                {'path': 'bar', '_discriminator': 'bar'},
                {'path': '^baz', '_discriminator': 'baz'},
            ],
        ]))
