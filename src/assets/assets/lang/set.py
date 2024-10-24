from src.assets.assets.lang.default import langs
from src.data.path import lang_path
from os.path import join,exists
from src.assets.assets.lang.create import create_lang

def set_langs():
    for key, value in langs.items():
        path = join(lang_path, f"{key}.json")
        if exists(path):
            print(f'{path} already exists.')
        else:
            print(f'{path} is created.')
            with open(path, 'w', encoding='utf-8') as f:
                create_lang(f, value)