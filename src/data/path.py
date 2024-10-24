from os.path import join, dirname, realpath
from sys import argv
from src.console import DataPath

#assets

base_path = dirname(realpath(argv[0])) if not DataPath else DataPath

assets_path = join(base_path, 'assets')

fonts_path = join(assets_path, 'fonts')

#data

main_path = join(base_path, '.rooms&doors')

packages_path = join(main_path, 'package.json')

options_path = join(main_path,'options.json')

main_assets_path = join(main_path, 'assets')

assets_packages_path = join(main_assets_path, 'package.json')

lang_path = join(main_assets_path, 'lang')

lang_packages_path = join(lang_path, 'package.json')