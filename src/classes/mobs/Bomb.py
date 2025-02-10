from p5 import translate, image, resetMatrix, pushMatrix, popMatrix
from src.classes.core.Drawer import Drawer
from src.classes.core.Timer import Timer

class Bomb:
    tickTimer = Timer(20, 1)
    explodeTimer = Timer(160, 1)
    drawer: Drawer
    exploded = False

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.timer = 3

        self.drawer = Drawer("src/assets/objects/bomb", {
            "ticking": 9
        })

    @property
    def ready(self):
        return self.drawer.ready

    def tick(self):
        self.explodeTimer.tick()

        if self.explodeTimer.ticked:
            self.drawer.lockAt(8)
            self.exploded = True

        return self.explodeTimer.ticked

    def draw(self):
        if self.tickTimer.tick():
            self.drawer.tick()

        img = self.drawer.image

        resetMatrix()
        pushMatrix()

        translate(self.x, self.y)
        image(img, 0, 0)

        popMatrix()