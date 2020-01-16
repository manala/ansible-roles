from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os.path

from ansible.plugins.lookup import LookupBase
from ansible.module_utils.six import string_types
from ansible.errors import AnsibleError

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        wantstate = kwargs.pop('wantstate', None)

        users = self._flatten(terms)

        for user in users:

            # Must be a dict
            if not isinstance(user, dict):
                raise AnsibleError('Expect a dict')

            # Check index key
            if 'user' not in user:
                raise AnsibleError('Expect "user" key')

            items = []

            if 'authorized_keys' in user:
                item = {
                    'user':            user.get('user'),
                    'authorized_keys': '\n'.join(user.get('authorized_keys')),
                    'state':           user.get('state', 'present'),
                }

                # File
                if 'authorized_keys_file' in user and user.get('authorized_keys_file'):
                    # Omit
                    if user.get('authorized_keys_file') == variables['omit']:
                        pass
                    # Path
                    elif isinstance(user.get('authorized_keys_file'), string_types):
                        # Absolute
                        if user.get('authorized_keys_file').startswith('/'):
                            item.update({
                                'authorized_keys_file': user.get('authorized_keys_file')
                            })
                        # Relative
                        else:
                            item.update({
                                'authorized_keys_file': os.path.expanduser('~' + user.get('user') + '/.ssh/' + user.get('authorized_keys_file'))
                            })

                items.append(item)

            # Merge by index key
            for item in items:
                itemFound = False
                for i, result in enumerate(results):
                    if result['user'] == item['user']:
                        results[i] = item
                        itemFound = True
                        break

                if not itemFound:
                    results.append(item)

        # Filter by state
        if wantstate:
            results = [result for result in results if result.get('state') == wantstate]

        return results
