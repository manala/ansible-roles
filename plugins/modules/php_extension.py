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
    cmd = 'phpquery -V'
    rc, out, err = module.run_command(cmd, check_rc=True)
    php_versions = out.splitlines()

    for php_version in php_versions:
        # Get sapis by version
        cmd = 'phpquery -v %s -S' % php_version
        rc, out, err = module.run_command(cmd, check_rc=True)
        php_sapis = out.splitlines()

        for php_sapi in php_sapis:
            cmd = 'phpquery -v %s -s %s -m %s' % (php_version, php_sapi, name)
            rc, out, err = module.run_command(cmd)
            if rc not in [0, 32]:
                module.fail_json(msg='Unable to query php extension state', cmd=cmd, rc=rc, stdout=out, stderr=err)

            # rc 0 -> extension already enabled
            # rc 32 -> extension already disabled
            if (rc == 0 and not enabled) or (rc == 32 and enabled):
                if module.check_mode:
                    module.exit_json(**result)
                result['changed'] = True
                cmd = 'php%smod -v %s -s %s %s' % ('en' if enabled else 'dis', php_version, php_sapi, name)
                module.run_command(cmd)

    module.exit_json(**result)


if __name__ == '__main__':
    main()
