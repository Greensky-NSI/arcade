from math import floor
from typing import List

from p5 import image, scale, translate, pushMatrix, resetMatrix, popMatrix
from uuid import uuid4
from src.classes.core.Drawer import Drawer
from src.classes.core.PlayerStats import PlayerStats
from src.classes.core.Timer import Timer
from src.classes.mobs.Bomb import Bomb
from src.typing.core import direction
from src.utils.globals import player_variables
from src.utils.parsers import parse_number_between_walls
from src.utils.toolbox import check_direction, check_positive_integer


class Player:
    x: int
    y: int
    drawer: Drawer
    facing: direction = None
    height = 71
    width = 49
    tickTimer = Timer(3, 1)
    bombs: List[Bomb] = []
    player_stats = PlayerStats()
    id: str
    last_tped = None

    def __init__(self):
        self.drawer = Drawer("src/assets/sprites/player", {
            "idle": 1,
            "walk": 8
        })

        self.x = 0
        self.y = 0
        self.id = str(uuid4())

    @property
    def uuid(self):
        return self.id

    @property
    def ready(self):
        return self.drawer.ready

    @property
    def stats(self):
        return self.player_stats.stats
    
    def tp(self, x, y):
        assert check_positive_integer(x)
        assert check_positive_integer(y)

        self.x = x
        self.y = y

        self.last_tped = (x, y)
    
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

        image(img, -increment, -self.height)

        popMatrix()

    def die(self):
        if self.last_tped:
            self.tp(*self.last_tped)

        self.player_stats.reset()

    def move(self, dir: direction, amount, limit_to = None):
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

        if limit_to:
            if dir == "posx":
                self.x = min(self.x, limit_to)
            elif dir == "negx":
                self.x = max(self.x, limit_to)
            elif dir == "posy":
                self.y = min(self.y, limit_to)
            elif dir == "negy":
                self.y = max(self.y, limit_to)

        self.x, self.y = parse_number_between_walls(self.x, "WIDTH"), parse_number_between_walls(self.y, "HEIGHT")

        return self
    
    def place_bomb(self, callback = None):
        if len(self.bombs) >= self.player_stats.bombs:
            return

        lab_x, lab_y = floor(self.x / 50), floor(self.y / 50)
        real_x, real_y = lab_x * 50, lab_y * 50
        bomb = Bomb(real_x + 9, real_y + 9, self.stats, self.uuid, callback)

        self.bombs.append(bomb)