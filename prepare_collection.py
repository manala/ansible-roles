#!/usr/bin/env python3

import os
import shutil
import glob
import re
import logging

logging.basicConfig(level=logging.INFO)

collection_dir = 'collection'

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

for plugins_dir in ['lookup', 'callback', 'filter', 'modules']:
	plugins_dir = os.path.join(collection_dir, 'plugins', plugins_dir)
	logging.info('Create plugins dir "%s"', plugins_dir)
	os.makedirs(plugins_dir)

#########
# Roles #
#########

dir = os.path.join(collection_dir, 'roles')

for role in glob.glob('roles/*'):
	role = os.path.basename(role)
	# Path
	role_path = os.path.join(dir, role)
	logging.info('Create role path "%s"', role_path)
	os.makedirs(role_path)
	# Files
	for role_file in ['CHANGELOG.md', 'README.md']:
		src = os.path.join('roles', role, role_file)
		if os.path.isfile(src):
			shutil.copy(
				src,
				os.path.join(role_path, role_file)
			)
	# Dirs
	for role_dir in ['defaults', 'files', 'handlers', 'meta', 'tasks', 'templates', 'vars']:
		src = os.path.join('roles', role, role_dir)
		if os.path.isdir(src):
			shutil.copytree(
				src,
				os.path.join(role_path, role_dir)
			)
	# Plugins
	for plugins in [
		{'src': 'lookup_plugins', 'dst': 'lookup'},
		{'src': 'callback_plugins', 'dst': 'callback'},
		{'src': 'filter_plugins', 'dst': 'filter'},
		{'src': 'library', 'dst': 'modules'}
	]:
		for src in glob.glob(os.path.join('roles', role, plugins['src'], '*.py')):
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
	files.extend(glob.glob(os.path.join(role_path, 'handlers/**/*.yml'), recursive=True))
	files.extend(glob.glob(os.path.join(role_path, 'tasks/**/*.yml'), recursive=True))
	files.extend(glob.glob(os.path.join(role_path, 'templates/**/*.j2'), recursive=True))
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
	files.extend(glob.glob(os.path.join(role_path, 'templates/**/*.j2'), recursive=True))
	regex = re.compile(r'(\|\s*)manala_', re.DOTALL)
	for file_path in files:
		with open(file_path, 'r+') as file:
			file_data = file.read()
			if len(re.findall(regex, file_data)):
				logging.info('Apply filter regex into file "%s"', file_path)
				file.seek(0)
				file.write(re.sub(regex, r'\1manala.roles.', file_data))
				file.truncate()
