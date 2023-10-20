from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.manala.roles.tests.unit.compat import unittest
from ansible.plugins.loader import lookup_loader


class Test(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.lookup = lookup_loader.get('manala.roles.php_packages')

    def test_merge(self):
        self.assertListEqual([
            'php1.2-foo',
        ], self.lookup.run([
            [
                'foo',
                'foo',
            ],
            '1.2',
        ]))

    def test_flatten(self):
        self.assertListEqual([
            'php1.2-foo',
            'php1.2-bar',
        ], self.lookup.run([
            [
                'foo',
                [
                    'bar',
                ]
            ],
            '1.2',
        ]))

    def test(self):
        self.assertListEqual([
            'php1.2-foo',
        ], self.lookup.run([
            [
                'foo',
            ],
            '1.2',
        ]))
