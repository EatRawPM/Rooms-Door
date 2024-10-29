from typing import Any

_save_scene = {}

def save_init() -> None:  # 初始化
    global _save_scene
    _save_scene = {}

def set_scene(key, value) -> None:
    #定义一个全局变量
    _save_scene[key] = value

def get_scene(key) -> Any:
    #获得一个全局变量，不存在则提示读取对应变量失败
    try:
        return _save_scene[key]
    except KeyError:
        print('读取'+key+'失败\r\n')