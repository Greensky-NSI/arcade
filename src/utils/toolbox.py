def check_direction(direction):
    """
    Vérifie si la direction donnée est valide.

    Args:
        direction (str): La direction à vérifier. Doit être 'posx', 'posy', 'negx' ou 'negy'.

    Returns:
        bool: True si la direction est valide, sinon une assertion est levée.
    """
    assert direction in ("posx", "posy", "negx", "negy"), "La direction doit être posx, posy, negx ou negy"

    return True

def check_positive_integer(number):
    """
    Vérifie si le nombre donné est un entier positif.

    Args:
        number (int): Le nombre à vérifier.

    Returns:
        bool: True si le nombre est un entier positif, sinon une assertion est levée.
    """
    assert isinstance(number, int) and number >= 0, "Le nombre doit être entier et positif"
    return True