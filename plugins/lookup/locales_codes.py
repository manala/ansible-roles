# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
    name: locales_codes
    author: Manala (@manala)
    short_description: returns a curated codes list
    description:
      - Takes a repositories list and returns it curated and optionally state or denormalized filtered.
    options:
      wantstatecurrent:
        description: filter list items by state current
      wantcodedenormalized:
        description: filter list items by code denormalized
'''

from ansible.plugins.lookup import LookupBase
from ansible.module_utils.six import string_types
from ansible.errors import AnsibleError

# As seen on native locale_gen module
LOCALE_NORMALIZATION = {
    ".utf8": ".UTF-8",
    ".eucjp": ".EUC-JP",
    ".iso885915": ".ISO-8859-15",
    ".cp1251": ".CP1251",
    ".koi8r": ".KOI8-R",
    ".armscii8": ".ARMSCII-8",
    ".euckr": ".EUC-KR",
    ".gbk": ".GBK",
    ".gb18030": ".GB18030",
    ".euctw": ".EUC-TW",
}


class LookupModule(LookupBase):

    # As seen on native locale_gen module
    def normalize(self, name):
        """locale -a might return the encoding in either lower or upper case.
        Passing through this function makes them uniform for comparisons."""
        for s, r in LOCALE_NORMALIZATION.items():
            name = name.replace(s, r)
        return name

    def denormalize(self, name):
        """locale -a might return the encoding in either lower or upper case.
        Passing through this function makes them uniform for comparisons."""
        for s, r in LOCALE_NORMALIZATION.items():
            name = name.replace(r, s)
        return name

    def run(self, terms, variables=None, **kwargs):

        results = []

        wantstatecurrent = kwargs.pop('wantstatecurrent', False)
        wantcodedenormalized = kwargs.pop('wantcodedenormalized', False)

        codes = self._flatten(terms[0])
        codesPresents = self._flatten(terms[1])

        itemDefault = {
            'state': 'present'
        }

        for code in codes:

            items = []

            # Short syntax
            if isinstance(code, string_types):
                item = itemDefault.copy()
                item.update({
                    'code': code
                })
            else:

                # Must be a dict
                if not isinstance(code, dict):
                    raise AnsibleError('Expected a dict but was a %s' % type(code))

                # Check index key
                if 'code' not in code:
                    raise AnsibleError('Missing "code" key')

                item = itemDefault.copy()
                item.update(code)

            item.update({
                'code': self.normalize(item['code'])
            })

            if wantcodedenormalized:
                codeDenormalized = self.denormalize(item['code'])
                if codeDenormalized != item['code']:
                    item.update({
                        'code_denormalized': self.denormalize(item['code'])
                    })

            if wantstatecurrent:
                item.update({
                    'state_current': 'present' if any(item['code'] == self.normalize(code) for code in codesPresents) else 'absent'
                })

            items.append(item)

            # Merge by index key
            for item in items:
                itemFound = False
                for i, result in enumerate(results):
                    if result['code'] == item['code']:
                        results[i] = item
                        itemFound = True
                        break

                if not itemFound:
                    results.append(item)

        return results
