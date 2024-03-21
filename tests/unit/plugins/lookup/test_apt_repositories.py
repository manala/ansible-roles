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

    # def test_merge(self):
    #     self.assertListEqual([
    #         {'source': 'foo', 'file': '/etc/apt/sources.list.d/foo.list', '_discriminator': 'bar', 'state': 'present'},
    #     ], self.lookup.run([
    #         [
    #             {'source': 'foo', '_discriminator': 'foo'},
    #             {'source': 'foo', '_discriminator': 'bar'},
    #         ],
    #         {},
    #         [],
    #         [],
    #     ]))

    # def test_flatten(self):
    #     self.assertListEqual([
    #         {'source': 'foo', 'file': '/etc/apt/sources.list.d/foo.list', 'state': 'present'},
    #         {'source': 'bar', 'file': '/etc/apt/sources.list.d/bar.list', 'state': 'present'},
    #     ], self.lookup.run([
    #         [
    #             {'source': 'foo'},
    #             [
    #                 {'source': 'bar'},
    #             ]
    #         ],
    #         {},
    #         [],
    #         [],
    #     ]))

    # def test_state(self):
    #     self.assertListEqual([
    #         {'name': 'foo', 'uris': 'bar', 'suites': 'baz/', 'state': 'present'},
    #         {'name': 'bar', 'uris': 'bar', 'suites': 'baz/', 'state': 'present'},
    #         {'name': 'baz', 'uris': 'bar', 'suites': 'baz/', 'state': 'absent'},
    #     ], self.lookup.run([
    #         [
    #             {'name': 'foo', 'uris': 'bar', 'suites': 'baz/'},
    #             {'name': 'bar', 'uris': 'bar', 'suites': 'baz/', 'state': 'present'},
    #             {'name': 'baz', 'uris': 'bar', 'suites': 'baz/', 'state': 'absent'},
    #             {'name': 'qux', 'uris': 'bar', 'suites': 'baz/', 'state': 'ignore'},
    #         ],
    #         {},
    #         {},
    #         [],
    #         [],
    #         "",
    #     ]))

    def test_invalid_state(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[{'name': 'bar', 'uris': 'bar', 'suites': 'baz/', 'state': 'foo'}], {}, {}, [], [], ""])
        self.assertEqual('Expected a state of "present", "absent" or "ignore" but was "foo"', str(error.exception))

    # def test_wantstate(self):
    #     self.assertListEqual([
    #         {'source': 'foo', 'file': '/etc/apt/sources.list.d/foo.list', 'state': 'present'},
    #         {'source': 'bar', 'file': '/etc/apt/sources.list.d/bar.list', 'state': 'present'},
    #     ], self.lookup.run([
    #         [
    #             {'source': 'foo'},
    #             {'source': 'bar', 'state': 'present'},
    #             {'source': 'baz', 'state': 'absent'},
    #             {'source': 'qux', 'state': 'ignore'},
    #         ],
    #         {},
    #         [],
    #         [],
    #     ], {}, **{'wantstate': 'present'}))

    # def test_invalid_wantstate(self):
    #     with self.assertRaises(AnsibleError) as error:
    #         self.lookup.run([[], {}, [], []], {}, **{'wantstate': 'foo'})
    #     self.assertEqual('Expected a wanstate of "present" or "absent" but was "foo"', str(error.exception))

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
            [   #TODO: add key to foo
                {'name': 'foo', 'uris': 'bar', 'suites': 'baz/'},
                {'name': 'bar', 'uris': 'baz', 'suites': 'qux/'},
            ],
            {},
            {},
            [],
            [],
            "",
        ]))

    # def test_exclusive(self):
    #     self.assertListEqual([
    #         {'file': '/exclusive.list', 'state': 'absent'},
    #     ], self.lookup.run([
    #         [],
    #         {},
    #         {},
    #         [],
    #         [
    #             {'path': '/exclusive.list'}
    #         ],
    #         "",
    #     ]))

    # def test_preferences(self):
    #     self.assertListEqual([
    #         {'source': 'foo', 'repository': 'foo', 'file': '/etc/apt/sources.list.d/foo.list', 'state': 'present'},
    #     ], self.lookup.run([
    #         [],
    #         {
    #             'foo': {'source': 'foo'},
    #         },
    #         {},
    #         [
    #             {'repository': 'foo'}
    #         ],
    #         [],
    #         "",
    #     ]))
