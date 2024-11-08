from os.path import exists
from os import mkdir

from src.assets.assets.icon import icon_path
from src.assets.assets.images.path import images_path
from src.data.assets.images.icon.create import create_icon
from src.data.options import init_options
from src.lang import init_lang
from src.assets import main_path, options_path, assets_path, packages_path, lang_path, assets_packages_path, lang_packages_path, texture_path, model_path, fonts_path
from src.data.options.create import create_options
from src.data.package.create import create_package
from src.data.assets.package.create import create_assets_package
from src.data.assets.lang.package.create import create_assets_lang_package
from src.data.assets.lang.set import set_langs
from src.data.assets.fonts import default_fonts_str
from src.assets.assets.font import default_font
from src.Port import *
from src.surface import init_surface

def init_data():
    def main():
        def package():
            if exists(packages_path):
                print(f'{Data}: {packages_path} already exists.')
            else:
                print(f'{Data}: {packages_path} is created.')
                with open(packages_path, 'w', encoding='utf-8') as f:
                    create_package(f)
        def options():
            if exists(options_path):
                print(f'{Data}: {options_path} already exists.')
            else:
                print(f'{{Data}}: {options_path} is created.')
                with open(options_path, 'w', encoding='utf-8') as f:
                    create_options(f)
        def assets():
            def assets_package():
                if exists(assets_packages_path):
                    print(f'{Data}: {assets_packages_path} already exists.')
                else:
                    print(f'{Data}: {assets_packages_path} is created.')
                    with open(assets_packages_path, 'w', encoding='utf-8') as f:
                        create_assets_package(f)
            def fonts():
                def default():
                    if exists(default_font):
                        print(f'{Data}: {default_font} already exists.')
                    else:
                        print(f'{Data}: {default_font} is created.')
                        with open(default_font, 'wb') as f:
                            f.write(default_fonts_str)

                if exists(fonts_path):
                    print(f'{Data}: {lang_path} already exists.')
                    default()
                else:
                    mkdir(fonts_path)
                    print(f'{Data}: {lang_path} is created.')
                    default()
            def images():
                def icon():
                    def png():
                        create_icon()
                    if exists(icon_path):
                        print(f'{Data}: {icon_path} already exists.')
                        png()
                    else:
                        mkdir(icon_path)
                        print(f'{Data}: {icon_path} is created.')
                        png()

                if exists(images_path):
                    print(f'{Data}: {images_path} already exists.')
                    icon()
                else:
                    mkdir(images_path)
                    print(f'{Data}: {images_path} is created.')
                    icon()
            def lang():
                def assets_lang_package():
                    if exists(lang_packages_path):
                        print(f'{Data}: {lang_packages_path} already exists.')
                    else:
                        print(f'{Data}: {lang_packages_path} is created.')
                        with open(lang_packages_path, 'w', encoding='utf-8') as f:
                            create_assets_lang_package(f)
                def langs():
                    set_langs()

                if exists(lang_path):
                    print(f'{Data}: {lang_path} already exists.')
                    assets_lang_package()
                    langs()
                else:
                    mkdir(lang_path)
                    print(f'{Data}: {lang_path} is created.')
                    assets_lang_package()
                    langs()
            def texture():
                if exists(texture_path):
                    print(f'{Data}: {texture_path} already exists.')
                else:
                    mkdir(texture_path)
                    print(f'{Data}: {texture_path} is created.')
            def model():
                if exists(model_path):
                    print(f'{Data}: {model_path} already exists.')
                else:
                    mkdir(model_path)
                    print(f'{Data}: {model_path} is created.')

            if exists(assets_path):
                print(f'{Data}: {assets_path} already exists.')
                assets_package()
                fonts()
                images()
                lang()
                texture()
                model()
            else:
                mkdir(assets_path)
                print(f'{Data}: {assets_path} is created.')
                assets_package()
                fonts()
                images()
                lang()
                texture()
                model()

        if exists(main_path):
            print(f'{Data}: {main_path} already exists.')
            package()
            options()
            assets()
        else:
            mkdir(main_path)
            print(f'{Data}: {main_path} is created.')
            package()
            options()
            assets()
    
    main()
    init_options()
    init_lang()

    init_surface()