from src.RDTextureBuilder.data import datas

class Get:
    def __init__(self, get_value):
        self.value = get_value

    def match(self):
        for key, value in datas.items():
            if self.value == key:
                print('is')

    def id(self):

        return

Get('id').match()