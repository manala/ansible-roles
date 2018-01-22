from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError

class LookupModule(LookupBase):

    def legacy_format_value(self, value):
        if (value is None):
            return 'null'
        elif (value is True):
            return 'true'
        elif (value is False):
            return 'false'
        else:
            return value

    def run(self, terms, variables=None, **kwargs):

        results = []

        if isinstance(terms[0], dict):
            for name, value in terms[0].iteritems():
                if not isinstance(value, (basestring, int, float)) or isinstance(value, bool):
                    raise AnsibleError("Expected a string, an integer or a float for key \"%s\" in manala_environment_variables" % name)
                results.append({
                    'name':  name,
                    'value': value
                })
        else:
            # Legacy
            for term in self._flatten(terms):

                # Term must be a dict
                if not isinstance(term, dict):
                    raise AnsibleError('Expect a dict')

                items = []

                if term.has_key('name') and term.has_key('value'):
                    # Expanded syntax
                    items.append({
                        'name':  term.get('name'),
                        'value': self.legacy_format_value(term.get('value'))
                    })
                else:
                    # Short syntax
                    items.append({
                        'name':  term.keys()[0],
                        'value': self.legacy_format_value(term.values()[0])
                    })

                # Merge by index key
                for item in items:
                    itemFound = False
                    for i, result in enumerate(results):
                        if result['name'] == item['name']:
                            results[i] = item
                            itemFound = True
                            break
                    if not itemFound:
                        results.append(item)

        return results
