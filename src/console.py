from pygame.math import Vector2 as vec2

'''
Console module for Rooms & Doors.
You can use this module to interact with the Rooms & Doors console.
'''


# navigation
'''
Hold down the 'Ctrl' key and click Reach.
'''

def client() -> None: ...
def server() -> None: ...
def data() -> None: ...
def lang() -> None: ...
def display() -> None: ...
def scene() -> None: ...

# client

client()

# if it is '', use ServerTitle.
ClientTitle: str = ''

# server

server()

# if it is '', use DefaultTitle.
ServerTitle: str = ''

# data

data()

"""
path of base path, '.rooms&doors' file in it.
if you want to change the path, you can change it here.
it is '' by default.
path of base path, base file in it.
if you want to change the path, you can change it here.
it is '' by default.
You better don't change it unless you know what you are doing.
"""
DataPath: str = ''

#lang 

"""
it is 'en_us' by default.
He decides the default lang for you when you first enter the game.(when the settings.json file is created)
Please check if the lang exists in the lang file, as this may cause errors.
"""

lang()

LangDefault: str = 'en_us'

# display

display()

# if True, it will define the size of the window.
DisplayDefaultSize: bool = False
# if True, it will display the window in your settings. else it will be in windowed mode.
DisplayFullScreenState: bool = False
# if default size is False, it will be the size of the window.
DisplaySize: vec2 = vec2(1280, 720)
# display fill color.
DisplayFill: str | tuple[int,int,int] = 'black'

# scene

scene()

SceneDefault: str = 'run'  # the scene that will be run when the game starts.