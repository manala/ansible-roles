from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.manala.roles.tests.unit.compat import unittest
from ansible.plugins.loader import lookup_loader

from ansible.errors import AnsibleError


class Test(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.lookup = lookup_loader.get('manala.roles.deploy_tasks')

    def test_not_dict(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([NotImplemented])
        self.assertEqual("Expected a dict but was a <class 'NotImplementedType'>", str(error.exception))

    def test_merge(self):
        self.assertListEqual([
            {'task': 'foo', 'options': 'bar', 'when': True, 'dir': '/', 'shared_dir': '/'},
            {'task': 'foo', 'options': 'bar', 'when': True, 'dir': '/', 'shared_dir': '/'},
        ], self.lookup.run([
            {'foo': 'bar'},
            {'foo': 'bar'},
        ]))

    def test_flatten(self):
        self.assertListEqual([
            {'task': 'foo', 'options': 'bar', 'when': True, 'dir': '/', 'shared_dir': '/'},
            {'task': 'bar', 'options': 'baz', 'when': True, 'dir': '/', 'shared_dir': '/'},
        ], self.lookup.run([
            {'foo': 'bar'},
            [
                {'bar': 'baz'},
            ],
        ]))

    def test_short_syntax(self):
        self.assertListEqual([
            {'task': 'foo', 'options': None, 'when': True, 'dir': '/', 'shared_dir': '/'},
        ], self.lookup.run([
            'foo',
        ]))

    def test_guess_task(self):
        self.assertListEqual([
            {'task': 'alpha', 'options': 'alpha', 'when': True, 'dir': '/', 'shared_dir': '/'},
            {'task': 'zeta', 'options': 'zeta', 'when': 'when', 'dir': '/', 'shared_dir': '/'},
        ], self.lookup.run([
            {'alpha': 'alpha', 'beta': 'beta'},
            {'zeta': 'zeta', 'when': 'when'},
        ]))

    def test_when(self):
        self.assertListEqual([
            {'task': 'foo', 'options': 'foo', 'when': 'when', 'dir': '/', 'shared_dir': '/'},
        ], self.lookup.run([
            {'foo': 'foo', 'when': 'when'},
        ]))

    def test_verbose_syntax(self):
        self.assertListEqual([
            {'task': 'foo', 'options': 'bar', 'when': 'when', 'dir': '/', 'shared_dir': '/'},
        ], self.lookup.run([
            {'foo': 'bar', 'when': 'when'},
        ]))
