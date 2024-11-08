from os.path import join, dirname, realpath
from sys import argv
from src.console import DataPath

#data

base_path = dirname(realpath(argv[0])) if not DataPath else DataPath

#assets

main_path = join(base_path, '.rooms&doors')

packages_path = join(main_path, 'package.json')

options_path = join(main_path,'options.json')

assets_path = join(main_path, 'assets')

assets_packages_path = join(assets_path, 'package.json')

fonts_path = join(assets_path, 'fonts')

lang_path = join(assets_path, 'lang')

lang_packages_path = join(lang_path, 'package.json')

texture_path = join(assets_path, 'texture')

model_path = join(assets_path, 'model')