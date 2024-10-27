import json
import os
from PIL import Image, ImageDraw
from src.TextureBuilder.body import Rect

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
                if key == 'rect':
                    for ey, ue in value.items():
                        print(f'body/rect: ({ey}: {ue})')
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
                "self": "body子类, "
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

    def __init__(self, input_file, output_folder):
        self.__input_file = input_file
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
        self.__bg_color = TextureBuilder.DEFAULT_BG_COLOR
        self.__alpha = TextureBuilder.DEFAULT_ALPHA

    def __load_json(self):
        try:
            with open(self.__input_file, 'r', encoding='utf-8') as f:
                self.__data: dict = json.load(f)
        except FileNotFoundError as e:
            raise FileNotFoundError(f'error: {e}')

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
            bg_color = self.__data.get('background-color', self.__data.get('bg-color', self.__bg_color))
            try:
                bg_color[3] = self.__alpha
            except IndexError:
                bg_color.append(self.__alpha)
        else:
            bg_color = (0,0,0,0)

        self.__bg_color = tuple(bg_color)

    def __load_body(self):
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
                    size = '32x32'
                    width = 32
                    height = 32

                    x = data.get('x', x)
                    y = data.get('y', y)

                    Rect(self.__draw, x, y, width, height, (0,0,0)).build()
                case other:
                        raise TypeError(f'{other}不存在!')

    def build(self, mode: str=''):
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

        save_path = os.path.join(self.__output_folder, f'{self.__name}.{self.__id}')

        if __mode == 'save':
            self.__image.save(save_path)
        elif __mode == 'show':
            self.__image.show()

        print(f'{self.__name}.{self.__id}已生成.')