from ansible.plugins.lookup import LookupBase
from ansible.template import Templar
from ansible.module_utils.six import iteritems, string_types

import re

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        templar = Templar(variables=variables, loader=self._loader)

        hashes = []

        if isinstance(terms[0], string_types):
            terms[0] = terms[0].replace('[[', '{{').replace(']]', '}}')
            terms[0] = templar.template(terms[0])

        for hash in terms[0]:
            if isinstance(hash, string_types):
                for key, value in iteritems(variables):
                    if re.search('^' + hash + '$', key):
                        hashes.append(value)
            else:
                hashes.append(hash)

        result = {}

        # Merge
        for hash in hashes:
            for resultKey, resultValue in iteritems(hash):
                resultValue = templar.template(resultValue, fail_on_undefined=False)
                if (resultKey in result) and (isinstance(result[resultKey], list) and isinstance(resultValue, list)):
                    result[resultKey] = result[resultKey] + resultValue
                elif (resultKey in result) and (isinstance(result[resultKey], dict) and isinstance(resultValue, dict)):
                    result[resultKey].update(resultValue)
                else:
                    result[resultKey] = resultValue

        return result
