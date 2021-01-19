from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError
from ansible.module_utils.six import string_types
from ansible.module_utils._text import to_text


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        wantstate = kwargs.pop('wantstate', None)

        if wantstate and wantstate not in ['present']:
            raise AnsibleError('Expect a wanstate of "present" but was "%s"' % to_text(wantstate))

        applications = self._flatten(terms[0])
        patterns = terms[1]

        itemDefault = {
            'state': 'present',
            'version': None,
            'source': None,
            'source_version': None
        }

        for application in applications:

            items = []

            # Short syntax
            if isinstance(application, string_types):
                item = itemDefault.copy()

                # Pattern
                if application.split('@')[0] not in patterns:
                    raise AnsibleError('Unknown "%s" pattern' % application.split('@')[0])

                item.update(patterns.get(application.split('@')[0]))

                item.update({
                    'application': application.split('@')[0],
                    'version': application.split('@')[1] if (len(application.split('@')) > 1) else None
                })

            else:

                # Must be a dict
                if not isinstance(application, dict):
                    raise AnsibleError('Expect a dict but was a %s' % type(application))

                # Check index key
                if 'application' not in application:
                    raise AnsibleError('Expect an "application" key')

                item = itemDefault.copy()

                # Pattern
                if application['application'] in patterns:
                    item.update(patterns.get(application['application']))

                item.update(application)

            # Source version
            if item.get('source_version') and item.get('version'):
                item.update({
                    'source': item.get('source_version').format(version=item.get('version'))
                })

            # No source
            if not item.get('source'):
                raise AnsibleError('No source')

            if item['state'] not in ['present', 'ignore']:
                raise AnsibleError('Expect a state of "present" or "ignore" but was "%s"' % to_text(item['state']))

            if item['state'] == 'ignore':
                continue

            items.append(item)

            # Merge by index key
            for item in items:
                itemFound = False
                for i, result in enumerate(results):
                    if result['application'] == item['application']:
                        results[i] = item
                        itemFound = True
                        break

                if not itemFound:
                    results.append(item)

        return results
