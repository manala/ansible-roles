from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.community.general.tests.unit.compat import unittest
from ansible_collections.manala.roles.plugins.filter.php_fpm_pools import pools, pools_section, pools_parameter

from ansible.errors import AnsibleFilterError


class TestPools(unittest.TestCase):

    def test_not_dict(self):
        with self.assertRaises(AnsibleFilterError) as error:
            pools(NotImplemented)
        self.assertEqual("php_fpm_pools expects a dict but was given a <class 'NotImplementedType'>", str(error.exception))

    def test_exclude(self):
        self.assertEqual('''[foo]
foo = foo''', pools({
            'foo': {'foo': 'foo'},
            'bar': {'bar': 'bar'},
        }, exclude=['bar']))

    def test(self):
        self.assertEqual('''[bar]
bar = 123

[baz]
baz = baz''', pools({
            'bar': {'bar': 123},
            'baz': {'baz': 'baz'},
        }))


class TestPoolsSection(unittest.TestCase):

    def test_not_dict(self):
        with self.assertRaises(AnsibleFilterError) as error:
            pools_section(NotImplemented)
        self.assertEqual("php_fpm_pools_section expects a dict but was given a <class 'NotImplementedType'>", str(error.exception))

    def test_exclude(self):
        self.assertEqual('''
foo = foo''', pools_section({
            'foo': 'foo',
            'bar': 'bar',
        }, exclude=['bar']))

    def test(self):
        self.assertEqual('''
bar = 123
baz = baz''', pools_section({
            'bar': 123,
            'baz': 'baz',
        }))


class TestPoolsParameter(unittest.TestCase):

    def test_not_dict(self):
        with self.assertRaises(AnsibleFilterError) as error:
            pools_parameter(NotImplemented, '')
        self.assertEqual("php_fpm_pools_parameter parameters expects a dict but was given a <class 'NotImplementedType'>", str(error.exception))

    def test_not_string(self):
        with self.assertRaises(AnsibleFilterError) as error:
            pools_parameter({}, NotImplemented)
        self.assertEqual("php_fpm_pools_parameter key expects a string but was given a <class 'NotImplementedType'>", str(error.exception))

    def test_required(self):
        with self.assertRaises(AnsibleFilterError) as error:
            pools_parameter({'foo': 'foo'}, 'bar', required=True)
        self.assertEqual('php_fpm_pools_parameter requires a value for key bar', str(error.exception))

    def test_default(self):
        self.assertEqual('''foo = foo''', pools_parameter({
            'bar': 'bar',
        }, 'foo', default='foo'))
        # Missing
        with self.assertRaises(AnsibleFilterError) as error:
            pools_parameter({'bar': 'bar'}, 'foo')
        self.assertEqual('php_fpm_pools_parameter missing a default value for key foo', str(error.exception))

    def test_comment(self):
        self.assertEqual(''';foo = foo''', pools_parameter({
            'bar': 'bar',
        }, 'foo', default='foo', comment=True))
        self.assertEqual('''bar = bar''', pools_parameter({
            'bar': 'bar',
        }, 'bar', default='foo', comment=True))
        # Missing default
        with self.assertRaises(AnsibleFilterError) as error:
            pools_parameter({'bar': 'bar'}, 'foo', comment=True)
        self.assertEqual('php_fpm_pools_parameter missing a default value for key foo', str(error.exception))

    def test_comment_string(self):
        self.assertEqual('''comment''', pools_parameter({
            'bar': 'bar',
        }, 'foo', comment='comment'))
        self.assertEqual('''bar = bar''', pools_parameter({
            'bar': 'bar',
        }, 'bar', comment='comment'))
        # Superfluous default
        self.assertEqual('''comment''', pools_parameter({
            'bar': 'bar',
        }, 'foo', default='foo', comment='comment'))

    def test_unknown_type(self):
        with self.assertRaises(AnsibleFilterError) as error:
            pools_parameter({'foo': NotImplemented}, 'foo')
        self.assertEqual('php_fpm_pools_parameter value of an unknown type <class \'NotImplementedType\'>', str(error.exception))

    def test_quote(self):
        self.assertEqual('''value[bar] = "123"\nvalue[foo] = "bar"''', pools_parameter({
            'value': {'foo': 'bar', 'bar': 123},
        }, 'value', quote=True))
        with self.assertRaises(AnsibleFilterError) as error:
            pools_parameter({'value': True}, 'value', quote=True)
        self.assertEqual('php_fpm_pools_parameter unquotable boolean value', str(error.exception))
        with self.assertRaises(AnsibleFilterError) as error:
            pools_parameter({'value': False}, 'value', quote=True)
        self.assertEqual('php_fpm_pools_parameter unquotable boolean value', str(error.exception))
        self.assertEqual('''value = "string"''', pools_parameter({
            'value': 'string',
        }, 'value', quote=True))
        self.assertEqual('''value =''', pools_parameter({
            'value': '',
        }, 'value', quote=True))
        self.assertEqual('''value = "123"''', pools_parameter({
            'value': 123,
        }, 'value', quote=True))
        self.assertEqual('''value = "4.56"''', pools_parameter({
            'value': 4.56,
        }, 'value', quote=True))

    def test(self):
        self.assertEqual('''value[bar] = 123\nvalue[foo] = bar''', pools_parameter({
            'value': {'foo': 'bar', 'bar': 123},
        }, 'value'))
        self.assertEqual('''value = yes''', pools_parameter({
            'value': True,
        }, 'value'))
        self.assertEqual('''value = no''', pools_parameter({
            'value': False,
        }, 'value'))
        self.assertEqual('''value = string''', pools_parameter({
            'value': 'string',
        }, 'value'))
        self.assertEqual('''value =''', pools_parameter({
            'value': '',
        }, 'value'))
        self.assertEqual('''value = 123''', pools_parameter({
            'value': 123,
        }, 'value'))
        self.assertEqual('''value = 4.56''', pools_parameter({
            'value': 4.56,
        }, 'value'))
        self.assertEqual('''value = foo\nvalue = bar''', pools_parameter({
            'value': ['foo', 'bar'],
        }, 'value'))
