from src.data.assets.package import package
from json import dump

def create_assets_package(fp) -> None:
    dump(package, fp, indent=4, ensure_ascii=False)