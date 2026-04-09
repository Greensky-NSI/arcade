from p5 import loadImage

from src.typing.vars import intList, assetsDict


class Drawer:
    images: intList
    loaded = False
    assets: assetsDict = {}
    path: str
    current_folder: str
    index: int = 0
    locked = False

    def __init__(self, path, images: intList):
        """
        Classe dessinateur

        :param path: str - Chemin vers le dossier contenant les images
        :param images: dict[str, int] - Nombre d'images par état
        """
        self.images = images
        self.path = path
        self.current_folder = list(images.keys())[0]

        self.load()

    def load(self):
        """
        Charge les images dans le dossier spécifié
        """
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
        """
        Retourne le dossier actuel
        :return:
        """
        return self.current_folder

    @property
    def image(self):
        """
        Retourne l'image actuelle

        :return:
        """
        self.index = self.index % len(self.assets[self.current_folder])

        return self.assets[self.current_folder][self.index]
    
    @property
    def ready(self):
        """
        Retourne si les images sont chargées

        :return:
        """
        return self.loaded

    def tick(self):
        """
        Passe à l'image suivante

        :return:
        """
        if not self.locked:
            self.index = (self.index + 1)

    def switchState(self, state):
        """
        Change l'état actuel

        :param state:
        :return:
        """
        assert state in self.assets.keys(), f"L'état doit faire partie des images chargées ({', '.join(self.assets.keys())})"

        self.current_folder = state
        return self

    def lockAt(self, index):
        """
        Verrouille l'image à un index donné

        :param index: int - Index de l'image à verrouiller
        :return: self
        """
        self.index = index % len(self.assets[self.current_folder])
        self.locked = True

        return self
    def unlock(self):
        """
        Déverrouille l'image

        :return:
        """
        self.locked = False
        return self
