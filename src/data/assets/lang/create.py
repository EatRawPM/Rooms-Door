from json import dump

def create_lang(fp, value: dict) -> None:
    dump(value, fp, indent=4, ensure_ascii=False)