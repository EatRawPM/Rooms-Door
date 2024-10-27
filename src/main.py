from src.tool import *
from src.data.assets.icon import icon
from src.assets.data import init_data
from src.lang import *
from src.scene.core.save_scene import *
from src.scene.run_scene import RunScene
from src.scene.menu_scene import MenuScene
from src.scene.game_scene import GameScene
from src.scene.core.scene_manager import SceneManager
# from src.TextureBuilder import TextureBuilder
import pygame

# TextureBuilder('./src/TextureBuilder/test.json', './src/TextureBuilder/out').build()

init_data()

class App:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_icon(icon)
        pygame.display.set_caption(get_lang('core.display.caption'))
        pygame.display.set_mode((1280, 720))

        set_scene('manager', SceneManager())
        set_scene('menu', MenuScene())
        set_scene('run', RunScene())
        set_scene('game', GameScene())
        
        self.surface_display = pygame.display.get_surface()
        
        self.clock = pygame.time.Clock()

        self.scene_manager = get_scene('manager')
        self.run_scene = get_scene('run')
        self.menu_scene = get_scene('menu')
        self.game_scene = get_scene('game')
        
    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit_game()
            self.scene_manager.on_input(event)
    def update(self) -> None:
        self.clock.tick(60)
        self.scene_manager.on_update()
        self.surface_display.fill('black')
        self.scene_manager.on_draw()
        pygame.display.update()
        
    def run(self) -> None:
        self.scene_manager.set_current_scene(get_scene('run'))
        self.scene_manager.on_enter()
        while True:
            self.handle_events()
            self.update()