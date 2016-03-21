#!/usr/bin/python

def main():

    module = AnsibleModule(
        argument_spec = dict(
            vars = dict(required=True)
        )
    )

    result = {
        'ansible_facts': module.params['vars']
    }

    module.exit_json(**result)

# Import module snippets
from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()
