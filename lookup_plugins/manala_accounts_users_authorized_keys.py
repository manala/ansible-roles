from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os.path

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        for term in self._flatten(terms):

            # Check index key
            if not term.has_key('user'):
                raise AnsibleError('Expect "user" key')

            items = []

            if term.has_key('authorized_keys'):
                item = {
                    'user':            term.get('user'),
                    'authorized_keys': '\n'.join(term.get('authorized_keys'))
                }

                # File
                if term.has_key('authorized_keys_file'):
                    # None
                    if term.get('authorized_keys_file') is None:
                        pass
                    # Omit
                    elif term.get('authorized_keys_file') == variables['omit']:
                        pass
                    # Path
                    elif isinstance(term.get('authorized_keys_file'), basestring):
                        # Absolute
                        if term.get('authorized_keys_file').startswith('/'):
                            item.update({
                                'authorized_keys_file': term.get('authorized_keys_file')
                            })
                        # Relative
                        else:
                            item.update({
                                'authorized_keys_file': os.path.expanduser('~' + term.get('user') + '/.ssh/' + term.get('authorized_keys_file'))
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
