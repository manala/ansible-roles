# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
    name: deploy_log
    type: stdout
    author: Manala (@manala)
    short_description: print stdout/stderr
    description:
      - Print stdout/stderr
'''

from ansible.plugins.callback import CallbackBase


class CallbackModule(CallbackBase):
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'notification'
    CALLBACK_NAME = 'manala_deploy_log'
    CALLBACK_NEEDS_WHITELIST = False

    def v2_runner_item_on_failed(self, result):
        if ('module_stdout' in result._result) and result._result.get('module_stdout'):
            print('module_stdout:')
            print(result._result.get('module_stdout'))
        if ('module_stderr' in result._result) and result._result.get('module_stderr'):
            print('module_stderr:')
            print(result._result.get('module_stderr'))
        if ('stdout' in result._result) and result._result.get('stdout'):
            print('stdout:')
            print(result._result.get('stdout'))
        if ('stderr' in result._result) and result._result.get('stderr'):
            print('stderr:')
            print(result._result.get('stderr'))

    def v2_runner_on_failed(self, result, ignore_errors=False):
        if ('stdout' in result._result) and result._result.get('stdout'):
            print('stdout:')
            print(result._result.get('stdout'))
        if ('stderr' in result._result) and result._result.get('stderr'):
            print('stderr:')
            print(result._result.get('stderr'))

    def v2_runner_on_ok(self, result):
        if ('stdout' in result._result) and result._result.get('stdout'):
            print('stdout:')
            print(result._result.get('stdout'))
        if ('stderr' in result._result) and result._result.get('stderr'):
            print('stderr:')
            print(result._result.get('stderr'))
