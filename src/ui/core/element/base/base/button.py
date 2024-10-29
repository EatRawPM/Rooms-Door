from src.ui.core.element.base.base.box import Box
import pygame


class Button(Box):
    def __init__(self, width: int, height: int, x: int, y: int, color: tuple[int, int, int] | str = 'white'):
        super().__init__(width, height, x, y, color)
        self.func = print
        self.args = 'this a bottom', 'test'

    def set_func(self, func):
        self.func = func

    def set_value(self, *args):
        self.args = args

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.func(*self.args)

ButtonType = Button