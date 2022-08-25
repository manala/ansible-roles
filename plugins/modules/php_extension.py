#!/usr/bin/python

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: php_extension
author: Manala (@manala)
short_description: Manage php extension
description: Manage php extension

options:
    name:
        description: Extension name.
        required: true
        type: str
    enabled:
        description: Whether the extension should be enabled.
        required: true
        type: bool
'''

EXAMPLES = r'''
- name: Enable php xdebug extension
  manala.roles.php_extension:
    name: xdebug
    enabled: true
'''

from ansible.module_utils.basic import AnsibleModule


def main():

    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True),
            enabled=dict(type='bool', required=True),
        ),
        supports_check_mode=True
    )

    result = module.params
    result['changed'] = False

    name = module.params['name']
    enabled = module.params['enabled']

    # Get versions
    rc, out, err = run_phpquery(module, '-V')
    php_versions = out.splitlines()

    for php_version in php_versions:
        # Get sapis by version
        rc, out, err = run_phpquery(module, '-v %s -S' % php_version)
        php_sapis = out.splitlines()

        for php_sapi in php_sapis:
            args = '-v %s -s %s -m %s' % (php_version, php_sapi, name)
            rc, out, err = run_phpquery(module, args)
            if rc not in [0, 32]:
                module.fail_json(msg='Unable to query php extension state', args=args, rc=rc, stdout=out, stderr=err)

            # rc 0 -> extension already enabled
            # rc 32 -> extension already disabled
            if (rc == 0 and not enabled) or (rc == 32 and enabled):
                if module.check_mode:
                    module.exit_json(**result)
                result['changed'] = True
                args = '-v %s -s %s %s' % (php_version, php_sapi, name)
                if enabled:
                    run_phpenmod(module, args)
                else:
                    run_phpdismod(module, args)

    module.exit_json(**result)


def run_phpquery(module, args):
    return module.run_command('phpquery %s' % args, check_rc=False)


def run_phpenmod(module, args):
    return module.run_command('phpenmod %s' % args, check_rc=True)


def run_phpdismod(module, args):
    return module.run_command('phpdismod %s' % args, check_rc=True)


if __name__ == '__main__':
    main()
