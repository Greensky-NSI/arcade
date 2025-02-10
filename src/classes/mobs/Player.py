from p5 import image, scale, translate, pushMatrix, resetMatrix, popMatrix

from PlayerStats import PlayerStats
from src.classes.core.Drawer import Drawer
from src.classes.core.Timer import Timer
from src.typing.core import direction
from src.utils.globals import player_variables
from src.utils.parsers import parse_number_between_walls
from src.utils.toolbox import check_direction, check_positive_integer
from src.classes.mobs.Bomb import Bomb
from typing import List

class Player:
    x: int
    y: int
    drawer: Drawer
    facing: direction = None
    height = 71
    width = 49
    tickTimer = Timer(3, 1)
    bombs: List[Bomb] = []
    stats = PlayerStats()

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
        if self.tickTimer.tick():
            self.drawer.tick()

        img = self.drawer.image

        self.width = img.width
        self.height = img.height

        coeff = 1
        if self.facing in ("negx", "negy"):
            coeff = -1

        resetMatrix()
        pushMatrix()
        increment = +(self.facing in ("negx", "posx")) + 1 % 2 + self.width // 2

        translate(self.x, self.y)
        scale(coeff, 1)

        image(img, -increment, 0)

        popMatrix()

    def move(self, dir: direction, amount):
        assert check_direction(dir)
        assert check_positive_integer(amount)

        coeff = 1

        self.facing = dir

        if "neg" in dir:
            coeff = -1
        
        if "y" in dir:
            self.y += coeff * amount * player_variables.dspeed
        else:
            self.x += coeff * amount * player_variables.dspeed

        self.x, self.y = parse_number_between_walls(self.x, "WIDTH"), parse_number_between_walls(self.y, "HEIGHT")

        return self
    
    def place_bomb(self):
        if len(self.bombs) >= self.stats.bombs:
            return

        bomb = Bomb(self.x - self.width // 2, self.y + self.height // 2)

        self.bombs.append(bomb)