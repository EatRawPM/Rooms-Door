from os.path import exists
from os import mkdir
from src.assets.options.options import init_options
from src.lang import init_lang
from src.data.path import main_path, options_path, main_assets_path, packages_path, lang_path, assets_packages_path, lang_packages_path, texture_path, model_path
from src.assets.options.create import create_options
from src.assets.package.create import create_package
from src.assets.assets.package.create import create_assets_package
from src.assets.assets.lang.package.create import create_assets_lang_package
from src.assets.assets.lang.set import set_langs

def init_data():
    def main():
        def package():
            if exists(packages_path):
                print(f'Data: {packages_path} already exists.')
            else:
                print(f'Data: {packages_path} is created.')
                with open(packages_path, 'w', encoding='utf-8') as f:
                    create_package(f)
        def options():
            if exists(options_path):
                print(f'Data: {options_path} already exists.')
            else:
                print(f'Data: {options_path} is created.')
                with open(options_path, 'w', encoding='utf-8') as f:
                    create_options(f)
        def assets():
            def assets_package():
                if exists(assets_packages_path):
                    print(f'Data: {assets_packages_path} already exists.')
                else:
                    print(f'Data: {assets_packages_path} is created.')
                    with open(assets_packages_path, 'w', encoding='utf-8') as f:
                        create_assets_package(f)
            def lang():
                def assets_lang_package():
                    if exists(lang_packages_path):
                        print(f'Data: {lang_packages_path} already exists.')
                    else:
                        print(f'Data: {lang_packages_path} is created.')
                        with open(lang_packages_path, 'w', encoding='utf-8') as f:
                            create_assets_lang_package(f)
                def langs():
                    set_langs()

                if exists(lang_path):
                    print(f'Data: {lang_path} already exists.')
                    assets_lang_package()
                    langs()
                else:
                    mkdir(lang_path)
                    print(f'Data: {lang_path} is created.')
                    assets_lang_package()
                    langs()
            def texture():
                if exists(texture_path):
                    print(f'Data: {texture_path} already exists.')
                else:
                    mkdir(texture_path)
                    print(f'Data: {texture_path} is created.')
            def model():
                if exists(model_path):
                    print(f'Data: {model_path} already exists.')
                else:
                    mkdir(model_path)
                    print(f'Data: {model_path} is created.')

            if exists(main_assets_path):
                print(f'Data: {main_assets_path} already exists.')
                assets_package()
                lang()
                texture()
                model()
            else:
                mkdir(main_assets_path)
                print(f'Data: {main_assets_path} is created.')
                assets_package()
                lang()
                texture()
                model()

        if exists(main_path):
            print(f'Data: {main_path} already exists.')
            package()
            options()
            assets()
        else:
            mkdir(main_path)
            print(f'Data: {main_path} is created.')
            package()
            options()
            assets()
    
    main()
    init_options()
    init_lang()