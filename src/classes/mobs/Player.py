from p5 import image, scale
from src.classes.core.Drawer import Drawer
from src.typing.core import direction
from src.utils.toolbox import check_direction, check_positive_integer

class Player:
    x: int
    y: int
    drawer: Drawer
    facing: direction = None
    height = 71
    width = 49

    def __init__(self):
        self.drawer = Drawer("src/assets/sprites/player", {
            "idle": 1,
            "walk": 8
        })

        self.x = 0
        self.y = 0
    
    @property
    def ready(self):
        return self.drawer.ready
    
    def tp(self, x, y):
        assert check_positive_integer(x)
        assert check_positive_integer(y)

        self.x = x
        self.y = y
    
    def draw(self):
        self.drawer.tick()
        img = self.drawer.image

        coeff = 1
        if self.facing in ("negx", "negy"):
            coeff = -1
        
        scale(1, coeff)

        image(img, self.x, self.y, self.width, self.height)

        scale(1, -coeff)
    
    def move(self, dir: direction, amount):
        assert check_direction(dir)
        assert check_positive_integer(amount)

        coeff = 1

        if "neg" in dir:
            coeff = -1
        
        if "y" in dir:
            self.y += coeff * amount
        else:
            self.x += coeff * amount
        
        return self