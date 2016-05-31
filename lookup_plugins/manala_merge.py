from ansible.plugins.lookup import LookupBase
from ansible.template import Templar
from ansible.compat.six import iteritems, string_types

import re

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        hashes = []

        for hash in terms[0]:
            if isinstance(hash, string_types):
                for key, value in variables.iteritems():
                    if re.search('^' + hash + '$', key):
                        hashes.append(value)
            else:
                hashes.append(hash)

        result = {}

        templar = Templar(variables=variables, loader=self._loader)

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
