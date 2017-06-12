#!/usr/bin/python

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

    facts = dict()

    for key, value in hash.iteritems():
        if prefix:
            facts[prefix + key] = hash[key]
        else:
            facts[key] = hash[key]


    # Handle var if provided
    if var:
        facts = { var: facts }

    module.exit_json(ansible_facts=facts)

# Import module snippets
from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()
