from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.errors import AnsibleFilterError
from ansible.module_utils.common._collections_compat import Iterable


def users_groups(users, groups=None):
    if not isinstance(users, Iterable):
        raise AnsibleFilterError('Expected an iterable but was a %s' % type(users))
    groups = groups or []
    if not isinstance(groups, Iterable):
        raise AnsibleFilterError('Expected a groups iterable but was a %s' % type(groups))

    results = []

    for user in users:
        for group in groups:
            if 'skipped' in group and group['skipped']:
                continue
            if group['item']['user'] == user['user']:
                user['group'] = group['stdout']
                break
        results.append(user)

    return results


class FilterModule(object):
    ''' Manala users groups filter '''

    def filters(self):
        filters = {
            'users_groups': users_groups,
        }

        return filters
