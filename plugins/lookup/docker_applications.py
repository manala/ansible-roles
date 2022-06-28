# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
    name: docker_applications
    author: Manala (@manala)
    short_description: returns a curated applications list
    description:
      - Takes a repositories list and returns it curated.
'''

from ansible.plugins.lookup import LookupBase
from ansible.module_utils.six import string_types
from ansible.errors import AnsibleError


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        results = []

        applications = self._flatten(terms[0])
        patterns = terms[1]

        itemDefault = {
            'tag': None,
            'rm': None,
            'interactive': None,
            'tty': None,
            'command': None,
            'volumes': {},
            'environment': {},
            'workdir': None
        }

        for application in applications:

            items = []

            # Short syntax
            if isinstance(application, string_types):
                item = itemDefault.copy()

                item.update({
                    'image': application.split(':')[0],
                    'application': ((application.split('/')[1]).split(':')[0]) if len(application.split('/')) > 1 else (application.split(':')[0])
                })

                # Pattern
                if application.split(':')[0] in patterns:
                    item.update(patterns.get(application.split(':')[0]))

                # Tag
                if len(application.split(':')) > 1:
                    item.update({
                        'tag': application.split(':')[1]
                    })
            else:

                # Must be a dict
                if not isinstance(application, dict):
                    raise AnsibleError('Expected a dict but was a %s' % type(application))

                # Check index key
                if 'application' not in application:
                    raise AnsibleError('Missing "application" key')

                item = itemDefault.copy()

                item.update(application)

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
