from p5 import loadImage
from src.typing.vars import intList, assetsDict

class Drawer:
    images: intList
    loaded = False
    assets: assetsDict = {}
    path: str
    current_folder: str
    index: int = 0

    def __init__(self, path, images: intList):
        self.images = images
        self.path = path
        self.current_folder = list(images.keys())[0]

        self.load()

    def load(self):
        if self.loaded:
            return

        for folder in self.images.keys():
            count = self.images[folder]
            self.assets[folder] = []

            for x in range(count):
                path = f"{self.path}/{folder}/{x}.png"
                img = loadImage(path)

                self.assets[folder].append(img)
        
        self.loaded = True
    
    @property
    def folder(self):
        return self.current_folder

    @property
    def image(self):
        self.index = self.index % len(self.assets[self.current_folder])

        return self.assets[self.current_folder][self.index]
    
    @property
    def ready(self):
        return self.loaded

    def tick(self):
        self.index = (self.index + 1)

    def switchState(self, state):
        assert state in self.assets.keys(), f"L'état doit faire partie des images chargées ({', '.join(self.assets.keys())})"

        self.current_folder = state
        return self

