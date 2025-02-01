from typing import Literal
from src.utils.globals import ENV

def parse_number_between_walls(number: int, wall: Literal["WIDTH", "HEIGHT"]) -> int:
    return max(0, min(number, getattr(ENV, wall)))
