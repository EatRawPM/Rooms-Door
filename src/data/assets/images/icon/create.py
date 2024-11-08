from src.assets.assets.icon import icon_path
from src.data.assets.images.icon import icon_str
from os.path import join
from PIL import Image

def create_icon():
    i = Image.frombytes('RGBA', (64,64), icon_str)
    i.save(join(icon_path, 'icon.png'))