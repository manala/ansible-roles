from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.module_utils.six import string_types, iteritems
from ansible.errors import AnsibleError


class LookupModule(LookupBase):

    def format_row(self, key, value, type):
        result = ''
        if type == 'array':
            if not isinstance(value, list):
                raise AnsibleError('Expected a list for key "%s" in manala_backup_manager config' % key)
            for index, val in enumerate(value):
                if not isinstance(val, dict):
                    raise AnsibleError('Expected a dict for key "%s" values in manala_backup_manager config' % key)
                for k, v in iteritems(val):
                     result += "%s_%s[%d]=\"%s\"\n" % (key, k, index, v)
        return result

    def run(self, terms, variables=None, **kwargs):

        wantrow = kwargs.pop('wantrow', None)
        wantrowtype = kwargs.pop('wantrowtype', None)
        wantrowdefault = kwargs.pop('wantrowdefault', None)

        config = self._flatten(terms)

        for row in config:
            for key, value in iteritems(row):
                if key == wantrow:
                    return self.format_row(key, value, wantrowtype)

        if wantrowdefault:
            return wantrowdefault
