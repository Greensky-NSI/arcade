from typing import Literal, TypedDict


class ScoreTableType(TypedDict):
    score: int
    type: Literal[0, 1]
