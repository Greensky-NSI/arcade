from p5 import rect, fill, circle, no_stroke, line, stroke_weight, stroke

class Labyrinthe:
    ordered_list = []

    def __init__(self, largeur, hauteur, taille_case):
        self.largeur = largeur
        self.hauteur = hauteur
        self.taille_case = taille_case
        self.nb_lignes = hauteur // taille_case
        self.nb_colonnes = largeur // taille_case
        self.grille = [["vide" for i in range(self.nb_colonnes)] for i in range(self.nb_lignes)]
        self.obstacles = []
        self.indestructibles = []

    def obstacle(self, obstacles):
        self.obstacles = obstacles[:]
        for x, y in obstacles:
            self.grille[y][x] = "obstacle"

    def indestructible(self, indestructibles):
        self.indestructibles = indestructibles[:]
        for x, y in indestructibles:
            self.grille[y][x] = "indestructible"

    def void(self, voids):
        for x, y in voids:
            self.grille[y][x] = "vide"

    def muraille(self, x, y, *, fill_color = (80, 80, 80), stroke_color = (60, 60, 60)):
        fill(*fill_color)
        stroke(*stroke_color)
        stroke_weight(3)
        rect((x * self.taille_case, y * self.taille_case), self.taille_case, self.taille_case)

        # no_stroke()
        # circle((x * self.taille_case + self.taille_case * 0.3, y * self.taille_case + self.taille_case * 0.3), self.taille_case * 0.2)
        # circle((x * self.taille_case + self.taille_case * 0.7, y * self.taille_case + self.taille_case * 0.7), self.taille_case * 0.2)
        # circle((x * self.taille_case + self.taille_case * 0.5, y * self.taille_case + self.taille_case * 0.5), self.taille_case * 0.15)

        # line((x * self.taille_case, y * self.taille_case), (x * self.taille_case + self.taille_case, y * self.taille_case))
        # line((x * self.taille_case, y * self.taille_case + self.taille_case), (x * self.taille_case + self.taille_case, y * self.taille_case + self.taille_case))
        # line((x * self.taille_case, y * self.taille_case), (x * self.taille_case, y * self.taille_case + self.taille_case))
        # line((x * self.taille_case + self.taille_case, y * self.taille_case), (x * self.taille_case + self.taille_case, y * self.taille_case + self.taille_case))

    def order(self):
        self.ordered_list = sorted([(self.grille[y][x], x, y) for y in range(self.nb_lignes) for x in range(self.nb_colonnes)], key=lambda item: ("vide", "obstacle", "indestructible").index(item[0]))

    def afficher_laby(self):
        for square_type, x, y in self.ordered_list:
            if square_type == "vide":
                fill(240, 240, 255)
                stroke(200, 200, 255)
                rect((x * self.taille_case, y * self.taille_case), self.taille_case, self.taille_case)
            elif square_type == "obstacle":
                self.muraille(x, y)
            elif square_type == "indestructible":
                self.muraille(x, y, fill_color=(140, 100, 100), stroke_color=(120, 80, 80))


models = {
    "one": {
        "indestructibles": [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (5, 5), (5, 6), (5, 7), (5, 7), (6, 7), (7, 7), (8, 7), (9, 7), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3), (1, 4), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (1, 12), (0, 9), (3, 5), (3, 6), (3, 6), (3, 7), (3, 8), (3, 9), (3, 9), (4, 9), (5, 9), (5, 9), (6, 9), (6, 9), (7, 9), (8, 9), (11, 6), (11, 6), (12, 6), (13, 6), (14, 6), (14, 6), (15, 6), (15, 7), (15, 8), (15, 9), (14, 9), (13, 9), (12, 9), (12, 9), (11, 9), (11, 9), (11, 8), (11, 8), (11, 7), (11, 7), (12, 7), (13, 7), (13, 7), (14, 7), (14, 8), (14, 8), (13, 8), (12, 8), (9, 5), (9, 5), (9, 3), (9, 3), (10, 3), (11, 3), (9, 9), (9, 10), (9, 10), (9, 11), (10, 11), (11, 11), (11, 11), (12, 11), (14, 11), (14, 11), (15, 11), (16, 11), (16, 11), (17, 11), (17, 11), (17, 10), (17, 10), (17, 9), (17, 9), (17, 9), (17, 7), (17, 7), (17, 6), (17, 5), (17, 4), (17, 4), (16, 4), (16, 4), (15, 4), (13, 4), (13, 4), (12, 4), (12, 4), (12, 4), (11, 4), (11, 4), (3, 11), (3, 11), (4, 11), (4, 11), (5, 11), (6, 11), (6, 11), (7, 11), (7, 11), (7, 12), (7, 12), (7, 13), (1, 14), (2, 14), (2, 14), (3, 14), (3, 13), (3, 13), (4, 13), (5, 13), (5, 15), (6, 15), (7, 15), (7, 15), (8, 15), (9, 15), (9, 14), (9, 14), (9, 13), (11, 13), (11, 13), (12, 13), (12, 13), (13, 13), (13, 13), (14, 13), (14, 13), (15, 13), (15, 13), (15, 14), (15, 14), (16, 14), (17, 14), (15, 15), (14, 15), (13, 15), (12, 15), (12, 15), (11, 15), (11, 15), (11, 15), (17, 13), (17, 13), (18, 13), (19, 13), (19, 13), (19, 12), (19, 11), (19, 11), (19, 10), (19, 10), (19, 9), (19, 7), (19, 6), (19, 5), (19, 5), (19, 15), (20, 15), (20, 15), (22, 14), (22, 13), (22, 13), (22, 12), (22, 11), (22, 11), (22, 10), (21, 13), (21, 13), (21, 11), (21, 11), (15, 2), (15, 2), (13, 3), (13, 1), (13, 1), (12, 1), (11, 1), (10, 1), (9, 1), (11, 0), (11, 0), (21, 1), (20, 1), (22, 2), (22, 3), (20, 3), (22, 1), (22, 1), (19, 1), (18, 1), (18, 1), (16, 0), (15, 0), (16, 2), (16, 2), (20, 5), (20, 5), (20, 4), (19, 3), (19, 3), (17, 3), (17, 3), (16, 3), (16, 3), (22, 5), (22, 5), (22, 6), (21, 7), (21, 9), (21, 9), (21, 9), (21, 8), (21, 8), (23, 8), (23, 8)],
        "obstacles": [(3, 0), (8, 1), (10, 0), (9, 0), (12, 0), (13, 0), (6, 1), (12, 3), (15, 3), (19, 4), (9, 2), (10, 2), (13, 2), (12, 2), (14, 0), (14, 1), (15, 1), (21, 10), (21, 12), (4, 0), (4, 2), (3, 2), (2, 2), (1, 2), (0, 5), (1, 5), (0, 7), (0, 8), (0, 13), (0, 11), (0, 10), (3, 15), (4, 15), (4, 14), (6, 14), (7, 14), (8, 12), (9, 12), (10, 15), (14, 14), (11, 14), (12, 14), (10, 13), (11, 12), (12, 12), (20, 0), (19, 0), (18, 0), (22, 4), (23, 4), (23, 3), (23, 6), (23, 7), (22, 8), (22, 9), (17, 1), (18, 2), (18, 3), (20, 2), (21, 2), (21, 3), (21, 6), (20, 6), (20, 7), (20, 8), (18, 5), (18, 6), (18, 7), (18, 8), (16, 13), (16, 15), (17, 15), (18, 15), (18, 14), (19, 14), (2, 6), (2, 7), (2, 8), (2, 10), (3, 10), (4, 10), (7, 10), (8, 10), (5, 12), (4, 12), (3, 12), (2, 12), (8, 5), (9, 4), (10, 4), (13, 5), (15, 5), (16, 7), (16, 9), (14, 10), (12, 10), (10, 7), (10, 9), (5, 8), (6, 8), (7, 8), (4, 6), (4, 5), (9, 6), (8, 6), (6, 4), (5, 4), (4, 4), (18, 10), (18, 11), (18, 12), (13, 12), (14, 12), (15, 12), (20, 13), (20, 11), (20, 10), (23, 9), (23, 10), (23, 12), (14, 4)]
    }
}
