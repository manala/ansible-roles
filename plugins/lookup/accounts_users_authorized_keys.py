# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
    name: accounts_users_authorized_keys
    author: Manala (@manala)
    short_description: returns a curated users authorized keys list
    description:
      - Takes a users authorized keys list and returns it curated.
'''

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError
from ansible.module_utils.six import string_types

import os.path


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        variables = variables or {}

        results = []

        users = self._flatten(terms)

        itemDefault = {}

        for user in users:

            # Must be a dict
            if not isinstance(user, dict):
                continue

            # Check index key
            if 'user' not in user:
                raise AnsibleError('Missing "user" key')

            # Mandatory field
            if 'authorized_keys' not in user:
                continue

            items = []

            item = itemDefault.copy()
            item.update(user)
            item.update({
                'authorized_keys': '\n'.join(user['authorized_keys']),
            })

            # File
            if 'authorized_keys_file' in user:
                # Empty
                if not user.get('authorized_keys_file'):
                    item.pop("authorized_keys_file")
                # Omit
                elif user.get('authorized_keys_file') == variables.get('omit'):
                    item.pop("authorized_keys_file")
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

        return results
