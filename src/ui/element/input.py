import pygame
import string
from src.ui.element.text import Text
from src.assets.assets.font import default_font


class Input(Text):
    def __init__(self, width: int = 100, height: int = 30, x: int = 0, y: int = 0,
                 color: str | tuple[int, int, int] = 'white', rect_color: str | tuple[int, int, int] = 'black',
                 font: str = default_font):
        self.width = width
        self.height = height
        self.color = color
        self.rect_color = rect_color
        self.font = font
        super().__init__('', self.height, x, y, color, self.font)
        self.rect = pygame.Rect(x, y, self.width, self.height)

        self.list: list = []  # 输入框内容列表
        self.active = False  # 输入框是否激活
        self.cursor = True  # 输入框是否显示光标
        self.count = 0  # 光标计时
        self.delete = False  # 是否删除

        self.last_delete = 0  # 上一次删除时间

    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False

        elif self.active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.delete = True
                elif event.unicode in string.ascii_letters or event.unicode in '0123456789_':
                    self.list.append(event.unicode)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_BACKSPACE:
                    self.delete = False

    def draw(self, surface_display: pygame.Surface):
        surface = self.font.render(''.join(self.list), True, self.color)
        if surface.get_rect().width <= self.width:
            self.rect.width = self.width
        else:
            self.rect.width = surface.get_rect().width
        pygame.draw.rect(surface_display, self.rect_color, self.rect, 1)
        surface_display.blit(surface, self.rect)

        self.count += 1
        if self.count == 20:
            self.count = 0
            self.cursor = not self.cursor

        if self.active and self.cursor:
            rect = surface.get_rect()
            x = self.rect.x + rect.width
            pygame.draw.line(surface_display, 'white', (x, self.rect.y), (x, self.rect.y + self.height), 1)

        if self.delete and self.list:  # 删除最后一个字符
            self.list.pop()

    @property
    def text(self) -> str:
        return ''.join(self.list)

InputType = Input