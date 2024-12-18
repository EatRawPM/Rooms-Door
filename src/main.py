from src.data import init_data

init_data()

from src.tool import *
from src.assets.assets.icon.icon import icon
from src.data.package.get import get_main_package
from src.scene.core.save_scene import *
from src.scene.run_scene import RunScene
from src.scene.menu_scene import MenuScene
from src.scene.game_scene import GameScene
from src.scene.core.scene_manager import SceneManager
from src.console import SceneDefault, DisplayFill
from src.window import state, windows_size
from src.package import Title
import pygame

class App:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_icon(icon)
        pygame.display.set_caption(f'{Title} {get_main_package("version")}')
        pygame.display.set_mode(windows_size, state)

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
        self.surface_display.fill(DisplayFill)
        self.scene_manager.on_draw()
        pygame.display.update()
        
    def run(self) -> None:
        self.scene_manager.set_current_scene(get_scene(SceneDefault))
        self.scene_manager.on_enter()
        while True:
            self.handle_events()
            self.update()