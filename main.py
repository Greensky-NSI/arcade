from p5 import run, size, background
from src.utils.globals import ENV
from src.classes.core.Menu import Menu

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


run()