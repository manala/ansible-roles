from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.action import ActionBase

import os


class FailedException(Exception):
    def __init__(self, result):
        self.result = result


class ActionModule(ActionBase):

    TRANSFERS_FILES = False

    def _run_module(self, name, args, task_args=None, task_vars=None):
        task_args = task_args or []
        task_vars = task_vars or {}

        # Relevant task args
        for key in task_args:
            if key in self._task.args:
                args[key] = self._task.args[key]
        # Action
        if name in ['ansible.builtin.template', 'ansible.builtin.copy']:
            task = self._task.copy()
            task.args = args
            action = self._shared_loader_obj.action_loader.get(
                name,
                task=task,
                connection=self._connection,
                play_context=self._play_context,
                loader=self._loader,
                templar=self._templar,
                shared_loader_obj=self._shared_loader_obj)
            result = action.run(task_vars=task_vars)
        else:
            result = self._execute_module(
                module_name=name,
                module_args=args,
                task_vars=task_vars)
        if result.get('failed'):
            raise FailedException(result)
        return result

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()

        result = super(ActionModule, self).run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        path = self._task.args.get('path')
        state = self._task.args.get('state', 'file')

        result['changed'] = False
        result['diff'] = []

        try:

            # Absent
            if (state == 'absent' and (
                    'template' in self._task.args
                    or 'content' in self._task.args
                    or 'copy' in self._task.args)):
                return self._run_module(
                    'ansible.builtin.file',
                    {'path': path, 'state': 'absent'},
                    task_vars=task_vars)

            # Parents
            if (self._task.args.get('parents') and (
                    'template' in self._task.args
                    or 'content' in self._task.args
                    or state == 'link'
                    or state == 'file')):
                parents_result = self._run_module(
                    'ansible.builtin.file',
                    {'path': os.path.dirname(path), 'state': 'directory'},
                    task_args=['owner', 'group', 'mode'],
                    task_vars=task_vars)
                result['changed'] |= parents_result['changed']
                result['diff'] += [parents_result['diff']]

            ############
            # Template #
            ############

            if 'template' in self._task.args:

                # Template
                template_result = self._run_module(
                    'ansible.builtin.template',
                    {'dest': path, 'src': self._task.args.get('template')},
                    task_args=['force', 'owner', 'group', 'mode'],
                    task_vars=task_vars)
                result['changed'] |= template_result['changed']
                result['diff'] += template_result['diff']

            ###########
            # Content #
            ###########

            elif 'content' in self._task.args:

                # Content
                content_result = self._run_module(
                    'ansible.builtin.copy',
                    {'dest': path, 'content': self._task.args.get('content')},
                    task_args=['force', 'owner', 'group', 'mode'],
                    task_vars=task_vars)
                result['changed'] |= content_result['changed']
                result['diff'] += content_result['diff']

            ########
            # Copy #
            ########

            elif 'copy' in self._task.args:

                result = self._run_module(
                    'ansible.builtin.copy',
                    {'dest': path, 'src': self._task.args.get('copy')},
                    task_args=['force', 'owner', 'group', 'mode'],
                    task_vars=task_vars)

            #######
            # Url #
            #######

            elif 'url' in self._task.args:

                # Url
                url_result = self._run_module(
                    'ansible.builtin.get_url',
                    {'dest': path, 'url': self._task.args.get('url')},
                    task_args=['validate_certs', 'force', 'owner', 'group', 'mode'],
                    task_vars=task_vars)
                result['changed'] |= url_result['changed']

                # Unarchive
                if self._task.args.get('unarchive', False) and not self._play_context.check_mode:
                    unarchive_result = self._run_module(
                        'ansible.builtin.unarchive',
                        {'src': path, 'dest': os.path.dirname(path), 'remote_src': True},
                        task_args=['creates'],
                        task_vars=task_vars)

            ########
            # Link #
            ########

            elif state == 'link':

                # Force
                if self._task.args.get('force'):
                    link_stat = self._execute_remote_stat(path, task_vars, follow=False)

                    if link_stat['exists'] and not link_stat['islnk']:
                        absent_result = self._run_module(
                            'ansible.builtin.file',
                            {'path': path, 'state': 'absent'},
                            task_vars=task_vars)
                        result['changed'] |= absent_result['changed']
                        result['diff'] += [absent_result['diff']]

                # Link
                link_result = self._run_module(
                    'ansible.builtin.file',
                    {'path': path, 'src': self._task.args.get('src'), 'state': 'link'},
                    task_args=['owner', 'group'],
                    task_vars=task_vars)
                result['changed'] |= link_result['changed']
                result['diff'] += link_result['diff']

            #############
            # Directory #
            #############

            elif state == 'directory':

                # Force
                if self._task.args.get('force'):
                    link_stat = self._execute_remote_stat(path, task_vars, follow=True)

                    if link_stat['exists'] and not link_stat['isdir']:
                        absent_result = self._run_module(
                            'ansible.builtin.file',
                            {'path': path, 'state': 'absent'},
                            task_vars=task_vars)
                        result['changed'] |= absent_result['changed']
                        result['diff'] += [absent_result['diff']]

                # Directory
                directory_result = self._run_module(
                    'ansible.builtin.file',
                    {'path': path, 'state': 'directory'},
                    task_args=['owner', 'group', 'mode'],
                    task_vars=task_vars)
                result['changed'] |= directory_result['changed']
                result['diff'] += directory_result['diff']

            ########
            # File #
            ########

            elif state == 'file':

                # Force
                if self._task.args.get('force'):
                    link_stat = self._execute_remote_stat(path, task_vars, follow=True)

                    if link_stat['exists'] and not link_stat['isreg']:
                        absent_result = self._run_module(
                            'ansible.builtin.file',
                            {'path': path, 'state': 'absent'},
                            task_vars=task_vars)
                        result['changed'] |= absent_result['changed']
                        result['diff'] += [absent_result['diff']]

                # Create
                create_result = self._run_module(
                    'ansible.builtin.copy',
                    {'dest': path, 'content': '', 'force': False},
                    task_args=['owner', 'group', 'mode'],
                    task_vars=task_vars)
                result['changed'] |= create_result['changed']

                # File
                file_result = self._run_module(
                    'ansible.builtin.file',
                    {'path': path, 'state': 'file'},
                    task_args=['owner', 'group', 'mode'],
                    task_vars=task_vars)
                result['changed'] |= file_result['changed']
                result['diff'] += file_result['diff']

            # Other...
            else:

                result = self._run_module(
                    'ansible.builtin.file',
                    {'path': path},
                    task_args=['state', 'follow', 'recurse', 'src', 'force', 'owner', 'group', 'mode'],
                    task_vars=task_vars)

            return result

        except FailedException as failed:
            return failed.result
