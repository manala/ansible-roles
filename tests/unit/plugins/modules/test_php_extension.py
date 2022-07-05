from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.manala.roles.tests.unit.compat import mock
from ansible_collections.manala.roles.tests.unit.plugins.modules.utils import AnsibleExitJson, ModuleTestCase, set_module_args

from ansible_collections.manala.roles.plugins.modules import php_extension


class Test(ModuleTestCase):

    def setUp(self):
        super(Test, self).setUp()
        self.maxDiff = None
        self.module = php_extension
        # Mocks
        self.mock_run_phpquery = mock.patch.object(self.module, 'run_phpquery')
        self.run_phpquery = self.mock_run_phpquery.start()
        self.mock_run_phpenmod = mock.patch.object(self.module, 'run_phpenmod')
        self.run_phpenmod = self.mock_run_phpenmod.start()
        self.mock_run_phpdismod = mock.patch.object(self.module, 'run_phpdismod')
        self.run_phpdismod = self.mock_run_phpdismod.start()

    def tearDown(self):
        super(Test, self).tearDown()
        # Mocks
        self.mock_run_phpquery.stop()
        self.mock_run_phpenmod.stop()
        self.mock_run_phpdismod.stop()

    def test_enabled(self):
        set_module_args(dict(
            name='module_foo',
            enabled=True,
        ))

        def run_phpquery_side_effect(module, args):
            return {
                '-V': (0, '1.2\n3.4', ''),                         # Get versions
                '-v 1.2 -S': (0, 'sapi_foo\nsapi_bar', ''),        # Get version 1.2 sapis
                '-v 1.2 -s sapi_foo -m module_foo': (32, '', ''),  # Get version 1.2 sapi_foo module state (already disabled)
                '-v 1.2 -s sapi_bar -m module_foo': (0, '', ''),   # Get version 1.2 sapi_bar module state (already enabled)
                '-v 3.4 -S': (0, 'sapi_baz\nsapi_qux', ''),        # Get version 3.4 sapis
                '-v 3.4 -s sapi_baz -m module_foo': (0, '', 'c'),  # Get version 3.4 sapi_baz module state (already enabled)
                '-v 3.4 -s sapi_qux -m module_foo': (32, '', ''),  # Get version 3.4 sapi_baz module state (already disabled)
            }[args]
        self.run_phpquery.side_effect = run_phpquery_side_effect

        with self.assertRaises(AnsibleExitJson):
            self.module.main()

        self.run_phpenmod.assert_has_calls([
            mock.call(mock.ANY, '-v 1.2 -s sapi_foo module_foo'),  # Set version 1.2 sapi foo module state (enabled)
            mock.call(mock.ANY, '-v 3.4 -s sapi_qux module_foo'),  # Set version 3.4 sapi qux module state (enabled)
        ])
        self.run_phpdismod.assert_not_called()

    def test_disabled(self):
        set_module_args(dict(
            name='module_bar',
            enabled=False,
        ))

        def run_phpquery_side_effect(module, args):
            return {
                '-V': (0, '1.2\n3.4', ''),                         # Get versions
                '-v 1.2 -S': (0, 'sapi_foo\nsapi_bar', ''),        # Get version 1.2 sapis
                '-v 1.2 -s sapi_foo -m module_bar': (32, '', ''),  # Get version 1.2 sapi_foo module state (already disabled)
                '-v 1.2 -s sapi_bar -m module_bar': (0, '', ''),   # Get version 1.2 sapi_bar module state (already enabled)
                '-v 3.4 -S': (0, 'sapi_baz\nsapi_qux', ''),        # Get version 3.4 sapis
                '-v 3.4 -s sapi_baz -m module_bar': (0, '', 'c'),  # Get version 3.4 sapi_baz module state (already enabled)
                '-v 3.4 -s sapi_qux -m module_bar': (32, '', ''),  # Get version 3.4 sapi_baz module state (already disabled)
            }[args]
        self.run_phpquery.side_effect = run_phpquery_side_effect

        with self.assertRaises(AnsibleExitJson):
            self.module.main()

        self.run_phpenmod.assert_not_called()
        self.run_phpdismod.assert_has_calls([
            mock.call(mock.ANY, '-v 1.2 -s sapi_bar module_bar'),  # Set version 1.2 sapi foo module state (enabled)
            mock.call(mock.ANY, '-v 3.4 -s sapi_baz module_bar'),  # Set version 3.4 sapi qux module state (enabled)
        ])
