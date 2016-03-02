from ansible.plugins.lookup import LookupBase
from ansible.template import Templar

import re

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        keys = []

        # Search variable name by patterns
        for pattern in terms[0]:
            for variable in variables.keys():
                if re.search('^' + pattern + '$', variable):
                    keys.append(variable)

        result = {}

        # Merge
        for key in keys:
            for (resultKey, resultValue) in variables[key].items():
                if (resultKey in result) and isinstance(resultValue, (list, tuple)):
                    result[resultKey] = result[resultKey] + resultValue
                else:
                    result[resultKey] = resultValue

        templar = Templar(variables=variables, loader=self._loader)
        result = templar.template(result, fail_on_undefined=False)

        return result
