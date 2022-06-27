from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.manala.roles.tests.unit.compat import unittest
from ansible_collections.manala.roles.plugins.filter.bind_zone import zone_file


class Test(unittest.TestCase):

    def test(self):
        self.assertEqual('''db.foo''', zone_file('foo'))
        self.assertEqual('''db.bar''', zone_file('bar.in-addr.arpa'))
