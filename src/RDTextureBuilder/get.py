from src.RDTextureBuilder.data import datas
from typing import Any

class Get:
    def __init__(self, fp: dict[str, Any], mode: str = 'global'):
        self.mode = mode
        self.fp = fp

        self.match()

    def match(self):
        match self.mode:
            case 'global':
                for key, value in self.fp.items():
                    print(key)
                    for key1, value1 in datas.items():
                        if not key in value:
                            print(123)
                        else:
                            print(111)
                        # if value1['key']:
                        #     ...
                        # else:
                        #     raise TypeError('The necessary value does not exist')
            case other:
                ...

    def id(self):

        return