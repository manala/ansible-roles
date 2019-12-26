#!/usr/bin/env python3

import os
import shutil
import glob
import re


for paths in ['./plugins/lookup', './plugins/callback', './plugins/filter']:
	if not os.path.exists(paths):
		os.makedirs(paths)

for files in glob.glob('./roles/*/lookup_plugins/*.py'):
	shutil.move(files, './plugins/lookup')

for files in glob.glob('./roles/*/callback_plugins/*.py'):
	shutil.move(files, './plugins/callback')

for files in glob.glob('./roles/*/filter_plugins/*.py'):
	shutil.move(files, './plugins/filter')

for filename in glob.glob( "./plugins/*/*.py" ):
	new_name = re.sub(r'manala_', r'', filename)
	os.rename(filename, new_name)

for paths in ['./roles/*/*_plugins/',
			'./roles/*/.manala/',
			'./roles/*/.travis.yml',
			'./roles/*/Makefile',
			'./roles/*/.gitignore',
			'./roles/*/tests/',
			'./.env.dist',
			'./.gitsplit.yml',
			'./.travis.yml',
			'./README.md']:
	for path in glob.glob(paths):
		if os.path.isfile(path):
			os.remove(path)
		else:
			shutil.rmtree(path)

files = [f for f in glob.glob('./roles/*/tasks/*.yml', recursive=True)]
regex = re.compile(r'(query\(\s*\')manala_', re.DOTALL)

for file_path in files:
	with open(file_path, 'r+') as file:
		file_data = file.read()
		if len(re.findall(regex, file_data)):
			file.seek(0)
			file.write(re.sub(regex, r"\1manala.roles.", file_data))
			file.truncate
