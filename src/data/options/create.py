from json import dump
from src.console import LangDefault

# create a default options file

value = {
    'lang': LangDefault,
}

def create_options(fp) -> None:
    dump(value, fp, indent=4, ensure_ascii=False)