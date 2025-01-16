from p5 import loadImage, PImage

class Drawer:
    images: dict[str, int]
    loaded = False
    assets: dict[str, list[PImage]]
    path: str
    current_folder: str
    index: int = 0

    def __init__(self, path, images: dict[str, int]):
        self.images = images
        self.path = path
        self.current_folder = images.keys()[0]

        self.load()

    def load(self):
        if self.loaded:
            return

        for folder in self.images.keys():
            count = self.images[folder]
            self.assets[folder] = []

            for x in range(count):
                path = f"{self.path}/{x}.png"
                img: PImage = loadImage(path)

                self.assets[folder].append(img)
        
        self.loaded = True
    
    @property
    def folder(self):
        return self.current_folder

    @property
    def image(self):
        return self.assets[self.current_folder][self.index]
    
    @property
    def ready(self):
        return self.loaded

    def tick(self):
        self.index = self.index + 1 % len(self.assets[self.current_folder])

        return self
    
    def switchState(self, state):
        assert state in self.assets.keys(), f"L'état doit faire partie des images chargées ({", ".join(self.assets.keys())})"

        self.current_folder = state
        self.index = 0

        return self

