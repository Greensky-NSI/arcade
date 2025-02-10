from p5 import run, size, background
from src.classes.core.Menu import Menu
from src.classes.mobs.Player import Player
from src.classes.mobs.Bomb import Bomb
from src.utils.globals import player_variables, ENV
from src.typing.custom_types import *

player: Player 
menu: Menu

def setup():
    global menu
    background(128)

    size(ENV.WIDTH, ENV.HEIGHT)
    menu = Menu()

def draw():
    background(128)
    if menu.ready:
        menu.draw()
        
        #TODO à compléter afin de pouvoir passer à la suite
        return

    if player.ready:
        player.draw()

    for bomb in player.bombs:
        if bomb.ready:
            bomb.draw()
            bomb.tick()
        if bomb.exploded:
            player.bombs.remove(bomb)

    if key_is_pressed:
        pressed = str(key).lower()

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
        if key==' ':
            player.place_bomb()
            moved=True

        if moved:
            player.drawer.switchState("walk")
    else:
        player.drawer.switchState("idle")

run()