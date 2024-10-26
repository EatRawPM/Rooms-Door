default_texture = {
    'id': 'default_texture',
    'name': 'Default',
    'type': 'texture',
    'body': {
        'family': {
            'default': {
                'background': False,
                'background-color': None,
                'size': '64x64',
                'pos': '0,0',
                'blit': True,
                'box': {
                    'white': {
                        'count': 2,
                        'size': '32x32',
                        'pos': ['0,0', '32, 32'],
                        'background':True,
                        'background-color': 'white',
                        'blit': True
                    },
                    'purple': {
                        'count': 2,
                        'size': '32x32',
                        'pos': ['32,0', '0, 32'],
                        'background':True,
                        'background-color': 'purple',
                        'blit': True
                    }
                }
            }
        },
        'family-box': {}
    },
    'script': {}
}