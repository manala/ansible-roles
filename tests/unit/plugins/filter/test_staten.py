from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.manala.roles.tests.unit.compat import unittest
from ansible_collections.manala.roles.plugins.filter.staten import staten_ignore, staten

from ansible.errors import AnsibleFilterError


class TestIgnore(unittest.TestCase):

    def test_not_list(self):
        with self.assertRaises(AnsibleFilterError) as error:
            staten_ignore(NotImplemented)
        self.assertEqual("Expected an iterable but was a <class 'NotImplementedType'>", str(error.exception))

    def test(self):
        self.assertListEqual([
            {'state': 'foo'},
            'short_syntax',
        ], staten_ignore([
            {'state': 'ignore'},
            {'state': 'foo'},
            'short_syntax',
        ]))


class Test(unittest.TestCase):

    def test_not_list(self):
        with self.assertRaises(AnsibleFilterError) as error:
            staten(NotImplemented)
        self.assertEqual("Expected an iterable but was a <class 'NotImplementedType'>", str(error.exception))

    def test_invalid_want(self):
        with self.assertRaises(AnsibleFilterError) as error:
            staten([], want="foo")
        self.assertEqual('Expected a want of "present" or "absent" but was "foo"', str(error.exception))

    def test_default(self):
        self.assertListEqual([
            {'state': 'present'},
        ], staten([
            {},
        ]))

    def test_ignore(self):
        self.assertListEqual([
        ], staten([
            {'state': 'ignore'},
        ]))

    def test_invalid_state(self):
        with self.assertRaises(AnsibleFilterError) as error:
            staten([{'state': 'foo'}])
        self.assertEqual('Expected a state of "present" or "absent" but was "foo"', str(error.exception))

    def test_want_present(self):
        self.assertListEqual([
            {'state': 'present'},
            'short_syntax',
        ], staten([
            {'state': 'present'},
            {'state': 'absent'},
            'short_syntax',
        ], want="present"))

    def test_want_absent(self):
        self.assertListEqual([
            {'state': 'absent'},
        ], staten([
            {'state': 'present'},
            {'state': 'absent'},
            'short_syntax',
        ], want="absent"))

    def test(self):
        self.assertListEqual([
            {'state': 'present'},
            {'state': 'absent'},
            'short_syntax',
        ], staten([
            {'state': 'present'},
            {'state': 'absent'},
            'short_syntax',
        ]))
