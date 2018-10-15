from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.module_utils.six import string_types
from ansible.errors import AnsibleError

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        for term in self._flatten(terms):

            # Normalize term as dict
            if isinstance(term, string_types):
                term = {
                    'package': term
                }

            # Check index key
            if 'package' not in term:
                raise AnsibleError('Expect "package" key')

            # Merge by index key
            termFound = False
            for i, result in enumerate(results):
                if result['package'] == term['package']:
                    results[i] = term
                    termFound = True
                    break

            if not termFound:
                results.append(term)

        return results
