from os import walk
from os.path import join
from json import load
from typing import LiteralString, Any
from src.data.options import *
from src.assets import lang_packages_path, lang_path
from src.StringSyntax import StringSyntax
from src.langdata import LangData

global_langs = {}

def init_lang() -> None:
    global global_langs

    read_lang()

def get_lang(kay: str) -> Any:
    global global_langs

    value: str = global_langs[kay]

    for string in StringSyntax:
        if string in value:
            key100 = ''
            value100 = ''

            for key10, value10 in LangData.get(kay).items():
                key100 = key10
                value100 = value10

            value = value.replace(key100, value100)

    return value

def read_lang() -> None:
    global global_langs

    lang = get_options('lang')
    path = get_lang_file(lang)
    with open(path, 'r', encoding='utf-8') as f:
        file = load(f)
        global_langs = file

def get_lang_package() -> dict[str: str]:
    with open(lang_packages_path, "r", encoding="utf-8") as f:
        package = load(f)

    return package

def get_lang_file(lang_name: str) -> LiteralString | str | bytes:
    lang_package = get_lang_package()
    langs = lang_package["langs"]
    for path, folders, files in walk(lang_path):
        for file in files:
            if file.endswith(".json"):
                if file != "package.json":
                    name = file.split(".")[0]
                    if name in langs:
                        if name == lang_name:
                            path = join(lang_path, file)
                            return path

    raise FileNotFoundError(f'{lang_name} isn\'t found!')