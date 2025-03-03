from p5 import run, size, background, PImage, load_image, image

from assets.loaders.banner import LoadDraver
from classes.mobs import Bomb
from labyrinthe import Labyrinthe, models
from src.classes.core.Menu import Menu
from src.classes.mobs.Player import Player
from src.typing.custom_types import *
from src.utils.globals import player_variables, ENV


player: Player 
menu: Menu
laby: Labyrinthe
laby_started = False
win_screen: PImage
draver: LoadDraver


def setup():
    global menu, player, laby, win_screen, draver
    background(128)

    size(ENV.WIDTH, ENV.HEIGHT)

    draver = LoadDraver()
    draver.load()

    laby = Labyrinthe(ENV.WIDTH, ENV.HEIGHT, 50, obstacle_proba=.85)

    win_screen = load_image("src/assets/images/win_screen.jpg")

    laby.obstacle(models["one"]["obstacles"])
    laby.indestructible(models["one"]["indestructibles"])
    laby.order()

    menu = Menu()
    player = Player()

    laby.register_player(player, player.uuid, (240, 247, 46))


def draw():
    global laby_started, win_screen, draver

    if not draver.ended:
        draver.draw()
        return

    if menu.ready and not menu.validated:
        background(128)

        menu.draw()
        if mouse_is_pressed:
            if menu.check_click(mouse_x, mouse_y):
                menu.mark_validated()

                player.tp(25, 40)

        return

    if not laby_started:
        background(128)

        laby.afficher_laby()
        laby_started = True
    if laby.won:
        image(win_screen, 0, 0, ENV.WIDTH, ENV.HEIGHT)
        return

    laby.affichage_opti(player.x, player.y)

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
        player_x, player_y = laby.to_lab_cords(player.x, player.y)
        block_x, block_y = laby.to_real_cords(player_x, player_y)

        laby.color_case(player_x, player_y, player.uuid)

        if laby.is_on_stat(player_x, player_y):
            laby.collect_stat(player_x, player_y, player)

        moved = False

        blocks = laby.blocks(player_x, player_y)
        if pressed in player_variables.deplacements_keymap.left:
            if blocks["left"]:
                player.move("negx", 1, block_x + 5)
            else:
                player.move("negx", 1)
            moved = True
        elif pressed in player_variables.deplacements_keymap.right:
            if blocks["right"]:
                player.move("posx", 1, block_x + 45)
            else:
                player.move("posx", 1)
            moved = True
        elif pressed in player_variables.deplacements_keymap.up:
            if blocks["up"]:
                player.move("negy", 1, block_y + 5)
            else:
                player.move("negy", 1)
            moved = True
        elif pressed in player_variables.deplacements_keymap.down:
            if blocks["down"]:
                player.move("posy", 1, block_y + 45)
            else:
                player.move("posy", 1)
            moved = True
        if key == ' ':
            player.place_bomb(laby.bomb_explode_callback)
            moved=True

        if moved:
            player.drawer.switchState("walk")
    else:
        player.drawer.switchState("idle")

run()