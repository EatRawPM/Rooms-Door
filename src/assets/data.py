from os.path import join, exists
from os import mkdir
from src.data.path import main_path, options_path, assets__path
from src.assets.options.create import create_options

def init_data():
    def main():
        def options():
            if exists(options_path):
                print(f'{options_path} already exists.')
            else:
                print(f'{options_path} is created.')
                with open(options_path, 'w', encoding='utf-8') as f:
                    create_options(f)
        def assets():
            if exists(assets__path):
                print(f'{assets__path} already exists.')
            else:
                mkdir(assets__path)
                print(f'{assets__path} is created.')
        
        if exists(main_path):
            print(f'{main_path} already exists.')
            options()
            assets()
        else:
            mkdir(main_path)
            print(f'{main_path} is created.')
            options()
            assets()
    
    main()