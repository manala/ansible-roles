from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.module_utils.six import iteritems, string_types
from ansible.module_utils.parsing.convert_bool import boolean
from ansible.plugins.action import ActionBase
from ansible.errors import AnsibleError

import re

class ActionModule(ActionBase):

    TRANSFERS_FILES = False

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()

        result = super(ActionModule, self).run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        facts = dict()

        cacheable = boolean(self._task.args.pop('cacheable', False))

        args = {
            'hashes': self._task.args.get('hashes'),
            'prefix': self._task.args.get('prefix', ''),
            'var':    self._task.args.get('var')
        }

        if not isinstance(args['hashes'], list):
            raise AnsibleError('Invalid hashes. Expected a list, received a %s.' % type(args['hashes']))

        if not isinstance(args['prefix'], string_types):
            raise AnsibleError('Invalid prefix. Expected a string, received a %s.' % type(args['prefix']))

        if args['var'] is not None and not isinstance(args['var'], string_types):
            raise AnsibleError('Invalid var. Expected a string, received a %s.' % type(args['var']))

        hashes = []

        # Resolve hashes references
        for hash in args['hashes']:
            if isinstance(hash, string_types):
                for key, value in iteritems(task_vars):
                    if re.search('^' + hash + '$', key):
                        hashes.append(value)
            else:
                hashes.append(hash)

        for hash in hashes:
            for fact_key, fact_value in iteritems(hash):
                fact_key = args['prefix'] + fact_key
                fact_value = self._templar.template(fact_value, fail_on_undefined=False)
                if (fact_key in facts) and (isinstance(facts[fact_key], list) and isinstance(fact_value, list)):
                    facts[fact_key] += fact_value
                elif (fact_key in facts) and (isinstance(facts[fact_key], dict) and isinstance(fact_value, dict)):
                    facts[fact_key].update(fact_value)
                else:
                    facts[fact_key] = fact_value

        # Merge with task_vars
        for fact_key, fact_value in iteritems(facts):
            if (fact_key in task_vars):
                task_var_value = self._templar.template(task_vars[fact_key], fail_on_undefined=False)
                if isinstance(task_var_value, list) and isinstance(fact_value, list):
                    facts[fact_key] = task_var_value + fact_value
                elif isinstance(task_var_value, dict) and isinstance(fact_value, dict):
                    task_var_value.update(fact_value)
                    facts[fact_key] = task_var_value

        if args['var']:
            facts = {args['var']: facts}

        result['changed'] = False
        result['ansible_facts'] = facts
        result['_ansible_facts_cacheable'] = cacheable

        return result
