import json
import os
from PIL import Image, ImageDraw
from src.TextureBuilder.body.rect import Rect
from src.Port import Builder
from typing import Any

def jsonfile_tips_h():
    print('TIPS_H')

    for key, value in TextureBuilder.TIPS_H.items():
        print(f'{key}: {value}')
def jsonfile_tips():
    print('TIPS')

    for key, value in TextureBuilder.TIPS.items():
        if key == 'in_body':
            for ley, lue in value.items():
                print(f'body: ({ley}: {lue})')
                if ley == 'rect':
                    for ey, ue in lue.items():
                        print(f'body/rect: ({ey}: {ue})')
                if ley == 'triangle':
                    for ey, ue in lue.items():
                        print(f'body/triangle: ({ey}: {ue})')
        else:
            print(f'global: ({key}: {value})')

class TextureBuilder:
    TIPS_H = {
        "必要": "必须填写, 否则报错!",
        "建议": "最好填写, 不填写为默认值",
        "可选": "自定义内容, 不填写为不触发",
        "特殊": "特殊的内容",
        "非必要": "如果要自定义的内容, 填写, 否则默认"
    }

    TIPS = {
        "id": "字符串, 建议, 决定生成文件后缀名, 默认: 'png'",
        "name": "字符串, 建议, 决定生成名, 默认: 'texture'",
        "type": "字符串, 必要, 决定是否识别, 必要值: 'texture'",
        "size": "字符串, 建议, 决定图片的大小, 格式: '高度x宽度', 默认: '64x64'",
        "width": "整数, 可选, 决定图片的长度, 层级: '低于size', 默认: 64",
        "height": "整数, 可选, 决定图片的宽度, 层级: '低于size', 默认: 64",
        "background": "布尔, 可选, 决定是否绘制背景, 默认: false",
        "bg": "布尔, 可选, 决定是否绘制背景, 层级: '低于background', 默认: false",
        "background-color": "列表[整数], 可选, 当bg为true时, 更换背景颜色, 默认: [0,0,0]",
        "alpha": "整数, 可选, 决定绘制的透明度, 范围: 0~255, 默认: 255",
        "body": "字典, 特殊, 决定子绘画内容, 格式: 'name': {value}",
        "in_body": {
            "name": "字符串, 必要, 无任何作用, 仅在构建时(控制台)显示, 格式: 全局body格式name",
            "value": "字典, 特殊, 决定body子绘画内容",
            "type": "字符串, 非必要, 默认: rect, TIPS: 每个type参数不一样",
            "rect": {
                "self": "body子类",
                "x": "整数, 建议, 决定Body的x位置, 默认: 0",
                "y": "整数, 建议, 决定Body的y位置, 默认: 0",
                "size": "字符串, 建议, 决定Body的大小, 格式: '高度x宽度', 默认: '64x64'",
                "width": "整数, 可选, 决定Body的长度, 层级: '低于size', 默认: 64",
                "height": "整数, 可选, 决定Body的宽度, 层级: '低于size', 默认: 64",
                "fill": "布尔, 可选, 决定是否填充, 默认: true",
                "alpha": "整数, 可选, 决定绘制填充的透明度, 范围: 0~255, 默认: 255",
                "color": "列表[整数], 可选, 当fill为true时, 更换填充颜色, 默认: [0,0,0]",
                "outline": "布尔, 可选, 决定是否绘制边框, 默认: false",
                "ol": "布尔, 可选, 决定是否绘制边框, 层级: '低于outline', 默认: false",
                "outline-size": "整数, 可选, 层级: '低于outline', 默认: 0",
                "ols": "整数, 可选, 层级: 'outline-size', 默认: 1",
                "outline-alpha": "整数, 可选, 决定绘制边框的透明度, 范围: 0~255, 默认: 255",
                "ola": "整数, 可选, 决定绘制边框的透明度, 范围: 0~255, 默认: 255"
            },
            "triangle": {
                "self": "body子类",
            }
        }
    }

    DEFAULT_MODE = 'save'

    DEFAULT_ID = 'png'
    DEFAULT_NAME = 'texture'
    DEFAULT_SIZE = '64x64'
    DEFAULT_BG = False
    DEFAULT_BG_COLOR = [0,0,0]
    DEFAULT_ALPHA = 255

    MODE = ['json', 'dict']

    def __init__(self, mode:str = 'json', input_value: str | dict[str, Any] = '', output_folder: str = '') -> None:
        self.__mode = mode
        self.__input_value = input_value
        self.__output_folder = output_folder
        self.__data: dict = {}
        self.__image = None
        self.__draw = None
        self.__body: dict = {}

        self.__id = TextureBuilder.DEFAULT_ID
        self.__name = TextureBuilder.DEFAULT_NAME

        self.__size = TextureBuilder.DEFAULT_SIZE
        self.__width = 64
        self.__height = 64

        self.__bg = TextureBuilder.DEFAULT_BG
        self.__bg_color = (0,0,0)
        self.__alpha = TextureBuilder.DEFAULT_ALPHA

    def __load_json(self) -> None:
        match self.__mode:
            case 'json':
                try:
                    with open(self.__input_value, 'r', encoding='utf-8') as f:
                        self.__data: dict = json.load(f)
                except FileNotFoundError as e:
                    raise FileNotFoundError(f'error: {e}')
            case 'dict':
                if isinstance(self.__input_value, dict):
                    self.__data = self.__input_value
                else:
                    raise TypeError(f'{self.__mode}下, 输入必须为dict!')
            case other:
                raise TypeError(f'{other}mode不存在!')

        if self.__data.get('type', '').lower() != 'texture':
            raise TypeError(f'JSON的Type是必须的, 且必须为\'texture\'')

        self.__id = self.__data.get('id', self.__id)
        self.__name = self.__data.get('name', self.__name)

        size = self.__data.get('size', self.__size)

        if not size is None:
            self.__width, self.__height = map(int, size.split('x'))

        self.__width = self.__data.get('width', self.__width)
        self.__height = self.__data.get('height', self.__height)

        self.__bg = self.__data.get('background', self.__data.get('bg', self.__bg))

        self.__alpha = self.__data.get('alpha', self.__alpha)

        if self.__bg:
            bg_color = self.__data.get('background-color', self.__data.get('bg-color', TextureBuilder.DEFAULT_BG_COLOR))
            try:
                bg_color[3] = self.__alpha
            except IndexError:
                bg_color.append(self.__alpha)
        else:
            bg_color = [0,0,0,0]

        self.__bg_color = tuple(bg_color)

    def __load_body(self) -> None:
        self.__body = self.__data.get('body', {})

        typey = 'rect'

        if not isinstance(self.__body, dict):
            raise TypeError(f'Body 必须为字典')

        if self.__body == {}:
            return

        for key, value in self.__body.items():
            name: str = key
            data: dict = value

            typey = data.get('type', typey)

            match typey:
                case 'rect':
                    x = 0
                    y = 0
                    d_size = '32x32'
                    width = 32
                    height = 32
                    fill = True
                    alpha = 255
                    color = (0,0,0)
                    outline = False
                    outline_size = 1
                    outline_color = (255,255,255),
                    outline_alpha = 255

                    x = data.get('x', x)
                    y = data.get('y', y)

                    size = data.get('size', d_size)

                    if not size is None:
                        width, height = map(int, size.split('x'))

                    width = data.get('width', width)
                    height = data.get('height', height)

                    fill = data.get('build', fill)

                    alpha = data.get('alpha', alpha)

                    if fill:
                        list_color = data.get('color', [0,0,0])
                        try:
                            list_color[3] = alpha
                        except IndexError:
                            list_color.append(alpha)
                    else:
                        list_color = [0,0,0,0]

                    color = tuple(list_color)

                    outline = data.get('outline', data.get('ol', outline))

                    outline_size = data.get('outline_size', data.get('ols', outline_size))

                    outline_alpha = data.get('outline_alpha', data.get('ola', outline_alpha))

                    if outline:
                        list_outline_color = data.get('outline-color', data.get('olc', [0,0,0]))
                        try:
                            list_outline_color[3] = outline_alpha
                        except IndexError:
                            list_outline_color.append(outline_alpha)
                    else:
                        list_outline_color = color

                    outline_color = tuple(list_outline_color)

                    Rect(name, self.__draw, x, y, width, height, color, outline_size, outline_color).build()
                case 'triangle':
                    ...
                case other:
                        raise TypeError(f'{other}不存在!')

    def build(self, mode: str='', create_folder: bool = True) -> None:
        if not mode is None:
            __mode = TextureBuilder.DEFAULT_MODE
        elif mode == 'save':
            __mode = 'save'
        elif mode == 'show':
            __mode = 'show'
        else:
            raise ValueError(f'{mode}不存在, 请选择正确的模式, 或留空!')

        self.__load_json()

        self.__image = Image.new('RGBA', (self.__width, self.__height), self.__bg_color)

        self.__draw = ImageDraw.Draw(self.__image)

        self.__load_body()

        print(f'{Builder}: {self.__name}.{self.__id}正在构建...')

        save_folder = os.path.join(self.__output_folder)
        save_path = os.path.join(save_folder, f'{self.__name}.{self.__id}')

        if create_folder:
            os.makedirs(save_folder, exist_ok=True)

        if __mode == 'save':
            self.__image.save(save_path)
        elif __mode == 'show':
            self.__image.show()

        print(f'{Builder}: {self.__name}.{self.__id}已生成!')