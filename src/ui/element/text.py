from src.ui.element import Element
from src.assets.assets.font import default_font
import pygame

class Text(Element):
    def __init__(self, text, size: int = 30, x: int = 0, y: int = 0, color: str | tuple[int, int, int] = 'white', font: str = default_font):
        super().__init__()
        self.font = pygame.font.Font(font, size)
        self.surface = self.font.render(str(text), True, color)
        self.rect = self.surface.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, surface_display: pygame.Surface):
        surface_display.blit(self.surface, self.rect)

TextType = Text