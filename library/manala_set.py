#!/usr/bin/python

from ansible.compat.six import iteritems, string_types

def main():

    module = AnsibleModule(
        argument_spec = dict(
            hash = dict(required=True, type='dict'),
            prefix = dict(required=False, type='str'),
            var = dict(required=False, type='str')
        )
    )

    prefix = module.params.get('prefix')
    hash   = module.params.get('hash')
    var    = module.params.get('var')

    # Handle prefix if provided
    if prefix:
        for key, value in iteritems(hash):
            hash.pop(key)
            hash[prefix + key] = value

    # Handle var if provided
    if var:
        hash = { var: hash }

    result = {
        'ansible_facts': hash
    }

    module.exit_json(**result)

# Import module snippets
from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()
