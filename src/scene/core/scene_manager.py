from src.scene import Scene
from src.scene.core.save_scene import *

class SceneManager(Scene):
    def __init__(self) -> None:
        super(SceneManager, self).__init__()
        self.current_scene = Scene()
        self.scene_type = ["run","menu", "game"]

    def set_current_scene(self,scene) -> None:
        self.current_scene.on_exit()
        self.current_scene = scene

    def switch_scene(self, types) -> None:
        self.current_scene.on_exit()
        match types:
            case "run":
                self.current_scene = get_scene("run")
            case "menu":
                self.current_scene = get_scene("menu")
            case "game":
                self.current_scene = get_scene("game")
        self.current_scene.on_enter()

    def on_enter(self) -> None:
        self.current_scene.on_enter()

    def on_update(self) -> None:
        self.current_scene.on_update()

    def on_draw(self) -> None:
        self.current_scene.on_draw()

    def on_input(self, event) -> None:
        self.current_scene.on_input(event)

    def on_exit(self) -> None:
        self.current_scene.on_exit()