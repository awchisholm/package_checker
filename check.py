import importlib
packages = ['pandas', 'matplotlib', 'numpy', 'pygame', 'flask', 'django', 'requests', 'scipy']
for package in packages:
	try:
		var = importlib.import_module(package)
		print('Package ' + package + ' OK')
	except ModuleNotFoundError:
		print('Package ' + package + ' not found')
