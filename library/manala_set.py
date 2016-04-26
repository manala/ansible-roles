#!/usr/bin/python

def main():

    module = AnsibleModule(
        argument_spec = dict(
            hash = dict(required=True),
            prefix = dict(required=False)
        )
    )

    prefix = module.params.get('prefix')
    hash   = module.params.get('hash')

    # Handle prefix if provided
    if prefix:
        for key, value in hash.items():
            hash.pop(key)
            hash[prefix + key] = value

    result = {
        'ansible_facts': hash
    }

    module.exit_json(**result)

# Import module snippets
from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()
