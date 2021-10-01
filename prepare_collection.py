#!/usr/bin/env python3

import os
import shutil
import pathlib
import re
import logging

logging.basicConfig(level=logging.INFO)

collection_dir = 'collection'
meta_dir = os.path.join(collection_dir, 'meta')

#########
# Clean #
#########

logging.info('Remove collection dir "%s"', collection_dir)
if os.path.isdir(collection_dir):
	shutil.rmtree(collection_dir)

########
# Root #
########

logging.info('Create collection dir "%s"', collection_dir)
os.makedirs(collection_dir)

logging.info('Create collection dir "%s"', meta_dir)
os.makedirs(meta_dir)

logging.info('Copy runtime file into "%s"', meta_dir)
shutil.copyfile(
	'runtime.yml',
	os.path.join(meta_dir, 'runtime.yml')
)

logging.info('Copy galaxy file into "%s"', collection_dir)
shutil.copyfile(
	'galaxy.yml',
	os.path.join(collection_dir, 'galaxy.yml')
)

logging.info('Copy README file into "%s"', collection_dir)
shutil.copyfile(
	'README_COLLECTION.md',
	os.path.join(collection_dir, 'README.md')
)

for plugins_dir in ['lookup', 'callback', 'filter', 'modules', 'action']:
	plugins_dir = os.path.join(collection_dir, 'plugins', plugins_dir)
	logging.info('Create plugins dir "%s"', plugins_dir)
	os.makedirs(plugins_dir)

#########
# Roles #
#########

roles_dir = os.path.join(collection_dir, 'roles')

for role_path in pathlib.Path('roles').glob('*'):
	role = os.path.basename(role_path)
	role_dir = os.path.join(roles_dir, role)
	logging.info('Create role dir "%s"', role_dir)
	os.makedirs(role_dir)
	# Files
	for file in ['CHANGELOG.md', 'README.md']:
		file_src = os.path.join('roles', role, file)
		if os.path.isfile(file_src):
			shutil.copy(
				file_src,
				os.path.join(role_dir, file)
			)
	# Dirs
	for dir in ['defaults', 'files', 'handlers', 'meta', 'tasks', 'templates', 'vars']:
		dir_src = os.path.join('roles', role, dir)
		if os.path.isdir(dir_src):
			shutil.copytree(
				dir_src,
				os.path.join(role_dir, dir)
			)
	# Plugins
	for plugins in [
		{'src': 'lookup_plugins', 'dst': 'lookup'},
		{'src': 'callback_plugins', 'dst': 'callback'},
		{'src': 'filter_plugins', 'dst': 'filter'},
		{'src': 'library', 'dst': 'modules'},
		{'src': 'action_plugins', 'dst': 'action'}
	]:
		for src in pathlib.Path('roles', role, plugins['src']).glob('*.py'):
			# Copy
			dst = os.path.join(
				collection_dir,
				'plugins',
				plugins['dst'],
				re.sub(r'manala_', r'', os.path.basename(src))
			)
			logging.info('Copy plugin file "%s" into "%s"', src, dst)
			shutil.copyfile(src, dst)
			# Filters
			if plugins['src'] == 'filter_plugins':
				regex = re.compile(r'(\')manala_', re.DOTALL)
				with open(dst, 'r+') as file:
					file_data = file.read()
					if len(re.findall(regex, file_data)):
						logging.info('Apply filter regex into file "%s"', dst)
						file.seek(0)
						file.write(re.sub(regex, r'\1', file_data))
						file.truncate()
	# Lookups
	files = []
	files.extend(pathlib.Path(role_dir, 'handlers').rglob('*.yml'))
	files.extend(pathlib.Path(role_dir, 'tasks').rglob('*.yml'))
	files.extend(pathlib.Path(role_dir, 'templates').rglob('*.j2'))
	regex = re.compile(r'(query\(\s*\')manala_', re.DOTALL)
	for file_path in files:
		with open(file_path, 'r+') as file:
			file_data = file.read()
			if len(re.findall(regex, file_data)):
				logging.info('Apply lookup regex into file "%s"', file_path)
				file.seek(0)
				file.write(re.sub(regex, r'\1manala.roles.', file_data))
				file.truncate()
	# Filters
	files = []
	files.extend(pathlib.Path(role_dir, 'tasks').rglob('*.yml'))
	files.extend(pathlib.Path(role_dir, 'templates').rglob('*.j2'))
	files.extend(pathlib.Path(role_dir, 'vars').rglob('*.yml'))
	regex = re.compile(r'(\|\s*)manala_', re.DOTALL)
	for file_path in files:
		with open(file_path, 'r+') as file:
			file_data = file.read()
			if len(re.findall(regex, file_data)):
				logging.info('Apply filter regex into file "%s"', file_path)
				file.seek(0)
				file.write(re.sub(regex, r'\1manala.roles.', file_data))
				file.truncate()
	# Actions
	files = []
	files.extend(pathlib.Path(role_dir, 'tasks').rglob('*.yml'))
	regex = r"^(\s+)manala_(\S+:)$"
	for file_path in files:
		with open(file_path, 'r+') as file:
			file_data = file.read()
			if len(re.findall(regex, file_data, re.MULTILINE)):
				logging.info('Apply action regex into file "%s"', file_path)
				file.seek(0)
				file.write(re.sub(regex, "\\1manala.roles.\\2", file_data, 0, re.MULTILINE))
				file.truncate()
