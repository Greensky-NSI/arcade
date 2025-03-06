from typing import Literal
from src.utils.globals import ENV

def parse_number_between_walls(number: int, wall: Literal["WIDTH", "HEIGHT"]) -> int:
    """
    Assure que le nombre donné est dans les limites de la dimension du mur spécifié.

    Args:
        number (int): Le nombre à contraindre.
        wall (Literal["WIDTH", "HEIGHT"]): La dimension du mur pour contraindre le nombre.

    Returns:
        int: Le nombre contraint dans les limites de 0 et de la dimension du mur spécifié.
    """
    return max(0, min(number, getattr(ENV, wall)))