from math import floor
from random import randint
from typing import Dict

from p5 import rect, fill, stroke, push_matrix, pop_matrix, strokeWeight, no_stroke, load_image, image

from classes.mobs import Bomb
from classes.mobs.Player import Player


class Labyrinthe:
    ordered_list = []
    colored_by = {}
    colors_attribution = {}
    players: Dict[str, Player] = {}
    won = False
    stats_at = {}

    def __init__(self, largeur, hauteur, taille_case, *, obstacle_proba: float = 0.95):
        self.largeur = largeur
        self.hauteur = hauteur
        self.taille_case = taille_case
        self.nb_lignes = hauteur // taille_case
        self.nb_colonnes = largeur // taille_case
        self.grille = [["vide" for i in range(self.nb_colonnes)] for i in range(self.nb_lignes)]
        self.obstacles = []
        self.indestructibles = []

        self.obstacle_proba = obstacle_proba

        self.assets = {
            "bombs": load_image("src/assets/sprites/stats/bomb.png"),
            "radius": load_image("src/assets/sprites/stats/radius.png"),
            "speed": load_image("src/assets/sprites/stats/speed.png")
        }

    def register_player(self, player: Player, uuid, color):
        self.players[uuid] = player
        self.colors_attribution[uuid] = color
        return self

    def color_case(self, x, y, uuid):
        self.colored_by[(x, y)] = uuid

        if self.count_cases_of(uuid) >= 35:
            self.win_game()

    def count_cases_of(self, uuid):
        return len([k for k, v in self.colored_by.items() if v == uuid])

    def uncolor_cases_of(self, uuid):
        for case in list(self.colored_by.keys())[:]:
            if self.colored_by[case] == uuid:
                del self.colored_by[case]

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

    def order(self):
        base_list = sorted([[self.grille[y][x], x, y] for y in range(self.nb_lignes) for x in range(self.nb_colonnes)], key=lambda item: ("vide", "obstacle", "indestructible").index(item[0]))

        for i, square in enumerate(base_list):
            if square[0] == "obstacle":
                if randint(0, 100) > self.obstacle_proba * 100:
                    base_list[i][0] = "vide"
                    self.grille[square[2]][square[1]] = "vide"
                    continue
            base_list[i] = tuple(base_list[i])

        self.ordered_list = base_list[:]

    def blocks(self, x, y):
        return {
            "left": x - 1 >= 0 and self.grille[y][x - 1] != "vide",
            "right": x + 1 < self.nb_colonnes and self.grille[y][x + 1] != "vide",
            "up": y - 1 >= 0 and self.grille[y - 1][x] != "vide",
            "down": y + 1 < self.nb_lignes and self.grille[y + 1][x] != "vide"
        }
    def to_lab_cords(self, x, y):
        return floor(x / self.taille_case), floor(y / self.taille_case)
    def to_real_cords(self, x, y):
        return x * self.taille_case, y * self.taille_case

    def display(self, square_list):
        push_matrix()
        for square in square_list:
            square_type = square[0]
            x, y = square[1], square[2]

            stroke(20, 20, 20)
            strokeWeight(1)

            if square_type == "vide":
                if (x, y) in self.colored_by:
                    fill(*self.colors_attribution[self.colored_by[(x, y)]])
                else:
                    fill(206, 206, 206)
            elif square_type == "obstacle":
                fill(61, 226, 193)
            elif square_type == "indestructible":
                fill(35, 90, 132)

            rect((x * self.taille_case, y * self.taille_case), self.taille_case, self.taille_case)

            if (x, y) in self.stats_at:
                stat = self.stats_at[(x, y)]
                image(self.assets[stat], x * self.taille_case + 8, y * self.taille_case + 8)
        pop_matrix()

    def affichage_opti(self, x, y):
        x = x // self.taille_case
        y = y // self.taille_case

        x_min = max(0, x - 1)
        x_max = min(self.nb_colonnes, x + 2)

        y_min = max(0, y - 2)
        y_max = min(self.nb_lignes, y + 3)

        square_list = [(self.grille[j][i], i, j) for j in range(y_min, y_max) for i in range(x_min, x_max)]

        self.display(square_list)

    def afficher_laby(self):
        self.display(self.ordered_list)

    def win_game(self):
        self.won = True

    def bomb_explode_callback(self, bomb: Bomb):
        square = self.to_lab_cords(bomb.x, bomb.y)
        radius = bomb.stats["range"]

        obstacles = {
            "left": (None, None),
            "right": (None, None),
            "up": (None, None),
            "down": (None, None)
        }
        for x in range(1, radius + 1):
            if self.grille[square[1]][square[0] + x] != "vide":
                obstacles["right"] = (square[0] + x - 1, square[1])
                break
        for x in range(1, radius + 1):
            if self.grille[square[1]][square[0] - x] != "vide":
                obstacles["left"] = (square[0] - x + 1, square[1])
                break
        for y in range(1, radius + 1):
            if self.grille[square[1] + y][square[0]] != "vide":
                obstacles["down"] = (square[0], square[1] + y - 1)
                break
        for y in range(1, radius + 1):
            if self.grille[square[1] - y][square[0]] != "vide":
                obstacles["up"] = (square[0], square[1] - y + 1)
                break

        affected_players = []

        for player in self.players.values():
            player_x, player_y = self.to_lab_cords(player.x, player.y)
            if (obstacles["left"][0] or square[0] - radius) <= player_x <= (obstacles["right"][0] or square[0] + radius) and (obstacles["up"][1] or square[1] - radius) <= player_y <= (obstacles["down"][1] or square[1] + radius):
                affected_players.append(player)

        for k, v in obstacles.items():
            x, y = v
            if x is None or y is None:
                continue

            if k == "left":
                x -= 1
            if k == "right":
                x += 1
            if k == "up":
                y -= 1
            if k == "down":
                y += 1
            
            if self.grille[y][x] == "indestructible":
                continue

            self.grille[y][x] = "vide"

            if randint(1, 100) > 40:
                self.summon_stat(x, y)

            self.affichage_opti(x * self.taille_case, y * self.taille_case)

        self.affichage_opti(square[0] * self.taille_case, square[1] * self.taille_case)

        if len(affected_players) > 0:
            for player in affected_players:
                player.die()
                self.uncolor_cases_of(player.uuid)


            base_list = [(self.grille[y][x], x, y) for y in range(self.nb_lignes) for x in range(self.nb_colonnes)]
            self.ordered_list = base_list[:]

            self.display(self.ordered_list)

    def summon_stat(self, x, y):
        available = ["speed"] * 30 + ["bombs"] * 40 + ["radius"] * 30
        stat = available[randint(0, 99)]

        self.stats_at[(x, y)] = stat

    def is_on_stat(self, x, y):
        return (x, y) in self.stats_at

    def collect_stat(self, x, y, player: Player):
        if not self.is_on_stat(x, y):
            return

        stat = self.stats_at[(x, y)]
        if stat == "bombs":
            player.player_stats.add_bombs(1)
        elif stat == "speed":
            player.player_stats.add_speed(1)
        elif stat == "radius":
            player.player_stats.add_range(1)
        else:
            raise ValueError(f"Unknown stat {stat}")

        del self.stats_at[(x, y)]


models = {
    "one": {
        "indestructibles": [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (5, 5), (5, 6), (5, 7), (5, 7), (6, 7), (7, 7), (8, 7), (9, 7), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3), (1, 4), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (1, 12), (0, 9), (3, 5), (3, 6), (3, 6), (3, 7), (3, 8), (3, 9), (3, 9), (4, 9), (5, 9), (5, 9), (6, 9), (6, 9), (7, 9), (8, 9), (11, 6), (11, 6), (12, 6), (13, 6), (14, 6), (14, 6), (15, 6), (15, 7), (15, 8), (15, 9), (14, 9), (13, 9), (12, 9), (12, 9), (11, 9), (11, 9), (11, 8), (11, 8), (11, 7), (11, 7), (12, 7), (13, 7), (13, 7), (14, 7), (14, 8), (14, 8), (13, 8), (12, 8), (9, 5), (9, 5), (9, 3), (9, 3), (10, 3), (11, 3), (9, 9), (9, 10), (9, 10), (9, 11), (10, 11), (11, 11), (11, 11), (12, 11), (14, 11), (14, 11), (15, 11), (16, 11), (16, 11), (17, 11), (17, 11), (17, 10), (17, 10), (17, 9), (17, 9), (17, 9), (17, 7), (17, 7), (17, 6), (17, 5), (17, 4), (17, 4), (16, 4), (16, 4), (15, 4), (13, 4), (13, 4), (12, 4), (12, 4), (12, 4), (11, 4), (11, 4), (3, 11), (3, 11), (4, 11), (4, 11), (5, 11), (6, 11), (6, 11), (7, 11), (7, 11), (7, 12), (7, 12), (7, 13), (1, 14), (2, 14), (2, 14), (3, 14), (3, 13), (3, 13), (4, 13), (5, 13), (5, 15), (6, 15), (7, 15), (7, 15), (8, 15), (9, 15), (9, 14), (9, 14), (9, 13), (11, 13), (11, 13), (12, 13), (12, 13), (13, 13), (13, 13), (14, 13), (14, 13), (15, 13), (15, 13), (15, 14), (15, 14), (16, 14), (17, 14), (15, 15), (14, 15), (13, 15), (12, 15), (12, 15), (11, 15), (11, 15), (11, 15), (17, 13), (17, 13), (18, 13), (19, 13), (19, 13), (19, 12), (19, 11), (19, 11), (19, 10), (19, 10), (19, 9), (19, 7), (19, 6), (19, 5), (19, 5), (19, 15), (20, 15), (20, 15), (22, 14), (22, 13), (22, 13), (22, 12), (22, 11), (22, 11), (22, 10), (21, 13), (21, 13), (21, 11), (21, 11), (15, 2), (15, 2), (13, 3), (13, 1), (13, 1), (12, 1), (11, 1), (10, 1), (9, 1), (11, 0), (11, 0), (21, 1), (20, 1), (22, 2), (22, 3), (20, 3), (22, 1), (22, 1), (19, 1), (18, 1), (18, 1), (16, 0), (15, 0), (16, 2), (16, 2), (20, 5), (20, 5), (20, 4), (19, 3), (19, 3), (17, 3), (17, 3), (16, 3), (16, 3), (22, 5), (22, 5), (22, 6), (21, 7), (21, 9), (21, 9), (21, 9), (21, 8), (21, 8), (23, 8), (23, 8)],
        "obstacles": [(3, 0), (8, 1), (10, 0), (9, 0), (12, 0), (13, 0), (6, 1), (12, 3), (15, 3), (19, 4), (9, 2), (10, 2), (13, 2), (12, 2), (14, 0), (14, 1), (15, 1), (21, 10), (21, 12), (4, 0), (4, 2), (3, 2), (2, 2), (1, 2), (0, 5), (1, 5), (0, 7), (0, 8), (0, 13), (0, 11), (0, 10), (3, 15), (4, 15), (4, 14), (6, 14), (7, 14), (8, 12), (9, 12), (10, 15), (14, 14), (11, 14), (12, 14), (10, 13), (11, 12), (12, 12), (20, 0), (19, 0), (18, 0), (22, 4), (23, 4), (23, 3), (23, 6), (23, 7), (22, 8), (22, 9), (17, 1), (18, 2), (18, 3), (20, 2), (21, 2), (21, 3), (21, 6), (20, 6), (20, 7), (20, 8), (18, 5), (18, 6), (18, 7), (18, 8), (16, 13), (16, 15), (17, 15), (18, 15), (18, 14), (19, 14), (2, 6), (2, 7), (2, 8), (2, 10), (3, 10), (4, 10), (7, 10), (8, 10), (5, 12), (4, 12), (3, 12), (2, 12), (8, 5), (9, 4), (10, 4), (13, 5), (15, 5), (16, 7), (16, 9), (14, 10), (12, 10), (10, 7), (10, 9), (5, 8), (6, 8), (7, 8), (4, 6), (4, 5), (9, 6), (8, 6), (6, 4), (5, 4), (4, 4), (18, 10), (18, 11), (18, 12), (13, 12), (14, 12), (15, 12), (20, 13), (20, 11), (20, 10), (23, 9), (23, 10), (23, 12), (14, 4)]
    }
}
