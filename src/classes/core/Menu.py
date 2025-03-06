from p5 import load_image, image, fill, stroke, stroke_weight, rect, scale, push_matrix, reset_matrix, text_align, \
    CENTER, text

from src.utils.globals import ENV


class Menu:
    """
    Classe représentant le menu principal de l'application.
    """

    asset = None
    validated = False

    def __init__(self):
        """
        Initialise le menu en chargeant l'image de fond.
        """
        self.asset = load_image("src/assets/images/menu_bg.jpg")

    @property
    def ready(self):
        """
        Vérifie si l'image de fond est chargée.

        :return: True si l'image est chargée, sinon False.
        """
        return self.asset is not None

    def check_click(self, x: int, y: int):
        """
        Vérifie si un clic est dans la zone du bouton.

        :param x: Coordonnée x du clic.
        :param y: Coordonnée y du clic.
        :return: True si le clic est dans la zone, sinon False.
        """
        return 524 <= x <= 675 and 379 <= y <= 447

    def mark_validated(self):
        """
        Marque le menu comme validé.
        """
        self.validated = True

    def draw(self):
        """
        Dessine le menu à l'écran.
        """
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