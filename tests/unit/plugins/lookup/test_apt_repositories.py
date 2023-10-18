from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.manala.roles.tests.unit.compat import unittest
from ansible.plugins.loader import lookup_loader

from ansible.errors import AnsibleError


class Test(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.lookup = lookup_loader.get('manala.roles.apt_repositories')

    def test_not_dict(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[NotImplemented], {}, {}, [], [], ""])
        self.assertEqual("Expected a dict but was a <class 'NotImplementedType'>", str(error.exception))

    def test_legacy_source(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[{'source': 'foo'}], {}, {}, [], [], ""])
        self.assertEqual('Using a "source" repository key is deprecated, please use deb822 notation. See manala.roles.apt README.md', str(error.exception))

    def test_missing_index(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[{}], {}, {}, [], [], ""])
        self.assertEqual('Missing "name" key', str(error.exception))

    def test_missing_uris(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[{'name': 'foo'}], {}, {}, [], [], ""])
        self.assertEqual('Missing "uris" key', str(error.exception))

    def test_missing_suites(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[{'name': 'foo', 'uris': 'foo'}], {}, {}, [], [], ""])
        self.assertEqual('Missing "suites" key', str(error.exception))

    def test_missing_components(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[{'name': 'foo', 'uris': 'foo', 'suites': 'bar'}], {}, {}, [], [], ""])
        self.assertEqual('If "components" key not present, "suites" key must end with a "/"', str(error.exception))

    def test_merge(self):
        self.assertListEqual([
            {'name': 'foo', 'uris': 'bar', 'suites': 'baz/', '_discriminator': 'bar', 'state': 'present'},
        ], self.lookup.run([
            [
                {'name': 'foo', 'uris': 'bar', 'suites': 'baz/', '_discriminator': 'foo'},
                {'name': 'foo', 'uris': 'bar', 'suites': 'baz/', '_discriminator': 'bar'},
            ],
            {},
            {},
            [],
            [],
            "",
        ]))

    def test_flatten(self):
        self.assertListEqual([
            {'name': 'foo', 'uris': 'bar', 'suites': 'baz/', 'state': 'present'},
            {'name': 'bar', 'uris': 'bar', 'suites': 'baz/', 'state': 'present'},
        ], self.lookup.run([
            [
                {'name': 'foo', 'uris': 'bar', 'suites': 'baz/'},
                [
                    {'name': 'bar', 'uris': 'bar', 'suites': 'baz/'},
                ]
            ],
            {},
            {},
            [],
            [],
            "",
        ]))

    def test_state(self):
        self.assertListEqual([
            {'name': 'foo', 'uris': 'bar', 'suites': 'baz/', 'state': 'present'},
            {'name': 'bar', 'uris': 'bar', 'suites': 'baz/', 'state': 'present'},
            {'name': 'baz', 'uris': 'bar', 'suites': 'baz/', 'state': 'absent'},
        ], self.lookup.run([
            [
                {'name': 'foo', 'uris': 'bar', 'suites': 'baz/'},
                {'name': 'bar', 'uris': 'bar', 'suites': 'baz/', 'state': 'present'},
                {'name': 'baz', 'uris': 'bar', 'suites': 'baz/', 'state': 'absent'},
                {'name': 'qux', 'uris': 'bar', 'suites': 'baz/', 'state': 'ignore'},
            ],
            {},
            {},
            [],
            [],
            "",
        ]))

    def test_invalid_state(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[{'name': 'bar', 'uris': 'bar', 'suites': 'baz/', 'state': 'foo'}], {}, {}, [], [], ""])
        self.assertEqual('Expected a state of "present", "absent" or "ignore" but was "foo"', str(error.exception))

    def test_wanttype_name(self):
        self.assertListEqual([
            {'name': 'corge', 'state': 'absent'},
            {'name': 'foo', 'uris': 'foo', 'suites': 'foo/', 'state': 'present'},
            {'name': 'bar', 'uris': 'bar', 'suites': 'bar/', 'state': 'present'},
            {'name': 'baz', 'uris': 'baz', 'suites': 'baz/', 'state': 'present', 'legacy_file': 'baz.list'},
            {'name': 'qux', 'uris': 'qux', 'suites': 'qux/', 'state': 'present', 'legacy_file': 'qux.list'},
        ], self.lookup.run([
            [
                {'name': 'foo', 'uris': 'foo', 'suites': 'foo/'},
                {'name': 'bar', 'uris': 'bar', 'suites': 'bar/'},
                {'name': 'baz', 'uris': 'baz', 'suites': 'baz/', 'legacy_file': 'baz.list'},
                {'name': 'qux', 'uris': 'qux', 'suites': 'qux/', 'legacy_file': 'qux.list'},
            ],
            {},
            {},
            [],
            [
                {'path': '/quux.list'},
                {'path': '/corge.sources'},
            ],
            "/etc/file",
        ], {}, **{'wanttype': 'name'}))

    def test_wanttype_file(self):
        self.assertListEqual([
            {'file': '/quux.list', 'state': 'absent'},
            {'file': '/etc/file/baz.list', 'state': 'absent'},
            {'file': '/etc/file/qux.list', 'state': 'absent'},
        ], self.lookup.run([
            [
                {'name': 'foo', 'uris': 'foo', 'suites': 'foo/'},
                {'name': 'bar', 'uris': 'bar', 'suites': 'bar/'},
                {'name': 'baz', 'uris': 'baz', 'suites': 'baz/', 'legacy_file': 'baz.list'},
                {'name': 'qux', 'uris': 'qux', 'suites': 'qux/', 'legacy_file': 'qux.list'},
            ],
            {},
            {},
            [],
            [
                {'path': '/quux.list'},
                {'path': '/corge.sources'},
            ],
            "/etc/file",
        ], {}, **{'wanttype': 'file'}))

    def test_invalid_wanttype(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[], {}, {}, [], [], ""], {}, **{'wanttype': 'foo'})
        self.assertEqual('Expected a wanttype of "name" or "file" but was "foo"', str(error.exception))

    def test_short_syntax(self):
        self.assertListEqual([
            {'name': 'foo', 'repository': 'foo', 'uris': 'bar', 'suites': 'baz/', 'state': 'present'},
        ], self.lookup.run([
            [
                'foo',
            ],
            {
                'foo': {'uris': 'bar', 'suites': 'baz/'},
            },
            {},
            [],
            [],
            "",
        ]))

    def test_pattern_syntax(self):
        self.assertListEqual([
            {'name': 'foo', 'repository': 'foo', 'uris': 'bar', 'suites': 'baz/', 'state': 'present'},
        ], self.lookup.run([
            [
                {'repository': 'foo'},
            ],
            {
                'foo': {'uris': 'bar', 'suites': 'baz/'},
            },
            {},
            [],
            [],
            "",
        ]))

    def test_verbose_syntax(self):
        self.assertListEqual([
            {'name': 'foo', 'uris': 'bar', 'suites': 'baz/', 'state': 'present'},
            {'name': 'bar', 'uris': 'baz', 'suites': 'qux/', 'state': 'present'},
        ], self.lookup.run([
            [
                {'name': 'foo', 'uris': 'bar', 'suites': 'baz/'},
                {'name': 'bar', 'uris': 'baz', 'suites': 'qux/'},
            ],
            {},
            {},
            [],
            [],
            "",
        ]))

    def test_exclusive(self):
        self.assertListEqual([
            {'file': '/exclusive.list', 'state': 'absent'},
        ], self.lookup.run([
            [],
            {},
            {},
            [],
            [
                {'path': '/exclusive.list'}
            ],
            "",
        ]))

    def test_preferences(self):
        self.assertListEqual([
            {'name': 'foo', 'uris': 'bar', 'suites': 'baz/', 'repository': 'foo', 'file': '/etc/apt/sources.list.d/foo.list', 'state': 'present'},
        ], self.lookup.run([
            [],
            {
                'foo': {'name': 'foo', 'uris': 'bar', 'suites': 'baz/', 'file': '/etc/apt/sources.list.d/foo.list'},
            },
            {},
            [
                {'repository': 'foo'}
            ],
            [],
            "",
        ]))
