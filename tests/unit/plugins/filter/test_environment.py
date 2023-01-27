from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.manala.roles.tests.unit.compat import unittest
from ansible_collections.manala.roles.plugins.filter.environment import environment, environment_parameter

from ansible.errors import AnsibleFilterError


class TestEnvironment(unittest.TestCase):

    def test_not_dict(self):
        with self.assertRaises(AnsibleFilterError) as error:
            environment(NotImplemented)
        self.assertEqual("environment expects a dict but was given a <class 'NotImplementedType'>", str(error.exception))

    def test_exclude(self):
        self.assertEqual('''foo="foo"''', environment({
            'foo': 'foo',
            'bar': 'bar',
        }, exclude=['bar']))

    def test(self):
        self.assertEqual('''bar=123
baz="baz"''', environment({
            'foo': None,
            'bar': 123,
            'baz': 'baz',
        }))


class TestEnvironmentParameter(unittest.TestCase):

    def test_not_dict(self):
        with self.assertRaises(AnsibleFilterError) as error:
            environment_parameter(NotImplemented, '')
        self.assertEqual("environment_parameter parameters expects a dict but was given a <class 'NotImplementedType'>", str(error.exception))

    def test_not_string(self):
        with self.assertRaises(AnsibleFilterError) as error:
            environment_parameter({}, NotImplemented)
        self.assertEqual("environment_parameter key expects a string but was given a <class 'NotImplementedType'>", str(error.exception))

    def test_required(self):
        with self.assertRaises(AnsibleFilterError) as error:
            environment_parameter({'foo': 'foo'}, 'bar', required=True)
        self.assertEqual('environment_parameter requires a value for key bar', str(error.exception))

    def test_default(self):
        self.assertEqual('''foo="foo"''', environment_parameter({
            'bar': 'bar',
        }, 'foo', default='foo'))
        # Missing
        with self.assertRaises(AnsibleFilterError) as error:
            environment_parameter({'bar': 'bar'}, 'foo')
        self.assertEqual('environment_parameter missing a default value for key foo', str(error.exception))

    def test_comment(self):
        self.assertEqual('''#foo="foo"''', environment_parameter({
            'bar': 'bar',
        }, 'foo', default='foo', comment=True))
        self.assertEqual('''bar="bar"''', environment_parameter({
            'bar': 'bar',
        }, 'bar', default='foo', comment=True))
        # Missing default
        with self.assertRaises(AnsibleFilterError) as error:
            environment_parameter({'bar': 'bar'}, 'foo', comment=True)
        self.assertEqual('environment_parameter missing a default value for key foo', str(error.exception))

    def test_comment_string(self):
        self.assertEqual('''comment''', environment_parameter({
            'bar': 'bar',
        }, 'foo', comment='comment'))
        self.assertEqual('''bar="bar"''', environment_parameter({
            'bar': 'bar',
        }, 'bar', comment='comment'))
        # Superfluous default
        self.assertEqual('''comment''', environment_parameter({
            'bar': 'bar',
        }, 'foo', default='foo', comment='comment'))

    def test_unknown_type(self):
        with self.assertRaises(AnsibleFilterError) as error:
            environment_parameter({'foo': NotImplemented}, 'foo')
        self.assertEqual('environment_parameter value of an unknown type <class \'NotImplementedType\'>', str(error.exception))

    def test(self):
        self.assertEqual('''''', environment_parameter({
            'value': None,
        }, 'value'))
        self.assertEqual('''value="string"''', environment_parameter({
            'value': 'string',
        }, 'value'))
        self.assertEqual('''value=123''', environment_parameter({
            'value': 123,
        }, 'value'))
        self.assertEqual('''value=4.56''', environment_parameter({
            'value': 4.56,
        }, 'value'))
