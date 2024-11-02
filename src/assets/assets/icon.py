from os.path import join
from pygame.image import load
from src.assets.assets.images.path import images_path

#path
icon_path = join(images_path, 'icons')

#icon
icon = load(join(icon_path, 'icon.png'))