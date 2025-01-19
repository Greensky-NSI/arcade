from p5 import run, size, background
from src.utils.globals import ENV
from src.classes.mobs.Bomb import Bomb

bomb: Bomb

def setup():
    global bomb
    background(128)

    size(ENV.WIDTH, ENV.HEIGHT)
    bomb = Bomb(ENV.WIDTH // 2, ENV.HEIGHT // 2)

def draw():
    background(128)
    if bomb.ready:
        bomb.draw()

    bomb.tick()

run()