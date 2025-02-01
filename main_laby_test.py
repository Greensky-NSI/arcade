from p5 import run, size, background

from src.typing.custom_types import *
from src.utils.globals import ENV
from src.classes.core.labyrinthe import Labyrinthe, models

laby: Labyrinthe
def setup():
    global laby
    background(128)

    laby = Labyrinthe(ENV.WIDTH, ENV.HEIGHT, 50, model_folder_name="model_one", model_assets_indestructibles_count=2, model_assets_obstacles_count=7, obstacle_proba=.84)


    laby.indestructible(models["one"]["indestructibles"])
    laby.obstacle(models["one"]["obstacles"])

    laby.order()
    size(ENV.WIDTH, ENV.HEIGHT)

def draw():
    background(128)

    laby.afficher_laby()

run()