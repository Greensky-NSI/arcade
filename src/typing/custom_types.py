# Fichier de typage personnalisé pour avoir les types de toutes les variables de p5 (certaines sont inacessibles)
from typing import Literal

key_is_pressed: bool
key: str
mouse_x: int
mouse_y: int
mouse_is_pressed: bool
mouse_button: Literal["LEFT", "RIGHT", "CENTER"]