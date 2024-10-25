from src.tool import draw_text
from src.scene.core.scene import Scene
from src.scene.core.save_scene import *
from src.timer import CountdownTimer

class RunScene(Scene):
    def __init__(self):
        super().__init__()
        self.scene_manager = get_scene('manager')

        self.timer = CountdownTimer(3)

    def on_enter(self):
        self.timer.start()

    def on_update(self):
        if self.timer.is_done():
            self.scene_manager.switch_scene('menu')

    def on_input(self, event): ...

    def on_draw(self):
        draw_text(self.timer.remaining_time())

    def on_exit(self): ...