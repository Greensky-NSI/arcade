def check_direction(direction):
    assert direction in ("posx", "posy", "negx", "negy"), "La direction doit être posx, posy, negx ou negy"

    return True

def check_positive_integer(number):
    assert isinstance(number, int) and number >= 0, "Le nombre doit être entier et positif"