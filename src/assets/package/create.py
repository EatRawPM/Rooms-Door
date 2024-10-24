from src.assets.package.package import package
from json import dump

def create_package(fp):
    dump(package, fp, indent=4, ensure_ascii=False)