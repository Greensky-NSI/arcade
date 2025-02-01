# Variables à utiliser dans tout le projet
# Les variables sont définies ici sous forme de classe pour éviter les problèmes de portée, et pour avoir l'auto complétion dans les IDE, ainsi que la vérification de type/erreurs pré-exécution

## Variables relatives au joueur
class movements:
    left = ["q", "a", "left"]
    right = ["d", "right"]
    up = ["z", "w", "up"]
    down = ["s", "down"]

class player_variables:
    deplacements_keymap = movements

    dspeed = 3

class LabyrintheVariables:
    square_size: int = 50

class ENV:
    WIDTH = 1200
    HEIGHT = 800