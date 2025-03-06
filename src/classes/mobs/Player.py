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
    """
    Classe représentant un joueur.

    Attributs:
        x (int): Coordonnée x du joueur.
        y (int): Coordonnée y du joueur.
        drawer (Drawer): Objet Drawer pour dessiner le joueur.
        facing (direction): Direction vers laquelle le joueur fait face.
        height (int): Hauteur du joueur.
        width (int): Largeur du joueur.
        tickTimer (Timer): Timer pour gérer les ticks du joueur.
        bombs (List[Bomb]): Liste des bombes placées par le joueur.
        player_stats (PlayerStats): Statistiques du joueur.
        id (str): Identifiant unique du joueur.
        last_tped (tuple): Dernière position téléportée du joueur.
        can_drop_bomb (list): Indicateur et timer pour savoir si le joueur peut poser une bombe.

    Méthodes:
        tp(self, x, y): Téléporte le joueur à une position donnée.
        draw(self): Dessine le joueur.
        die(self): Tue le joueur.
        move(self, dir, amount, limit_to): Déplace le joueur dans une direction donnée.
        place_bomb(self, callback): Place
    """
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
    can_drop_bomb = [True, Timer(30, 1)]

    def __init__(self):
        """
        Initialise le joueur.
        """
        self.drawer = Drawer("src/assets/sprites/player", {
            "idle": 1,
            "walk": 8
        })

        self.x = 0
        self.y = 0
        self.id = str(uuid4())

    @property
    def uuid(self):
        """
        Retourne l'identifiant du joueur.

        :return:
        """
        return self.id

    @property
    def ready(self):
        """
        Vérifie si les images du joueur sont chargées.

        :return:
        """
        return self.drawer.ready

    @property
    def stats(self):
        """
        Retourne les statistiques du joueur.

        :return:
        """
        return self.player_stats.stats
    
    def tp(self, x, y):
        """
        Téléporte le joueur à une position donnée.

        :param x:
        :param y:
        :return:
        """
        assert check_positive_integer(x)
        assert check_positive_integer(y)

        self.x = x
        self.y = y

        self.last_tped = (x, y)
    
    def draw(self):
        """
        Dessine le joueur.

        :return:
        """
        if self.tickTimer.tick():
            self.drawer.tick()
        if not self.can_drop_bomb[0]:
            if self.can_drop_bomb[1].tick():
                self.can_drop_bomb[0] = True

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
        """
        Tue le joueur.

        :return:
        """
        if self.last_tped:
            self.tp(*self.last_tped)

        self.player_stats.reset()

    def move(self, dir: direction, amount, limit_to = None):
        """
        Déplace le joueur dans une direction donnée.

        :param dir: direction - Direction du déplacement.
        :param amount: int - Distance du déplacement.
        :param limit_to: int - Limite du déplacement.
        :return:
        """
        assert check_direction(dir)
        assert check_positive_integer(amount)

        coeff = 1

        self.facing = dir

        if "neg" in dir:
            coeff = -1

        if "y" in dir:
            self.y += coeff * amount * player_variables.dspeed * self.player_stats.speed
        else:
            self.x += coeff * amount * player_variables.dspeed * self.player_stats.speed

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
        """
        Place une bombe à la position actuelle du joueur.

        :param callback: Callable - Fonction à appeler lors de l'explosion.
        :return:
        """
        if len(self.bombs) >= self.player_stats.bombs or not self.can_drop_bomb[0]:
            return

        self.can_drop_bomb[0] = False

        lab_x, lab_y = floor(self.x / 50), floor(self.y / 50)
        real_x, real_y = lab_x * 50, lab_y * 50
        bomb = Bomb(real_x + 9, real_y + 9, self.stats, self.uuid, callback)

        self.bombs.append(bomb)

    def increment_score(self, amount):
        """
        Incrémente le score du joueur.

        :param amount:
        :return:
        """
        assert check_positive_integer(amount)

        self.player_stats.add_score(amount)