from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.manala.roles.tests.unit.compat import unittest
from ansible.plugins.loader import lookup_loader

from ansible.errors import AnsibleError


class Test(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.lookup = lookup_loader.get('manala.roles.templates_exclusive')

    def test_not_dict(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[NotImplemented], [], '', ''])
        self.assertEqual("Expected a dict but was a <class 'NotImplementedType'>", str(error.exception))

    def test_missing_index(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[{'foo': 'bar'}], [], '', ''])
        self.assertEqual('Missing "file" key', str(error.exception))

    def test_merge(self):
        self.assertListEqual([
            {'file': 'foo', '_discriminator': 'bar', 'template': '', 'state': 'present'},
        ], self.lookup.run([
            [
                {'file': 'foo', '_discriminator': 'foo'},
                {'file': 'foo', '_discriminator': 'bar'},
            ],
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
            [],
            '',
            '',
        ]))

    def test_invalid_state(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[{'file': 'foo', 'state': 'foo'}], [], '', ''])
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
            [],
            '',
            '',
        ], {}, **{'wantstate': 'present'}))

    def test_invalid_wantstate(self):
        with self.assertRaises(AnsibleError) as error:
            self.lookup.run([[], [], '', ''], {}, **{'wantstate': 'foo'})
        self.assertEqual('Expected a wanstate of "present" or "absent" but was "foo"', str(error.exception))

    def test_template_file(self):
        self.assertListEqual([
            {'file': 'foo', 'template': 'foo.j2', 'state': 'present'},
        ], self.lookup.run([
            [
                {'template': 'foo.j2'},
            ],
            [],
            '',
            '',
        ]))

    def test(self):
        self.assertListEqual([
            {'file': '/exclusive', 'template': 'template.j2', 'state': 'absent'},
            {'file': '/dir/foo', 'template': 'template.j2', 'state': 'present'},
        ], self.lookup.run([
            [
                {'file': 'foo'},
            ],
            [
                {'path': '/exclusive'}
            ],
            '/dir',
            'template.j2',
        ]))
