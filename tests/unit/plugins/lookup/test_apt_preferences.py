from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.manala.roles.tests.unit.compat import unittest
from ansible.plugins.loader import lookup_loader

from ansible.errors import AnsibleError


class Test(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.lookup = lookup_loader.get('manala.roles.apt_preferences')

    def test_not_dict(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[NotImplemented], {}, {}, [], '', ''])
        self.assertEqual("Expected a dict but was a <class 'NotImplementedType'>", str(error.exception))

    def test_missing_index(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[{'foo': 'bar'}], {}, {}, [], '', ''])
        self.assertEqual('Missing "file" key', str(error.exception))

    def test_merge(self):
        self.assertListEqual([
            {'file': 'foo', 'template': '', '_discriminator': 'bar', 'state': 'present'},
        ], self.lookup.run([
            [
                {'file': 'foo', '_discriminator': 'foo'},
                {'file': 'foo', '_discriminator': 'bar'},
            ],
            {},
            {},
            [],
            '',
            '',
        ]))

    def test_flatten(self):
        self.assertListEqual([
            {'file': 'foo', 'template': '', 'state': 'present'},
            {'file': 'bar', 'template': '', 'state': 'present'},
        ], self.lookup.run([
            [
                {'file': 'foo'},
                [
                    {'file': 'bar'},
                ]
            ],
            {},
            {},
            [],
            '',
            '',
        ]))

    def test_state(self):
        self.assertListEqual([
            {'file': 'foo', 'template': '', 'state': 'present'},
            {'file': 'bar', 'template': '', 'state': 'present'},
            {'file': 'baz', 'template': '', 'state': 'absent'},
        ], self.lookup.run([
            [
                {'file': 'foo'},
                {'file': 'bar', 'state': 'present'},
                {'file': 'baz', 'state': 'absent'},
                {'file': 'qux', 'state': 'ignore'},
            ],
            {},
            {},
            [],
            '',
            '',
        ]))

    def test_invalid_state(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[{'package': 'foo', 'file': 'foo', 'state': 'foo'}], {}, {}, [], '', ''])
        self.assertEqual('Expected a state of "present", "absent" or "ignore" but was "foo"', str(error.exception))

    def test_wantstate(self):
        self.assertListEqual([
            {'file': 'foo', 'template': '', 'state': 'present'},
            {'file': 'bar', 'template': '', 'state': 'present'},
        ], self.lookup.run([
            [
                {'file': 'foo'},
                {'file': 'bar', 'state': 'present'},
                {'file': 'baz', 'state': 'absent'},
                {'file': 'qux', 'state': 'ignore'},
            ],
            {},
            {},
            [],
            '',
            '',
        ], {}, **{'wantstate': 'present'}))

    def test_invalid_wantstate(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[], {}, {}, [], '', ''], {}, **{'wantstate': 'foo'})
        self.assertEqual('Expected a wanstate of "present" or "absent" but was "foo"', str(error.exception))

    def test_short_syntax(self):
        self.assertListEqual([
            {'file': 'foo', 'package': '*', 'pin': 'origin foo', 'preference': 'foo',
             'priority': 1000, 'repository': 'foo', 'template': '', 'state': 'present'},
            {'file': 'bar_bar', 'package': 'bar bar', 'pin': 'origin bar', 'preference': 'bar.bar:123',
             'priority': 123, 'repository': 'bar.bar', 'template': '', 'state': 'present'},
            {'file': 'baz', 'package': 'baz', 'pin': 'origin baz', 'preference': 'baz@baz',
             'priority': 1000, 'repository': 'baz', 'template': '', 'state': 'present'},
            {'file': 'qux', 'package': 'qux', 'pin': 'origin qux', 'preference': 'qux@qux:456',
             'priority': 456, 'repository': 'qux', 'template': '', 'state': 'present'},
        ], self.lookup.run([
            [
                'foo',
                'bar.bar:123',
                'baz@baz',
                'qux@qux:456',
            ],
            {
                'bar.bar': 'bar bar',
            },
            {
                'foo': {'uris': 'http://foo', 'suites': 'foo/'},
                'bar.bar': {'uris': 'https://bar', 'suites': 'bar/'},
                'baz': {'uris': 'http://baz', 'suites': 'baz/'},
                'qux': {'uris': 'http://qux', 'suites': 'qux/'},
            },
            [],
            '',
            '',
        ]))

    def test_pattern_syntax(self):
        self.assertListEqual([
            {'file': 'foo', 'package': '*', 'pin': 'origin foo', 'preference': 'foo',
             'priority': 1000, 'repository': 'foo', 'template': '', 'state': 'present'},
            {'file': 'bar', 'package': 'package', 'pin': 'pin', 'preference': 'bar',
             'priority': 123, 'template': '', 'state': 'present'},
        ], self.lookup.run([
            [
                {'preference': 'foo'},
                {'preference': 'bar', 'file': 'bar', 'package': 'package', 'pin': 'pin', 'priority': 123},
            ],
            {},
            {
                'foo': {'uris': 'http://foo', 'suites': 'foo/'},
                'bar': {'uris': 'bar', 'suites': 'bar/'},
            },
            [],
            '',
            '',
        ]))

    def test_verbose_syntax(self):
        self.assertListEqual([
            {'file': 'foo', 'package': 'package', 'pin': 'pin', 'priority': 123, 'template': '', 'state': 'present'},
        ], self.lookup.run([
            [
                {'file': 'foo', 'package': 'package', 'pin': 'pin', 'priority': 123},
            ],
            {},
            {},
            [],
            '',
            '',
        ]))

    def test_exclusive(self):
        self.assertListEqual([
            {'file': '/exclusive', 'template': '', 'state': 'absent'},
        ], self.lookup.run([
            [],
            {},
            {},
            [
                {'path': '/exclusive'},
            ],
            '',
            '',
        ]))

    def test_dir(self):
        self.assertListEqual([
            {'file': '/dir/foo', 'template': '', 'state': 'present'},
        ], self.lookup.run([
            [
                {'file': 'foo'},
            ],
            {},
            {},
            [],
            '/dir',
            '',
        ]))

    def test_template(self):
        self.assertListEqual([
            {'file': 'foo', 'template': 'template.j2', 'state': 'present'},
            {'file': 'bar', 'template': 'bar.j2', 'state': 'present'},
        ], self.lookup.run([
            [
                {'file': 'foo'},
                {'file': 'bar', 'template': 'bar.j2'},
            ],
            {},
            {},
            [],
            '',
            'template.j2',
        ]))
