from src.assets.assets.lang.package.package import package
from json import dump

def create_assets_lang_package(fp) -> None:
    dump(package, fp, indent=4, ensure_ascii=False)