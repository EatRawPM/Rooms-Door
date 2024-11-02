from typing import Any
from src.assets import options_path
from json import load, dump

global_options = {}

def init_options() -> None:
    global global_options
    
    read_options()
    
def read_options() -> None:
    global global_options
    
    with open(options_path, 'r', encoding='utf-8') as f:
        s = load(f)
        global_options = s

def get_options(v: str) -> Any:
    global global_options
    
    for k, va in global_options.items():
        if k == v:
            s = global_options[k]
            return s

def set_options(key: str, value: any) -> None:
    global global_options
    
    for k, v in global_options.items():
        if k == key:
            print(value)
            global_options[k] = value
            with open(options_path, 'w', encoding='utf-8') as f:
                dump(global_options, f, indent=4, ensure_ascii=False)
            return