from src.TextureBuilder.builder import TextureBuilder
from src.data.assets.texture.default import default_texture

default_texture_surface = TextureBuilder('dict', default_texture, './out').build(mode='load')