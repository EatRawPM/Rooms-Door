from json import load
from src.RDTextureBuilder.build import Build

class Read:
    def __init__(self, path):
        self.path = path
        self.file = ''

    def load(self):
        with open(self.path, 'r') as f:
            file = load(f)

            return file

    def read(self):
        self.file = self.load()

        return self.file

class RDTextureBuilder:
    def __init__(self, input_path: str = '', output_path: str = ''):
        self.input_path = input_path
        self.output_path = output_path
        self.file = Read('./test.json').read()

    def build(self) -> None:
        Build()

builder = RDTextureBuilder()