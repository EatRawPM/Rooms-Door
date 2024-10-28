from PIL import ImageDraw
from src.Port import *

class Rect:
    def __init__(self,name: str ,draw: ImageDraw.ImageDraw, x: int, y: int, width: int, height: int, fill_color: tuple, out_line_size: int = 0,outline_color: tuple = (0,0,0)):
        self.__name = name
        self.__draw = draw
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

        self.__end_x = self.__x + self.__width
        self.__end_y = self.__y + self.__height

        self.__fill_color = fill_color
        self.__outline_size = out_line_size
        self.__outline_color = outline_color

    def build(self):
        print(f'{Builder}: {self.__name}正在构建...')
        self.__draw.rectangle([self.__x, self.__y, self.__end_x, self.__end_y], self.__fill_color, self.__outline_color, self.__outline_size)
        print(f'{Builder}: {self.__name}已生成!')