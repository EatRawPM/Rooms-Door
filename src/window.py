# define window full size, you can set it
import pygame
from src.console import DisplayFullScreenState, DisplayDefaultSize, DisplaySize

state = pygame.FULLSCREEN if DisplayFullScreenState else 0

full_size = (1920, 1080)

windows_size = full_size if DisplayDefaultSize else DisplaySize