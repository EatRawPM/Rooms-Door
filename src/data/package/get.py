import json
from typing import Any
from src.assets.__init__ import packages_path

def get_main_package(key: str) -> Any:
    with open(packages_path, 'r', encoding='utf-8') as f:
        return json.load(f)[key]