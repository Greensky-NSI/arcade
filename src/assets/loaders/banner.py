from p5 import PImage, load_image, image, tint, rect, fill

from src.classes.core.Timer import Timer
from utils.globals import ENV


class LoadDraver:
    image: PImage
    timer: Timer
    ended = False

    def __init__(self):
        self.timer = Timer(180, 1)

    def load(self):
        self.image = load_image("src/assets/images/banner.jpg")

    def draw(self):
        self.timer.tick()

        endsAt = 60
        alpha = int(255 * (1 - self.timer.current_tick / endsAt))

        fill(128, 128, 128, alpha)
        image(self.image, 0, 0, ENV.WIDTH, ENV.HEIGHT)
        rect(0, 0, ENV.WIDTH, ENV.HEIGHT)

        if self.timer.ticked:
            self.ended = True
            return