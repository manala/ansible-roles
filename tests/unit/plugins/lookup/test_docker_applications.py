from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.community.general.tests.unit.compat import unittest
from ansible.plugins.loader import lookup_loader

from ansible.errors import AnsibleError


class Test(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.lookup = lookup_loader.get('manala.roles.docker_applications')

    def test_not_dict(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[NotImplemented], {}])
        self.assertEqual("Expected a dict but was a <class 'NotImplementedType'>", str(error.exception))

    def test_missing_index(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[{'foo': 'bar'}], {}])
        self.assertEqual('Missing "application" key', str(error.exception))

    def test_merge(self):
        self.assertListEqual([
            {'application': 'foo', 'command': None, 'environment': {}, 'interactive': None,
             'rm': None, 'tag': None, 'tty': None, 'volumes': {}, 'workdir': None, '_discriminator': 'bar'},
        ], self.lookup.run([
            [
                {'application': 'foo', '_discriminator': 'foo'},
                {'application': 'foo', '_discriminator': 'bar'},
            ],
            {}
        ]))

    def test_flatten(self):
        self.assertListEqual([
            {'application': 'foo', 'command': None, 'environment': {}, 'interactive': None,
             'rm': None, 'tag': None, 'tty': None, 'volumes': {}, 'workdir': None},
            {'application': 'bar', 'command': None, 'environment': {}, 'interactive': None,
             'rm': None, 'tag': None, 'tty': None, 'volumes': {}, 'workdir': None},
        ], self.lookup.run([
            [
                {'application': 'foo'},
                [
                    {'application': 'bar'},
                ],
            ],
            {}
        ]))

    def test_short_syntax(self):
        self.assertListEqual([
            {'application': 'foo', 'image': 'foo', 'command': None, 'environment': {}, 'interactive': None,
             'rm': None, 'tag': None, 'tty': None, 'volumes': {}, 'workdir': None},
            {'application': 'bar', 'image': 'bar', 'command': None, 'environment': {}, 'interactive': None,
             'rm': None, 'tag': 'tag', 'tty': None, 'volumes': {}, 'workdir': None},
            {'application': 'baz', 'image': 'baz', 'command': 'command', 'environment': {}, 'interactive': None,
             'rm': None, 'tag': None, 'tty': None, 'volumes': {}, 'workdir': None},
            {'application': 'qux', 'image': 'qux', 'command': 'command', 'environment': {}, 'interactive': None,
             'rm': None, 'tag': 'tag', 'tty': None, 'volumes': {}, 'workdir': None},
        ], self.lookup.run([
            [
                'foo',
                'bar:tag',
                'baz',
                'qux:tag',
            ],
            {
                'baz': {'command': 'command'},
                'qux': {'command': 'command'},
            }
        ]))

    def test_verbose_syntax(self):
        self.assertListEqual([
            {'application': 'foo', 'command': 'command', 'environment': {}, 'interactive': None,
             'rm': None, 'tag': None, 'tty': None, 'volumes': {}, 'workdir': None},
        ], self.lookup.run([
            [
                {'application': 'foo', 'command': 'command'},
            ],
            {}
        ]))
