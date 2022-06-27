from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.manala.roles.tests.unit.compat import unittest
from ansible.plugins.loader import lookup_loader

from ansible.errors import AnsibleError


class Test(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.lookup = lookup_loader.get('manala.roles.php_packages_exclusive')

    def test(self):
        self.assertListEqual([
        ], self.lookup.run([
            # Packages wanted
            [
                'php1.2.3-sapi_foo',
                'php1.2.3-extension_foo',
            ],
            # Packages availables sapis
            [
                'php1.2.3-sapi_foo',
                'php1.2.3-sapi_bar',
                'php1.2.3-sapi_baz',
                'php1.2.3-sapi_qux',
                'php1.2.3-sapi_quux',
            ],
            # Packages already presents
            [
                'unknown ok not-installed    php1.2.3-foo',
                'install ok installed    php1.2.3-sapi_foo',
                'install ok installed    php1.2.3-sapi_bar',
                'install ok installed    php1.2.3-sapi_baz',
                'install ok installed    php1.2.3-sapi_qux',
                'install ok installed    php1.2.3-extension_foo',
                'install ok installed    php1.2.3-extension_bar',
                'install ok installed    php1.2.3-extension_baz',
                'install ok installed    php1.2.3-extension_qux',
            ],
            # Packages wanted dependencies
            [
                'Package php1.2.3-sapi_foo depends on:',
                '  php1.2.3-sapi_bar php1.2.3-sapi_baz',
                'Package php1.2.3-extension_foo depends on:',
                '  php1.2.3-extension_bar php1.2.3-extension_baz',
            ],
            # Exclusive - Sapis
            False,
            # Exclusive - Extensions
            False,
        ]))

    def test_sapis_excusive(self):
        self.assertListEqual([
            'php1.2.3-sapi_qux',
        ], self.lookup.run([
            # Packages wanted
            [
                'php1.2.3-sapi_foo',
                'php1.2.3-extension_foo',
            ],
            # Packages availables sapis
            [
                'php1.2.3-sapi_foo',
                'php1.2.3-sapi_bar',
                'php1.2.3-sapi_baz',
                'php1.2.3-sapi_qux',
                'php1.2.3-sapi_quux',
            ],
            # Packages already presents
            [
                'unknown ok not-installed    php1.2.3-foo',
                'install ok installed    php1.2.3-sapi_foo',
                'install ok installed    php1.2.3-sapi_bar',
                'install ok installed    php1.2.3-sapi_baz',
                'install ok installed    php1.2.3-sapi_qux',
                'install ok installed    php1.2.3-extension_foo',
                'install ok installed    php1.2.3-extension_bar',
                'install ok installed    php1.2.3-extension_baz',
                'install ok installed    php1.2.3-extension_qux',
            ],
            # Packages wanted dependencies
            [
                'Package php1.2.3-sapi_foo depends on:',
                '  php1.2.3-sapi_bar php1.2.3-sapi_baz',
                'Package php1.2.3-extension_foo depends on:',
                '  php1.2.3-extension_bar php1.2.3-extension_baz',
            ],
            # Exclusive - Sapis
            True,
            # Exclusive - Extensions
            False,
        ]))

    def test_extensions_excusive(self):
        self.assertListEqual([
            'php1.2.3-extension_qux',
        ], self.lookup.run([
            # Packages wanted
            [
                'php1.2.3-sapi_foo',
                'php1.2.3-extension_foo',
            ],
            # Packages availables sapis
            [
                'php1.2.3-sapi_foo',
                'php1.2.3-sapi_bar',
                'php1.2.3-sapi_baz',
                'php1.2.3-sapi_qux',
                'php1.2.3-sapi_quux',
            ],
            # Packages already presents
            [
                'unknown ok not-installed    php1.2.3-foo',
                'install ok installed    php1.2.3-sapi_foo',
                'install ok installed    php1.2.3-sapi_bar',
                'install ok installed    php1.2.3-sapi_baz',
                'install ok installed    php1.2.3-sapi_qux',
                'install ok installed    php1.2.3-extension_foo',
                'install ok installed    php1.2.3-extension_bar',
                'install ok installed    php1.2.3-extension_baz',
                'install ok installed    php1.2.3-extension_qux',
            ],
            # Packages wanted dependencies
            [
                'Package php1.2.3-sapi_foo depends on:',
                '  php1.2.3-sapi_bar php1.2.3-sapi_baz',
                'Package php1.2.3-extension_foo depends on:',
                '  php1.2.3-extension_bar php1.2.3-extension_baz',
            ],
            # Exclusive - Sapis
            False,
            # Exclusive - Extensions
            True,
        ]))
