import json
import os
from PIL import Image, ImageDraw
from pygame import SurfaceType
from src.TextureBuilder.body.rect import Rect
from src.Port import Builder
from typing import Any
from pygame.image import frombytes

class TextureBuilder:
    DEFAULT_MODE = 'save'

    DEFAULT_ID = 'png'
    DEFAULT_NAME = 'texture'
    DEFAULT_SIZE = '64x64'
    DEFAULT_BG = False
    DEFAULT_BG_COLOR = [0,0,0]
    DEFAULT_ALPHA = 255

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

        self.__width = self.__data.get('width', self.__data.get('w', self.__width))
        self.__height = self.__data.get('height', self.__data.get('h', self.__width))

        self.__bg = self.__data.get('background', self.__data.get('bg', self.__bg))

        self.__alpha = self.__data.get('alpha', self.__data.get('a', self.__alpha))

        if self.__bg:
            bg_color = self.__data.get('background-color', self.__data.get('bgc', TextureBuilder.DEFAULT_BG_COLOR))
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

    def build(self, mode: str='save', create_folder: bool = True) -> None | bytes | SurfaceType:
        print(f'{Builder}: {self.__name}.{self.__id}正在构建...')

        self.__load_json()

        self.__image = Image.new('RGBA', (self.__width, self.__height), self.__bg_color)

        self.__draw = ImageDraw.Draw(self.__image)

        self.__load_body()

        save_folder = os.path.join(self.__output_folder)
        save_path = os.path.join(save_folder, f'{self.__name}.{self.__id}')

        if create_folder:
            os.makedirs(save_folder, exist_ok=True)


        print(mode)
        match mode:
            case 'save':
                self.__image.save(save_path)
            case 'show':
                self.__image.show()
            case 'bytes':
                return self.__image.tobytes()
            case 'load':
                image_bytes = self.__image.tobytes()
                return frombytes(image_bytes, self.__image.size, 'RGBA')

            case other:
                raise TypeError(f'{other}不存在!')

        print(f'{Builder}: {self.__name}.{self.__id}已生成!')