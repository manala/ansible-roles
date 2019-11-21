#!/usr/bin/env python3

import os
import shutil
import glob
import re

if not os.path.exists('./plugins/lookup'):
    os.makedirs('./plugins/lookup')

for files in glob.glob('./roles/*/*_plugins/*.py'):
	shutil.move(files, './plugins/lookup')

for filename in glob.glob( "./plugins/lookup/*.py" ):
	new_name = re.sub(r'manala_', r'', filename)
	os.rename(filename, new_name)

for path in ['./roles/*/*_plugins/',
			#'./roles/*/.manala/',
			#'./.manala/',
			'./roles/*/.travis.yml',
			'./roles/*/Makefile',
			'./Makefile',
			'./roles/*/.gitignore',
			'./roles/*/tests/']:
	for path2 in glob.glob(path):
		if os.path.isfile(path2):
			os.remove(path2)
		else:
			shutil.rmtree(path2)

files = [f for f in glob.glob('./roles/*/tasks/*.yml', recursive=True)]
regex = re.compile(r'(lookup\(\s*\')manala_', re.DOTALL)

for file_path in files:
	with open(file_path, 'r+') as file:
		file_data = file.read()
		if len(re.findall(regex, file_data)):
			file.seek(0)
			file.write(re.sub(regex, r"\1manala.roles.", file_data))
			file.truncate
