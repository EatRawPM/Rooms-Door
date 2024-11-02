import pygame
from pygame import SurfaceType
from pygame.transform import scale
from src.core.objects.images.image import Image
from src.imports import imports_files
import time

class Animation(Image):
    def __init__(self, screen: SurfaceType, folder: str,now_int: int = 0, maxint: int = 1,timer: int = 1, size: tuple[float, float] = None, x: int=0, y: int=0):
        self.images = imports_files(folder)
        self.image = self.images[now_int]
        self.now_int = now_int
        self.maxint = maxint
        self.screen = screen
        self.timer = timer
        super().__init__(self.screen, self.image, size, x, y)

        self.times = 0

    def update(self):
        if time.time() - self.times <= self.timer:
            return

        self.times = time.time()

        self.now_int = 0 if self.nowint == self.maxint else + 1
        self.image = self.images[self.nowint]

    def draw(self):
        super().draw()
        self.update()