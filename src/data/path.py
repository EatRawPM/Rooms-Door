from os.path import join, dirname, realpath
from sys import argv
from src.console import DataPath

#assets

base_path = dirname(realpath(argv[0])) if not DataPath else DataPath

assets_path = join(base_path, 'assets')

fonts_path = join(assets_path, 'fonts')

lang_path = join(assets_path, 'lang')

#data

main_path = join(base_path, '.rooms&doors')

options_path = join(main_path,'options.json')

assets__path = join(main_path, 'assets')