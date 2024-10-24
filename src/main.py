from src.tool import *
from src.data.assets.icon import icon
from src.assets.data import init_data
import pygame

init_data()

class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Rooms & Doors")
        pygame.display.set_mode((1280, 720))
        
        self.surface_display = pygame.display.get_surface()
        
        self.clock = pygame.time.Clock()
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit_game()
        
    def update(self):
        self.clock.tick(60)
        pygame.display.update()
        
    def run(self):
        while True:
            self.handle_events()
            self.update()