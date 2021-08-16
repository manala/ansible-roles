from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.community.general.tests.unit.compat import unittest
from ansible_collections.manala.roles.plugins.filter.json import json

from ansible.errors import AnsibleFilterError


class Test(unittest.TestCase):

    def test_not_dict(self):
        with self.assertRaises(AnsibleFilterError) as error:
            json(NotImplemented)
        self.assertEqual("json expects a dict but was given a <class 'NotImplementedType'>", str(error.exception))

    def test_exclude(self):
        self.assertEqual('''{
    "foo": "foo"
}''', json({
            'foo': 'foo',
            'bar': 'bar',
        }, exclude=['bar']))

    def test(self):
        self.assertEqual('''{
    "bar": 123,
    "baz": "baz",
    "foo": null
}''', json({
            'foo': None,
            'bar': 123,
            'baz': 'baz',
        }))
