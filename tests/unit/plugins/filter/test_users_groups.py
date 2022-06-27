from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.manala.roles.tests.unit.compat import unittest
from ansible_collections.manala.roles.plugins.filter.users_groups import users_groups

from ansible.errors import AnsibleFilterError


class Test(unittest.TestCase):

    def test_not_list(self):
        with self.assertRaises(AnsibleFilterError) as error:
            users_groups(NotImplemented)
        self.assertEqual("Expected an iterable but was a <class 'NotImplementedType'>", str(error.exception))

    def test_not_groups_list(self):
        with self.assertRaises(AnsibleFilterError) as error:
            users_groups([], NotImplemented)
        self.assertEqual("Expected a groups iterable but was a <class 'NotImplementedType'>", str(error.exception))

    def test_skipped(self):
        self.assertListEqual([
            {'user': 'foo'},
        ], users_groups([
            {'user': 'foo'},
        ], [
            {'skipped': True},
        ]))

    def test(self):
        self.assertListEqual([
            {'user': 'foo', 'group': 'foo'},
            {'user': 'bar', 'group': 'bar'},
        ], users_groups([
            {'user': 'foo'},
            {'user': 'bar', 'group': 'baz'},
        ], [
            {'item': {'user': 'foo'}, 'stdout': 'foo'},
            {'item': {'user': 'bar'}, 'stdout': 'bar'},
        ]))
