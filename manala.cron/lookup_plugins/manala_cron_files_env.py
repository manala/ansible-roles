from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        files = self._flatten(terms[0])

        for file in files:

            if file.has_key('env'):
                env = file.get('env')

                # Env must be a dict
                if not isinstance(env, dict):
                    raise AnsibleError('Expected a dict')

                for name,value in env.iteritems():

                    if not isinstance(value, (basestring, int, float)) or isinstance(value, bool):
                        raise AnsibleError("Expected a string, an integer or a float for key \"%s\" in manala_cron_files env" % name)

                    item = {
                        'file': file.get('file'),
                        'name': name,
                        'value': value
                    }

                    if file.has_key('user'):
                        item['user'] = file.get('user')

                    results.append(item)

        return results
