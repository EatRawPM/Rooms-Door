from src.ui.element import Element
import pygame


class Box(Element):
    def __init__(self, width: int, height: int, x: int = 0, y: int = 0, color: str | tuple[int, int, int] = 'white'):
        super().__init__()
        self.box = pygame.Surface((width, height))
        self.box.fill(color)
        self.rect = self.box.get_rect()
        self.rect.topleft = (x, y)

    def center(self, **state):
        print(state)

    @property
    def width(self) -> int:
        return self.box.get_width()

    @property
    def height(self) -> int:
        return self.box.get_height()

    @property
    def size(self) -> tuple[int, int]:
        return self.box.get_size()

    @property
    def x(self) -> int:
        return self.rect.x

    @property
    def y(self) -> int:
        return self.rect.y

    @property
    def position(self) -> tuple[int, int]:
        return self.rect.topleft

    def set_width(self, width: int):
        self.box = pygame.transform.scale(self.box, (width, self.box.get_height()))
        self.rect = self.box.get_rect()

    def set_height(self, height: int):
        self.box = pygame.transform.scale(self.box, (self.box.get_width(), height))
        self.rect = self.box.get_rect()

    def set_size(self, width: int, height: int):
        self.box = pygame.transform.scale(self.box, (width, height))
        self.rect = self.box.get_rect()

    def set_x(self, x: int):
        self.rect.x = x

    def set_y(self, y: int):
        self.rect.y = y

    def set_position(self, x: int, y: int):
        self.rect.topleft = (x, y)

    def set_color(self, color: str | tuple[int, int, int]):
        self.box.fill(color)

    def draw(self, surface_display: pygame.Surface):
        surface_display.blit(self.box, self.rect)

BoxType = Box