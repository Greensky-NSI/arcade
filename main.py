from p5 import run, size, background
from src.classes.mobs.Player import Player
from src.classes.mobs.Bomb import Bomb
from src.utils.globals import player_variables, ENV
from src.typing.custom_types import *

player: Player 
bombs=[]

def setup():
    global player
    background(128)

    size(ENV.WIDTH, ENV.HEIGHT)
    player = Player()
    player.tp(ENV.WIDTH // 2, ENV.HEIGHT // 2)

def draw():
    global bombs
    background(128)
    if player.ready:
        player.draw()

    for bomb in bombs:
        if bomb.ready:
            bomb.draw()
        if bomb.tick():
            bombs.remove(bomb)

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
            bombs.append(Bomb(player.x, player.y))
            moved=True

        if moved:
            player.drawer.switchState("walk")
    else:
        player.drawer.switchState("idle")

run()