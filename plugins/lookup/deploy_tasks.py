# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
    name: deploy_tasks
    author: Manala (@manala)
    short_description: returns a curated tasks list
    description:
      - Takes a tasks list and returns it curated.
'''

from ansible.plugins.lookup import LookupBase
from ansible.module_utils.six import string_types
from ansible.errors import AnsibleError


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        variables = variables or {}

        results = []

        tasks = self._flatten(terms)

        itemDefault = {
            'options': None,
            'when': True,
            'dir':
                (
                    variables['deploy_helper'].get('new_release_path')
                ) if 'deploy_helper' in variables else (
                    variables.get('manala_deploy_dir', '') + '/' + variables.get('manala_deploy_current_dir', '')
                ),
            'shared_dir':
                (
                    variables['deploy_helper'].get('shared_path')
                ) if 'deploy_helper' in variables else (
                    variables.get('manala_deploy_dir', '') + '/' + variables.get('manala_deploy_shared_dir', '')
                )
        }

        for task in tasks:

            items = []

            # Short syntax
            if isinstance(task, string_types):
                item = itemDefault.copy()
                item.update({
                    'task': task
                })
                items.append(item)
            else:

                # Must be a dict
                if not isinstance(task, dict):
                    raise AnsibleError('Expected a dict but was a %s' % type(task))

                # Guess task (first one not in blacklist)
                item = None
                for taskKey, taskValue in task.items():
                    if taskKey not in ['when']:
                        item = itemDefault.copy()
                        item.update({
                            'task': taskKey,
                            'options': taskValue
                        })
                        break
                if item:
                    item.update({
                        'when': task.get('when') if 'when' in task else True
                    })
                    items.append(item)

            # Merge
            for item in items:
                results.append(item)

        return results
