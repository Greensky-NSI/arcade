from p5 import load_image, image, fill, stroke, stroke_weight, rect, scale, push_matrix, reset_matrix, text_align, \
    CENTER, text

from src.utils.globals import ENV


class Menu:
    asset = None

    def __init__(self):
        self.asset = load_image("src/assets/images/menu_bg.jpg")

    @property
    def ready(self):
        return self.asset is not None

    def draw(self):
        image(self.asset, 0, 0, ENV.WIDTH, ENV.HEIGHT)

        push_matrix()
        scale(ENV.WIDTH / 800, ENV.HEIGHT / 600)

        fill(23, 240, 78)
        text_align(CENTER)
        stroke(0)
        stroke_weight(2)

        # text("Jouer", 400, 300)

        fill(45, 250, 102, 50)
        stroke(45, 250, 45)
        stroke_weight(5)
        rect(350, 285, 100, 50)

        reset_matrix()