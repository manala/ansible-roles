from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        items = []

        for term in self._flatten(terms):

            # Normalize term as dict
            if isinstance(term, basestring):
                term = {
                    'package': term
                }

            # Check index key
            if not term.has_key('package'):
                raise AnsibleError('Expect "package" key')

            # Merge by index key
            termFound = False
            for i, item in enumerate(items):
                if item['package'] == term['package']:
                    items[i] = term
                    termFound = True
                    break

            if not termFound:
                items.append(term)

        return items
