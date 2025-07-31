from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.manala.roles.tests.unit.compat import unittest
from ansible_collections.manala.roles.plugins.filter.defaulten import defaulten

from ansible.errors import AnsibleFilterError


class Test(unittest.TestCase):

    def test_not_list(self):
        with self.assertRaises(AnsibleFilterError) as error:
            defaulten(NotImplemented)
        self.assertEqual("Expected an iterable but was a <class 'NotImplementedType'>", str(error.exception))

    def test_no_default_parameter(self):
        with self.assertRaises(AnsibleFilterError) as error:
            defaulten([{'foo': 'bar'}])
        self.assertEqual('Expected default as a dict but was a "None"', str(error.exception))

    def test_default_not_dict(self):
        with self.assertRaises(AnsibleFilterError) as error:
            defaulten([{'foo': 'bar'}], default='not_a_dict')
        self.assertEqual('Expected default as a dict but was a "not_a_dict"', str(error.exception))

    def test_value_not_dict(self):
        with self.assertRaises(AnsibleFilterError) as error:
            defaulten(['foo', 'bar'], default={'baz': 'qux'})
        self.assertEqual('Expected value from values as a dict but was a "foo"', str(error.exception))

    def test_nested_dict_values(self):
        self.assertListEqual([
            {'foo': 'bar', 'config': {'nested': 'override'}}
        ], defaulten(
            [
                {'config': {'nested': 'override'}},
            ],
            default={'foo': 'bar', 'config': {'nested': 'default', 'other': 'value'}}
        ))

    def test(self):
        self.assertListEqual([
            {'foo': 'bar'},
            {'foo': 'foo'},
            {'foo': 'bar', 'bar': 'baz'},
            {'foo': 'bar', 'baz': 'qux'},
        ], defaulten(
            [
                {},
                {'foo': 'foo'},
                {'bar': 'baz'},
                {'foo': 'bar', 'baz': 'qux'},
            ],
            default={'foo': 'bar'},
        ))
