from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.community.general.tests.unit.compat import unittest
from ansible_collections.manala.roles.plugins.filter.proftpd_config import config, config_parameter

from ansible.errors import AnsibleFilterError


class TestConfig(unittest.TestCase):

    def test_not_dict(self):
        with self.assertRaises(AnsibleFilterError) as error:
            config(NotImplemented)
        self.assertEqual("proftpd_config expects a dict but was given a <class 'NotImplementedType'>", str(error.exception))

    def test_exclude(self):
        self.assertEqual('''foo foo''', config({
            'foo': 'foo',
            'bar': 'bar',
        }, exclude=['bar']))

    def test(self):
        self.assertEqual('''bar 123
baz baz''', config({
            'foo': None,
            'bar': 123,
            'baz': 'baz',
        }))


class TestConfigParameter(unittest.TestCase):

    def test_not_dict(self):
        with self.assertRaises(AnsibleFilterError) as error:
            config_parameter(NotImplemented, '')
        self.assertEqual("proftpd_config_parameter parameters expects a dict but was given a <class 'NotImplementedType'>", str(error.exception))

    def test_not_string(self):
        with self.assertRaises(AnsibleFilterError) as error:
            config_parameter({}, NotImplemented)
        self.assertEqual("proftpd_config_parameter key expects a string but was given a <class 'NotImplementedType'>", str(error.exception))

    def test_required(self):
        with self.assertRaises(AnsibleFilterError) as error:
            config_parameter({'foo': 'foo'}, 'bar', required=True)
        self.assertEqual('proftpd_config_parameter requires a value for key bar', str(error.exception))

    def test_default(self):
        self.assertEqual('''foo foo''', config_parameter({
            'bar': 'bar',
        }, 'foo', default='foo'))
        # Missing
        with self.assertRaises(AnsibleFilterError) as error:
            config_parameter({'bar': 'bar'}, 'foo')
        self.assertEqual('proftpd_config_parameter missing a default value for key foo', str(error.exception))

    def test_comment(self):
        self.assertEqual('''#foo foo''', config_parameter({
            'bar': 'bar',
        }, 'foo', default='foo', comment=True))
        self.assertEqual('''bar bar''', config_parameter({
            'bar': 'bar',
        }, 'bar', default='foo', comment=True))
        # Missing default
        with self.assertRaises(AnsibleFilterError) as error:
            config_parameter({'bar': 'bar'}, 'foo', comment=True)
        self.assertEqual('proftpd_config_parameter missing a default value for key foo', str(error.exception))

    def test_comment_string(self):
        self.assertEqual('''comment''', config_parameter({
            'bar': 'bar',
        }, 'foo', comment='comment'))
        self.assertEqual('''bar bar''', config_parameter({
            'bar': 'bar',
        }, 'bar', comment='comment'))
        # Superfluous default
        self.assertEqual('''comment''', config_parameter({
            'bar': 'bar',
        }, 'foo', default='foo', comment='comment'))

    def test_unknown_type(self):
        with self.assertRaises(AnsibleFilterError) as error:
            config_parameter({'foo': NotImplemented}, 'foo')
        self.assertEqual('proftpd_config_parameter value of an unknown type <class \'NotImplementedType\'>', str(error.exception))

    def test(self):
        self.assertEqual('''''', config_parameter({
            'value': None,
        }, 'value'))
        self.assertEqual('''value on''', config_parameter({
            'value': True,
        }, 'value'))
        self.assertEqual('''value off''', config_parameter({
            'value': False,
        }, 'value'))
        self.assertEqual('''value string''', config_parameter({
            'value': 'string',
        }, 'value'))
        self.assertEqual('''value 123''', config_parameter({
            'value': 123,
        }, 'value'))
        self.assertEqual('''value 4.56''', config_parameter({
            'value': 4.56,
        }, 'value'))
