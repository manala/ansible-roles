from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.manala.roles.tests.unit.compat import unittest
from ansible_collections.manala.roles.plugins.filter.toml import toml, toml_section, toml_parameter

from ansible.errors import AnsibleFilterError


class TestToml(unittest.TestCase):

    def test_not_dict(self):
        with self.assertRaises(AnsibleFilterError) as error:
            toml(NotImplemented)
        self.assertEqual("toml expects a dict but was given a <class 'NotImplementedType'>", str(error.exception))

    def test_exclude(self):
        self.assertEqual('''foo = "foo"''', toml({
            'foo': 'foo',
            'bar': 'bar',
        }, exclude=['bar']))

    def test(self):
        self.assertEqual('''bar = 123
baz = "baz"
foo =''', toml({
            'foo': None,
            'bar': 123,
            'baz': 'baz',
        }))


class TestTomlSection(unittest.TestCase):

    def test_not_dict(self):
        with self.assertRaises(AnsibleFilterError) as error:
            toml_section(NotImplemented)
        self.assertEqual("toml_section expects a dict but was given a <class 'NotImplementedType'>", str(error.exception))

    def test_exclude(self):
        self.assertEqual('''
  foo = "foo"''', toml_section({
            'foo': 'foo',
            'bar': 'bar',
        }, exclude=['bar']))

    def test(self):
        self.assertEqual('''
  bar = 123
  baz = "baz"
  foo =''', toml_section({
            'foo': None,
            'bar': 123,
            'baz': 'baz',
        }))


class TestTomlParameter(unittest.TestCase):

    def test_not_dict(self):
        with self.assertRaises(AnsibleFilterError) as error:
            toml_parameter(NotImplemented, '')
        self.assertEqual("toml_parameter parameters expects a dict but was given a <class \'NotImplementedType'>", str(error.exception))

    def test_not_string(self):
        with self.assertRaises(AnsibleFilterError) as error:
            toml_parameter({}, NotImplemented)
        self.assertEqual("toml_parameter key expects a string but was given a <class \'NotImplementedType'>", str(error.exception))

    def test_required(self):
        with self.assertRaises(AnsibleFilterError) as error:
            toml_parameter({'foo': 'foo'}, 'bar', required=True)
        self.assertEqual('toml_parameter requires a value for key bar', str(error.exception))

    def test_default(self):
        self.assertEqual('''foo = "foo"''', toml_parameter({
            'bar': 'bar',
        }, 'foo', default='foo'))
        # Missing
        with self.assertRaises(AnsibleFilterError) as error:
            toml_parameter({'bar': 'bar'}, 'foo')
        self.assertEqual('toml_parameter missing a default value for key foo', str(error.exception))

    def test_comment(self):
        self.assertEqual('''# foo = "foo"''', toml_parameter({
            'bar': 'bar',
        }, 'foo', default='foo', comment=True))
        self.assertEqual('''bar = "bar"''', toml_parameter({
            'bar': 'bar',
        }, 'bar', default='foo', comment=True))
        # Missing default
        with self.assertRaises(AnsibleFilterError) as error:
            toml_parameter({'bar': 'bar'}, 'foo', comment=True)
        self.assertEqual('toml_parameter missing a default value for key foo', str(error.exception))

    def test_comment_string(self):
        self.assertEqual('''comment''', toml_parameter({
            'bar': 'bar',
        }, 'foo', comment='comment'))
        self.assertEqual('''bar = "bar"''', toml_parameter({
            'bar': 'bar',
        }, 'bar', comment='comment'))
        # Superfluous default
        self.assertEqual('''comment''', toml_parameter({
            'bar': 'bar',
        }, 'foo', default='foo', comment='comment'))

    def test(self):
        self.assertEqual('''value =''', toml_parameter({
            'value': None,
        }, 'value'))
        self.assertEqual('''value = true''', toml_parameter({
            'value': True,
        }, 'value'))
        self.assertEqual('''value = false''', toml_parameter({
            'value': False,
        }, 'value'))
        self.assertEqual('''value = ["foo", "bar"]''', toml_parameter({
            'value': ['foo', 'bar'],
        }, 'value'))
        self.assertEqual('''[value]
bar = "bar"
foo = "foo"''', toml_parameter({
            'value': {'foo': 'foo', 'bar': 'bar'},
        }, 'value'))
        self.assertEqual('''value = "string"''', toml_parameter({
            'value': 'string',
        }, 'value'))
        self.assertEqual('''value = 123''', toml_parameter({
            'value': 123,
        }, 'value'))
        self.assertEqual('''value = 4.56''', toml_parameter({
            'value': 4.56,
        }, 'value'))
