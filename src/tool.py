import pygame
from src.data.assets.font import default_font
import sys


def draw_text(text, font: str = default_font, size: int = 30, color: str | tuple[int, int, int] = 'white', x: int = 0, y: int = 0) -> None:
    pygame.init()
    surface_display = pygame.display.get_surface()
    Font = pygame.font.Font(font, size)
    surface = Font.render(str(text), True, color)
    rect = surface.get_rect(topleft=(x, y))
    surface_display.blit(surface, rect)

def exit_game() -> None:
    pygame.quit()
    sys.exit()