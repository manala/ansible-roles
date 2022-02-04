from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.general.tests.unit.compat import mock
from ansible_collections.community.general.tests.unit.plugins.modules.utils import AnsibleExitJson, ModuleTestCase, set_module_args

from ansible_collections.manala.roles.plugins.modules import php_extension


class Test(ModuleTestCase):

    def setUp(self):
        super(Test, self).setUp()
        self.maxDiff = None
        self.module = php_extension
        self.mock_run_command = mock.patch.object(AnsibleModule, 'run_command')
        self.run_command = self.mock_run_command.start()

    def tearDown(self):
        super(Test, self).tearDown()
        self.mock_run_command.stop()

    def test_enabled(self):
        set_module_args(dict(
            name='foo',
            enabled=True,
        ))
        self.run_command.side_effect = [
            (0, '1.2\n3.4', ''),  # Get versions
            (0, 'foo\nbar', ''),  # Get version 1.2 sapis
            (32, '', ''),  # Get version 1.2 sapi foo module state
            (0, '', ''),  # Set version 1.2 sapi foo module state
            (0, '', ''),  # Get version 1.2 sapi bar module state
            (0, 'baz\nqux', ''),  # Get version 3.4 sapis
            (0, '', 'c'),  # Get version 3.4 sapi baz module state
            (32, '', ''),  # Get version 3.4 sapi qux module state
            (0, '', ''),  # Set version 3.4 sapi qux module state
        ]

        with self.assertRaises(AnsibleExitJson):
            self.module.main()

        self.run_command.assert_any_call('phpenmod -v 1.2 -s foo foo')
        self.run_command.assert_any_call('phpenmod -v 3.4 -s qux foo')

    def test_disabled(self):
        set_module_args(dict(
            name='bar',
            enabled=False,
        ))
        self.run_command.side_effect = [
            (0, '1.2\n3.4', ''),  # Get versions
            (0, 'foo\nbar', ''),  # Get version 1.2 sapis
            (32, '', ''),  # Get version 1.2 sapi foo module state
            (0, '', ''),  # Get version 1.2 sapi bar module state
            (0, '', ''),  # Set version 1.2 sapi bar module state
            (0, 'baz\nqux', ''),  # Get version 3.4 sapis
            (0, '', 'c'),  # Get version 3.4 sapi baz module state
            (0, '', ''),  # Set version 3.4 sapi baz module state
            (32, '', ''),  # Get version 3.4 sapi qux module state
        ]

        with self.assertRaises(AnsibleExitJson):
            self.module.main()

        self.run_command.assert_any_call('phpdismod -v 1.2 -s bar bar')
        self.run_command.assert_any_call('phpdismod -v 3.4 -s baz bar')
