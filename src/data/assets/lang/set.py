from src.data.assets.lang import langs
from src.assets import lang_path
from os.path import join,exists
from src.data.assets.lang.create import create_lang
from src.Port import *

def set_langs() -> None:
    for key, value in langs.items():
        path = join(lang_path, f"{key}.json")
        if exists(path):
            print(f'{Data}: {path} already exists.')
        else:
            print(f'{Data}: {path} is created.')
            with open(path, 'w', encoding='utf-8') as f:
                create_lang(f, value)