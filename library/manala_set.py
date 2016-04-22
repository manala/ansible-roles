#!/usr/bin/python

def main():

    module = AnsibleModule(
        argument_spec = dict(
            vars = dict(required=True),
            prefix = dict(required=False)
        )
    )

    prefix = module.params.get('prefix')
    vars   = module.params.get('vars')

    # Handle prefix if provided
    if prefix:
        for key, value in vars.items():
            vars.pop(key)
            vars[prefix + key] = value

    result = {
        'ansible_facts': vars
    }

    module.exit_json(**result)

# Import module snippets
from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()
