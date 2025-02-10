from p5 import run, size, background
from src.classes.mobs.Player import Player
from src.utils.globals import player_variables, ENV
from src.typing.custom_types import *
from src.classes.core.labyrinthe import Labyrinthe, models

player: Player
laby: Labyrinthe
initiated = False


def setup():
    global player, laby
    background(128)

    size(ENV.WIDTH, ENV.HEIGHT)
    player = Player()
    player.tp(5, 5)

    laby = Labyrinthe(ENV.WIDTH, ENV.HEIGHT, 50, model_folder_name="model_one", model_assets_indestructibles_count=2, model_assets_obstacles_count=7)
    laby.obstacle(models["one"]["obstacles"])
    laby.indestructible(models["one"]["indestructibles"])

    laby.order()


def draw():
    global initiated

    if not initiated:
        background(128)

        laby.afficher_laby()
        initiated = True

    if player.ready:
        laby.affichage_opti(player.x // laby.taille_case, player.y // laby.taille_case)
        player.draw()

    if key_is_pressed:
        pressed = str(key).lower()

        moved = False
        if pressed in player_variables.deplacements_keymap.left:
            player.move("negx", 1)
            moved = True
        elif pressed in player_variables.deplacements_keymap.right:
            player.move("posx", 1)
            moved = True
        elif pressed in player_variables.deplacements_keymap.up:
            player.move("negy", 1)
            moved = True
        elif pressed in player_variables.deplacements_keymap.down:
            player.move("posy", 1)
            moved = True

        if moved:
            player.drawer.switchState("walk")
    else:
        player.drawer.switchState("idle")

run()