from ansible.plugins.lookup import LookupBase
from ansible.template import Templar

import re

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        hashes = []

        for hash in terms[0]:
            if isinstance(hash, basestring):
                for key, value in variables.iteritems():
                    if re.search('^' + hash + '$', key):
                        hashes.append(value)
            else:
                hashes.append(hash)

        result = {}

        templar = Templar(variables=variables, loader=self._loader)

        # Merge
        for hash in hashes:
            for resultKey, resultValue in hash.iteritems():
                resultValue = templar.template(resultValue, fail_on_undefined=False)
                if (resultKey in result) and isinstance(resultValue, (list, tuple)):
                    result[resultKey] = result[resultKey] + resultValue
                else:
                    result[resultKey] = resultValue

        return result
