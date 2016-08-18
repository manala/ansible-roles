from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

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
            for i, result in enumerate(results):
                if result['package'] == term['package']:
                    results[i] = term
                    termFound = True
                    break

            if not termFound:
                results.append(term)

        return results
