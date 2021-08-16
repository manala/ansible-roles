from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.community.general.tests.unit.compat import unittest
from ansible_collections.manala.roles.plugins.filter.yaml import yaml, yaml_parameter, yaml_flatten

from ansible.errors import AnsibleFilterError


class TestYaml(unittest.TestCase):

    def test_not_dict(self):
        with self.assertRaises(AnsibleFilterError) as error:
            yaml(NotImplemented)
        self.assertEqual("yaml expects a dict but was given a <class 'NotImplementedType'>", str(error.exception))

    def test_exclude(self):
        self.assertEqual('''foo: foo''', yaml({
            'foo': 'foo',
            'bar': 'bar',
        }, exclude=['bar']))

    def test(self):
        self.assertEqual('''bar: 123
baz: baz
foo: null''', yaml({
            'foo': None,
            'bar': 123,
            'baz': 'baz',
        }))


class TestYamlParameter(unittest.TestCase):

    def test_not_dict(self):
        with self.assertRaises(AnsibleFilterError) as error:
            yaml_parameter(NotImplemented, '')
        self.assertEqual("yaml_parameter parameters expects a dict but was given a <class 'NotImplementedType'>", str(error.exception))

    def test_not_string(self):
        with self.assertRaises(AnsibleFilterError) as error:
            yaml_parameter({}, NotImplemented)
        self.assertEqual("yaml_parameter key expects a string but was given a <class 'NotImplementedType'>", str(error.exception))

    def test_required(self):
        with self.assertRaises(AnsibleFilterError) as error:
            yaml_parameter({'foo': 'foo'}, 'bar', required=True)
        self.assertEqual('yaml_parameter requires a value for key bar', str(error.exception))

    def test_default(self):
        self.assertEqual('''foo: foo''', yaml_parameter({
            'bar': 'bar',
        }, 'foo', default='foo'))
        # Missing
        with self.assertRaises(AnsibleFilterError) as error:
            yaml_parameter({'bar': 'bar'}, 'foo')
        self.assertEqual('yaml_parameter missing a default value for key foo', str(error.exception))

    def test_comment(self):
        self.assertEqual('''#foo: foo''', yaml_parameter({
            'bar': 'bar',
        }, 'foo', default='foo', comment=True))
        self.assertEqual('''bar: bar''', yaml_parameter({
            'bar': 'bar',
        }, 'bar', default='foo', comment=True))
        # Missing default
        with self.assertRaises(AnsibleFilterError) as error:
            yaml_parameter({'bar': 'bar'}, 'foo', comment=True)
        self.assertEqual('yaml_parameter missing a default value for key foo', str(error.exception))

    def test_comment_string(self):
        self.assertEqual('''comment''', yaml_parameter({
            'bar': 'bar',
        }, 'foo', comment='comment'))
        self.assertEqual('''bar: bar''', yaml_parameter({
            'bar': 'bar',
        }, 'bar', comment='comment'))
        # Superfluous default
        self.assertEqual('''comment''', yaml_parameter({
            'bar': 'bar',
        }, 'foo', default='foo', comment='comment'))

    def test(self):
        self.assertEqual('''value: null''', yaml_parameter({
            'value': None,
        }, 'value'))
        self.assertEqual('''value: true''', yaml_parameter({
            'value': True,
        }, 'value'))
        self.assertEqual('''value: false''', yaml_parameter({
            'value': False,
        }, 'value'))
        self.assertEqual('''value:
- foo
- bar''', yaml_parameter({
            'value': ['foo', 'bar'],
        }, 'value'))
        self.assertEqual('''value:
    bar: bar
    foo: foo''', yaml_parameter({
            'value': {'foo': 'foo', 'bar': 'bar'},
        }, 'value'))
        self.assertEqual('''value: string''', yaml_parameter({
            'value': 'string',
        }, 'value'))
        self.assertEqual('''value: 123''', yaml_parameter({
            'value': 123,
        }, 'value'))
        self.assertEqual('''value: 4.56''', yaml_parameter({
            'value': 4.56,
        }, 'value'))


class TestYamlFlatten(unittest.TestCase):

    def test_not_dict(self):
        with self.assertRaises(AnsibleFilterError) as error:
            yaml_flatten(NotImplemented)
        self.assertEqual("yaml_flatten expects a dict but was given a <class 'NotImplementedType'>", str(error.exception))

    def test(self):
        self.assertEqual({
            'foo': 'foo',
            'bar.baz': 'baz'
        }, yaml_flatten({
            'foo': 'foo',
            'bar': {
                'baz': 'baz'
            }
        }))
        self.assertEqual({
            'parent.foo': 'foo',
            'parent.bar.baz': 'baz'
        }, yaml_flatten({
            'foo': 'foo',
            'bar': {
                'baz': 'baz'
            }
        }, parent='parent'))
        self.assertEqual({
            'parent:foo': 'foo',
            'parent:bar:baz': 'baz'
        }, yaml_flatten({
            'foo': 'foo',
            'bar': {
                'baz': 'baz'
            }
        }, parent='parent', separator=':'))
